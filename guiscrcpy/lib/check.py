"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging
import shutil
from subprocess import Popen, PIPE, call, TimeoutExpired

from ..lib.utils import decode_process, shellify as _
from ..platform.platform import System
from ..install.finder import open_exe_name_dialog

environment = System()


def get(ls, idx, default=""):
    try:
        return ls[idx]
    except IndexError:
        return default


def _get_dimension_raw_noexcept(path, device_id=None):
    if device_id:
        shell_adb = Popen(
            _("{} -s {} shell wm size".format(path, device_id)),
            stdout=PIPE, stderr=PIPE)
    else:
        shell_adb = Popen(_("{} shell wm size".format(path)),
                          stdout=PIPE, stderr=PIPE)
    return shell_adb


class ScrcpyNotFoundError(FileNotFoundError):
    pass


class ScrcpyBridge:
    def __init__(self, path=None):
        if path is not None:
            self.path = path
        elif shutil.which('scrcpy'):
            self.path = shutil.which('scrcpy')
        else:
            self.path = open_exe_name_dialog(None, 'scrcpy')
        if self.path is None:
            raise ScrcpyNotFoundError("Could not find `scrcpy` on PATH. Make "
                                      "sure scrcpy is installed and "
                                      "accessible from the terminal.")

    def start(self, args, stdout=PIPE, stderr=PIPE):
        proc = Popen(
            _("{} {}".format(self.path, args)),
            stdout=stdout,
            stderr=stderr,
        )
        return proc

    def get_path(self):
        return self.path


class AdbNotFoundError(FileNotFoundError):
    pass


class AdbRuntimeError(RuntimeError):
    pass


class AndroidDebugBridge:
    def __init__(self, path=None):
        if path is not None:
            self.path = path
        elif shutil.which('adb') is not None:
            self.path = shutil.which('adb')
        else:
            self.path = open_exe_name_dialog(None, 'adb')
        if self.path is None:
            AdbNotFoundError("Could not find `adb` on PATH. "
                             "Make sure adb is installed accessible "
                             "from the terminal")

    def shell_input(self, command, device_id=None):
        path = self.path
        if device_id:
            Popen(
                _("{} -s {} shell input {}".format(path, device_id, command)),
                stdout=PIPE,
                stderr=PIPE,
            )
        else:
            Popen(
                _("{} shell input {}".format(path, command)),
                stdout=PIPE,
                stderr=PIPE,
            )

    def get_path(self):
        return self.path

    def kill_adb_server(self):
        self.command(self.path, "kill-server")

    def get_dimensions(self, device_id=None):
        shell_adb = _get_dimension_raw_noexcept(
            path=self.path, device_id=device_id
        )
        try:
            if shell_adb.wait(timeout=3) != 0:
                print("E: Command 'adb shell wm size' exited with {}".format(
                    shell_adb.returncode))
                return False
        except TimeoutExpired:
            print("E: adb falied; timeout exceeded 10s, killing and "
                  "respawining adb")
            self.kill_adb_server()
            if isinstance(device_id, str) and device_id.count('.') >= 3:
                self.command(self.path, "connect {}".format(device_id))
            shell_adb = _get_dimension_raw_noexcept(
                path=self.path, device_id=device_id
            )
            if shell_adb.wait(timeout=8) != 0:
                print("E: Command 'adb shell wm size' exited with {}".format(
                    shell_adb.returncode))
                return False
        raw_dimensions = shell_adb.stdout.read().decode().strip('\n')
        for i in ['Override size', 'Physical size']:
            if i in raw_dimensions:
                out = raw_dimensions[raw_dimensions.find(i):]
                out_decoded = out.split(':')[1].strip()
                dimension_values = out_decoded.split('x')
                return dimension_values

        # As the for loop did not find any device; and hence we have reached
        # this line. Announce to the user regarding the same
        logging.error(
            "AndroidDeviceError: adb shell wm size did not return "
            "'Physical Size' or 'Override Size'"
        )
        return False

    def shell(self, command, device_id=None):
        if device_id:
            po = Popen(_("{} -s {} shell {}".format(
                self.path, device_id, command)),
                stdout=PIPE, stderr=PIPE)
        else:
            po = Popen(_("{} shell {}".format(self.path, command)),
                       stdout=PIPE, stderr=PIPE)
        return po

    def command(self, command, device_id=None):
        if device_id:
            adb_shell_output = Popen(
                _("{} -s {} {}".format(self.path, device_id, command)),
                stdout=PIPE,
                stderr=PIPE)
        else:
            adb_shell_output = Popen(_("{} {}".format(self.path, command)),
                                     stdout=PIPE, stderr=PIPE)
        return adb_shell_output

    def tcpip(self, port=5555, identifier=""):
        if identifier:
            command = "{path} -s {identifier} -d tcpip {port}"
        else:
            command = "{path} -d tcpip {port}"
        exit_code = call(
            _(command.format(path=self.path, port=port,
                             identifier=identifier)),
            stdout=PIPE,
            stderr=PIPE
        )
        return exit_code

    def devices(self):
        proc = Popen(_(self.path + " devices"), stdout=PIPE)
        output = [[y.strip() for y in x.split('\t')]
                  for x in decode_process(proc)[1:]][:-1]

        logging.debug("ADB: {}".format(output))
        return output

    def devices_detailed(self):
        proc = Popen(_(self.path + " devices -l"), stdout=PIPE)
        output = [[y.strip() for y in x.split()]
                  for x in decode_process(proc)[1:]][:-1]
        devices_found = []
        for device in output:
            # https://github.com/srevinsaju/guiscrcpy/issues/117
            if 'udev' in device and 'permission' in device:
                # This is an error with some linux and Windows OSes
                # This happens because the udev is not configured
                # and linux adb does not have access to reading the device
                # the status hence should be 'no_permission'
                status = 'no_permission'
            else:
                status = device[1]
            description = {
                'identifier': device[0],
                'status': status,
                'product': get(device, 2, ':').split(':')[-1],
                'model': get(device, 3, ':').split(':')[-1],
                'device': get(device, 4, ':').split(':')[-1],
                'transport_id': get(device, 5, ':').split(':')[-1]
            }
            devices_found.append(description)
        logging.debug("ADB: {}".format(devices_found))
        return devices_found

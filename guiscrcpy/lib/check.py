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
from subprocess import Popen, PIPE, call, TimeoutExpired

from guiscrcpy.lib.utils import decode_process, check_existence, shellify as _
from guiscrcpy.platform.platform import System

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


class scrcpy:
    path = None

    def __init__(self):
        pass

    @staticmethod
    def start(path, args):
        Popen(
            _("{} {}".format(path, args)),
            stdout=PIPE,
            stderr=PIPE,
        )
        return True

    @staticmethod
    def device():
        pass

    @staticmethod
    def check():
        scrcpy_path = check_existence(
            environment.paths(), ['scrcpy'], False, True)
        if scrcpy_path and (isinstance(scrcpy_path, list)):
            return scrcpy_path[0]
        else:
            logging.error(
                'scrcpy could not be found in any of the paths {}'.format(
                    environment.paths()))


class adb:
    path = None

    def __init__(self):
        pass

    @staticmethod
    def check():
        adb_path = check_existence(environment.paths(), ['adb'], False, True)
        if adb_path and (isinstance(adb_path, list)):
            return adb_path[0]
        else:
            logging.error(
                'adb could not be found in any of the paths {}'.format(
                    environment.paths()))

    @staticmethod
    def shell_input(path, command, device_id=None):
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

    @staticmethod
    def kill_adb_server(path):
        adb.command(path, "kill-server")

    @staticmethod
    def get_dimensions(path, device_id=None):
        shell_adb = _get_dimension_raw_noexcept(
            path=path, device_id=device_id
        )
        try:
            if shell_adb.wait(timeout=3) != 0:
                print("E: Command 'adb shell wm size' exited with {}".format(
                    shell_adb.returncode))
                return False
        except TimeoutExpired:
            print("E: adb falied; timeout exceeded 10s, killing and "
                  "respawining adb")
            adb.kill_adb_server(path)
            if isinstance(device_id, str) and device_id.count('.') >= 3:
                adb.command(adb.path, "connect {}".format(device_id))
            shell_adb = _get_dimension_raw_noexcept(
                path=path, device_id=device_id
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

    @staticmethod
    def shell(path, command, device_id=None):
        if device_id:
            Popen(_("{} -s {} shell {}".format(path, device_id, command)),
                  stdout=PIPE, stderr=PIPE)
        else:
            Popen(_("{} shell {}".format(path, command)),
                  stdout=PIPE, stderr=PIPE)
        return True

    @staticmethod
    def command(path, command, device_id=None):
        if device_id:
            adb_shell_output = Popen(
                _("{} -s {} {}".format(path, device_id, command)), stdout=PIPE,
                stderr=PIPE)
        else:
            adb_shell_output = Popen(_("{} {}".format(path, command)),
                                     stdout=PIPE, stderr=PIPE)
        return adb_shell_output

    @staticmethod
    def tcpip(path, port=5555, identifier=""):
        if identifier:
            command = "{path} -s {identifier} -d tcpip {port}"
        else:
            command = "{path} -d tcpip {port}"
        exit_code = call(
            _(command.format(path=path, port=port, identifier=identifier)),
            stdout=PIPE,
            stderr=PIPE
        )
        return exit_code

    @staticmethod
    def devices(increment=''):
        if increment is None:
            raise FileNotFoundError(
                "guiscrcpy couldn't find adb. "
                "Please specify path to adb in configuration filename"
            )
        proc = Popen(_(increment + " devices"), stdout=PIPE)
        output = [[y.strip() for y in x.split('\t')]
                  for x in decode_process(proc)[1:]][:-1]

        logging.debug("ADB: {}".format(output))
        return output

    @staticmethod
    def devices_detailed(increment=''):
        if increment is None:
            raise FileNotFoundError(
                "guiscrcpy couldn't find adb. "
                "Please specify path to adb in configuration filename"
            )
        proc = Popen(_(increment + " devices -l"), stdout=PIPE)
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

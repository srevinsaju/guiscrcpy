import logging
import sys
from subprocess import PIPE, TimeoutExpired, call
from typing import List

from .base import Bridge
from ..check import _get_dimension_raw_noexcept, get
from ..utils import decode_process, open_process
from ...logging import make_logger


class AndroidDebugBridge(Bridge):
    logger = make_logger("adb")
    name = "adb"

    def get_target_android_version(self, device_id=None):
        api = -1

        # This function uses device API level to identify different android versions instead of
        # Android version as they can break in scenarios where version names are like 8.1.0
        # Fixes: https://github.com/srevinsaju/guiscrcpy/issues/248
        _proc = self.shell("getprop ro.build.version.sdk", device_id=device_id)
        _ecode = _proc.wait()

        if _ecode == 0:
            api = int(_proc.stdout.read())
        else:
            raise RuntimeError("adb did not respond to getprop ro.build.version.sdk")

        return api

    def shell_input(self, command, device_id=None):
        cmd = [self.path, "-s", device_id, "shell", "input", command] if device_id else [self.path, "shell", "input", command]
        open_process(cmd, stdout=PIPE, stderr=PIPE)

    def kill_adb_server(self):
        self.command(self.path, "kill-server")

    def get_dimensions(self, device_id=None):
        shell_adb = _get_dimension_raw_noexcept(path=self.path, device_id=device_id)
        try:
            if shell_adb.wait(timeout=3) != 0:
                self.logger.warning(
                    "Command '{}' exited with '{}'".format(
                        shell_adb.args, shell_adb.returncode
                    )
                )
                return False
        except TimeoutExpired:
            self.logger.warning("adb falied; timeout exceeded 10s, killing and respawining adb")
            self.kill_adb_server()
            if isinstance(device_id, str) and device_id.count(".") >= 3:
                self.command(self.path, "connect {}".format(device_id))
            shell_adb = _get_dimension_raw_noexcept(path=self.path, device_id=device_id)
            if shell_adb.wait(timeout=8) != 0:
                self.logger.warning(
                    "Command '{}' exited with '{}'".format(
                        shell_adb.args, shell_adb.returncode
                    )
                )
                return False
        raw_dimensions = shell_adb.stdout.read().decode().strip("\n")
        for i in ["Override size", "Physical size"]:
            if i in raw_dimensions:
                out = raw_dimensions[raw_dimensions.find(i) :]
                out_decoded = out.split(":")[1].strip()
                dimension_values = out_decoded.split("x")
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
            po = open_process(
                [self.path, "-s", device_id, "shell", command],
                stdout=PIPE,
                stderr=PIPE,
            )
        else:
            po = open_process(
                [self.path, "shell", command],
                stdout=PIPE, 
                stderr=PIPE,
            )
        return po

    def command(self, command: List[str], device_id=None):
        cmd = [self.path, "-s", device_id] if device_id else [self.path]
        cmd.extend(command)
        adb_shell_output = open_process(cmd, stdout=PIPE, stderr=PIPE)
        return adb_shell_output

    def tcpip(self, port=5555, identifier=""):
        if identifier:
            command = [self.path, "-s", identifier, "-d", "tcpip", port]
        else:
            command = [self.path, "-d", "tcpip", port]
        exit_code = call(command, stdout=sys.stdout, stderr=sys.stdout)
        return exit_code

    def devices(self):
        proc = open_process([self.path, "devices"], stdout=PIPE)
        output = [[y.strip() for y in x.split("\t")] for x in decode_process(proc)[1:]][
            :-1
        ]

        logging.debug("ADB: {}".format(output))
        return output

    def devices_detailed(self):
        proc = open_process([self.path, "devices", "-l"], stdout=PIPE)
        output = [[y.strip() for y in x.split()] for x in decode_process(proc)[1:]][:-1]
        devices_found = []
        for device in output:
            # https://github.com/srevinsaju/guiscrcpy/issues/117
            if "udev" in device and "permission" in device:
                # This is an error with some linux and Windows OSes
                # This happens because the udev is not configured
                # and linux adb does not have access to reading the device
                # the status hence should be 'no_permission'
                status = "no_permission"
            else:
                status = device[1]
            description = {
                "identifier": device[0],
                "status": status,
                "product": get(device, 2, ":").split(":")[-1],
                "model": get(device, 3, ":").split(":")[-1],
                "device": get(device, 4, ":").split(":")[-1],
                "transport_id": get(device, 5, ":").split(":")[-1],
            }
            devices_found.append(description)
        logging.debug("ADB: {}".format(devices_found))
        return devices_found

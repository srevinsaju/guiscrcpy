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
import shlex
from subprocess import Popen, PIPE
from guiscrcpy.lib.utils import decode_process, check_existence, shellify as _
from guiscrcpy.platform.platform import System

environment = System()


def check(binary):
    pass


class scrcpy:
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
        if scrcpy_path and (type(scrcpy_path) is list):
            return scrcpy_path[0]
        else:
            logging.error('scrcpy could not be found in any of the paths {}'.format(
                environment.paths()))


class adb:
    def __init__(self):
        pass

    @staticmethod
    def check():
        adb_path = check_existence(environment.paths(), ['adb'], False, True)
        if adb_path and (type(adb_path) is list):
            return adb_path[0]
        else:
            logging.error('adb could not be found in any of the paths {}'.format(
                environment.paths()))

    @staticmethod
    def shell_input(path, command):
        shellx = Popen(
            _("{} shell input {}".format(path, command)),
            stdout=PIPE,
            stderr=PIPE,
        )

    @staticmethod
    def get_dimensions(path):
        shellx = Popen(
            _("{} shell wm size".format(path)),
            stdout=PIPE,
            stderr=PIPE,
        )
        raw_dimensions = shellx.stdout.read().decode().strip('\n')
        for i in ['Override size', 'Physical size']:
            if i in raw_dimensions:
                out = raw_dimensions[raw_dimensions.find(i):]
                out_decoded = out.split(':')[1].strip()
                dimValues = out_decoded.split('x')
                return dimValues
        else:
            logging.error(
                "AndroidDeviceError: adb shell wm size did not return 'Physical Size' or 'Override Size'"
            )
            return False

    @staticmethod
    def shell(path, command):
        shellx = Popen(
            _("{} shell {}".format(path, command)),
            stdout=PIPE,
            stderr=PIPE,
        )
        return True

    @staticmethod
    def command(path, command):
        shellx = Popen(
            _("{} {}".format(path, command)),
            stdout=PIPE,
            stderr=PIPE,
        )
        return shellx

    @staticmethod
    def devices(increment=''):
        if increment is None:
            raise FileNotFoundError(
                "guiscrcpy couldn't find adb. Please specify path to adb in configuration file")
        proc = Popen(_(increment + " devices"), stdout=PIPE)
        output = decode_process(proc)[1].split('\t')
        logging.debug("ADB: {}".format(output))
        return output

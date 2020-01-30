import logging
import shlex
from subprocess import Popen, PIPE
from guiscrcpy.lib.utils import decode_process, check_existence
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
            shlex.split("{} {}".format(path, args)),
            stdout=PIPE,
            stderr=PIPE,
        )
        return True

    @staticmethod
    def device():
        pass

    @staticmethod
    def check():
        scrcpy_path = check_existence(environment.paths(), ['scrcpy'], False)
        if scrcpy_path and (type(scrcpy_path) is list):
            return scrcpy_path[0]
        else:
            logging.error('scrcpy could not be found in any of the paths {}'.format(environment.paths()))

class adb:
    def __init__(self):
        pass

    @staticmethod
    def check():
        adb_path = check_existence(environment.paths(), ['adb'], False)
        if adb_path and (type(adb_path) is list):
            return adb_path[0]
        else:
            logging.error('adb could not be found in any of the paths {}'.format(environment.paths()))

    @staticmethod
    def shell_input(path, command):
        shellx = Popen(
            shlex.split("{} shell input {}".format(path, command)),
            stdout=PIPE,
            stderr=PIPE,
        )

    @staticmethod
    def get_dimensions(path):
        shellx = Popen(
            shlex.split("{} shell wm size".format(path)),
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
            logging.error("AndroidDeviceError: adb shell wm size did not return 'Physical Size' or 'Override Size'")
            return False

    @staticmethod
    def shell(path, command):
        shellx = Popen(
            shlex.split("{} shell {}".format(path, command)),
            stdout=PIPE,
            stderr=PIPE,
        )
        return True

    @staticmethod
    def devices(increment=''):
        proc = Popen(shlex.split(increment + " devices"), stdout=PIPE)
        output = decode_process(proc)[1].split('\t')
        logging.debug("ADB: {}".format(output))
        return output

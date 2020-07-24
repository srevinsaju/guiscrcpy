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

import argparse
import json
import os
import sys
import time
import uuid

from qtpy import QtWidgets
from qtpy.QtCore import QThread

from pynput import keyboard

from guiscrcpy.lib.check import adb
from guiscrcpy.lib.config import InterfaceConfig
from guiscrcpy.lib.mapper.ux import MapperUI

get1 = False
fixed_pos = [0.0, 0.0]
final_pos = [0.0, 0.0]

cfgmgr = InterfaceConfig()
config = cfgmgr.get_config()
adb.path = config['adb']

json_file = 'guiscrcpy.mapper.json'

print("+++++++++++++++++++++++++++++++++++++++")
print("guiscrcpy ~ mapper by srevinsaju")
print("=======================================")
print("Make sure that your device is turned on, and connected to your PC")
print('With USB debugging turned on.')
print("+++++++++++++++++++++++++++++++++++++++")
print("Waiting for device")
adb.command(adb.path, 'wait-for-any-device')
print("Device : OK!\n")

cfgpath = cfgmgr.cfgpath


class Mapper:
    def __init__(self, device_id):
        self.config = dict()
        self._device_id = device_id
        self.app = None
        self.window = None
        self.dimensions = adb.get_dimensions(adb.path, device_id)

    def set_device_id(self, device_id):
        """
        sets the internal device id to the :param
        :param device_id:
        :type device_id:
        :return:
        :rtype:
        """
        self._device_id = device_id

    def get_device_id(self):
        return self._device_id

    def get_screenshot(self):
        """
        Gets the screenshot using `adb screncap` command
        :return:
        :rtype:
        """
        print("Make sure your phone display is switched on.")
        uid = uuid.uuid4().hex  # generate a random seed
        print("Generating Screenshot: {}".format(uid))

        # capture screenshot using `adb screencap`
        print("Please wait. A full definition screenshot is being captured")

        adb_screencap_process = adb.command(
            adb.path, 'shell screencap -p /sdcard/{uid}.png'.format(
                uid=uid
            ),
            device_id=self._device_id
        )
        adb_screencap_process_ecode = adb_screencap_process.wait(500)
        if adb_screencap_process_ecode != 0:
            print("Screenshot failed. Exiting")
            print(adb_screencap_process.stdout.read().decode('utf-8'))
            return
        # sleep for two seconds so that the image is processed
        time.sleep(2)

        # pull screenshot from android using `adb pull`
        adb_pull_process = adb.command(
            adb.path, 'pull /sdcard/{uid}.png {dest}'.format(
                uid=uid,
                dest=cfgpath
            ),
            device_id=self._device_id
        )
        adb_pull_process_ecode = adb_pull_process.wait(500)

        if adb_pull_process_ecode != 0:
            print("Screenshot pull failed. Exiting")
            print(adb_pull_process.stdout.read().decode('utf-8'))
            return

        # sleep for 1 second to get capture time
        time.sleep(1)

        # remove data from user sdcard
        adb.command(
            adb.path, "shell rm /sdcard/{uid}.png".format(uid=uid),
            device_id=self._device_id
        )
        print("[LOG] Screenshot captured. "
              "Saved to {cfgpath}".format(cfgpath=cfgpath))
        return os.path.join(cfgpath, '{uid}.png'.format(uid=uid))

    # The following functions handle key events on the mapper
    def on_key_press(self, key):
        try:
            if key.char in self.config.keys():
                print("[KEY] Hotkey command eecuting")
                position_to_tap = self.config.get(key.char)
                c = adb.command(
                    adb.path,
                    'shell input tap {} {}'.format(*position_to_tap),
                    device_id=self.get_device_id()
                )
                print(c.stdout.read().decode('utf-8'))
                print("[KEY][COMPLETE]")

        except AttributeError as e:
            print("E: {}".format(e))

    def listen_keypress(self):
        """
        Listens to keypress using pynput and executes self.on_key_press
        on every keydown
        :return:
        :rtype:
        """
        print(
            "[SERVER] LISTENING VALUES:"
            "Your keys are being listened by server. "
        )
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()

    # configuration
    def read_configuration(self):
        guiscrcpy_mapper_json = os.path.join(cfgpath, 'guiscrcpy.mapper.json')
        if not os.path.exists(guiscrcpy_mapper_json):
            self.create_configuration()
        with open(guiscrcpy_mapper_json, 'r', encoding='utf-8') as f:
            self.config.update(json.load(f))

    def create_configuration(self):
        guiscrcpy_mapper_json = os.path.join(cfgpath, 'guiscrcpy.mapper.json')
        with open(guiscrcpy_mapper_json, 'w') as w:
            json.dump(self.config, w)
        print("Wrote configuration file.")

    def add_position(self, char, position):
        self.config[char] = position

    # initialize
    def initialize(self, initialize_qt=False):
        """
        Initializes GUI to set keys to mapper
        :return:
        :rtype:
        """
        print("Setting up guiscrcpy-mapper for the first time use...")
        print("Intializing GUI window")
        print(__name__ == "__main__")
        if __name__ == '__main__' or initialize_qt:
            print("Creating QtCore window Application instance")
            self.app = QtWidgets.QApplication(sys.argv)
        self.window = MapperUI(
            self,
            self.get_screenshot(),
            self.dimensions,
            fixed_pos=fixed_pos,
            final_pos=final_pos
        )
        input()
        # Mapper process ended
        print("Registration process completed.")
        print("Registered mappings are : ", self.config)
        print("Writing configuration file...")
        self.create_configuration()


class MapperAsync(QThread):
    def __init__(self, parent, device_id, initialize=True):
        QThread.__init__(self, parent)
        self.parent = parent
        self.device_id = device_id
        self.initialize = initialize

    def run(self):
        mp = Mapper(self.device_id)
        if self.initialize:
            mp.initialize(initialize_qt=False)
        else:
            mp.read_configuration()
            mp.listen_keypress()


def command_line_argument_parse():
    """
    Creates an ArgumentParser object and returns a named tuple
    generated by the parser.parse_args()
    :return:
    :rtype:
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--mapper', action="store_true",
        help="Start the mapper"
    )
    parser.add_argument(
        '--mapper-delay', default=10,
        help="Set time to delay before screen is captured"
    )
    parser.add_argument(
        '--mapper-reset', action="store_true",
        help="Remove mapper configuration file and stat from scratch"
    )
    parser.add_argument(
        '--mapper-device-id', default='',
        help="Sets the device-id for mapper to configure "
             "(optional, needed for multiple devices)"
    )
    return parser.parse_args()


def main():
    """
    Main function only executed if __name__ == __main__
    :return:
    :rtype:
    """
    args = command_line_argument_parse()
    if args.mapper_device_id:
        mapper_device_id = args.mapper_device_id
    else:
        mapper_device_id = None

    # get the adb shell dimensions using wmctrl
    adb.get_dimensions(adb.path, device_id=mapper_device_id)

    # delay for 5 seconds by default or respect command line arguments
    delay = args.mapper_delay
    time.sleep(delay)


if __name__ == "__main__":
    main()

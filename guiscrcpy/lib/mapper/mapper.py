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

import json
import os
import time
import uuid
import subprocess

from qtpy import QtWidgets
from qtpy.QtCore import QThread

from pynput import keyboard

from guiscrcpy.lib.bridge.exceptions import AdbRuntimeError
from guiscrcpy.lib.mapper.ux import MapperUI

fixed_pos = [0.0, 0.0]
final_pos = [0.0, 0.0]

json_file = "guiscrcpy.mapper.json"


def log(category, message):
    print("[{}]".format(str(category).upper()), message)


class Mapper:
    def __init__(self, device_id, adb, config_path=None):
        self.config = dict()
        self._device_id = device_id
        self.app = None
        self.adb = adb
        log("mapper", "Waiting for device...")
        self.adb.command("wait-for-any-device")
        log("mapper", "Device connection established...")
        self.window = None
        self.guiscrcpy_mapper_json = config_path
        self.dimensions = adb.get_dimensions(device_id)
        log("mapper", "Checking device orientation")
        if self.check_orientation() == 1:
            # reverse the detected dimensions.
            # possibly the device is landscape / not the default
            # orientation as detected by Android Window Manager
            self.dimensions = self.dimensions[::-1]

    def check_orientation(self):
        proc = self.adb.shell("dumpsys input")
        try:
            e_code = proc.wait(5)
        except subprocess.TimeoutExpired:
            e_code = 0
            log(
                "mapper",
                "Failed to detect orientation instantly. Expect"
                "invalid orientations.",
            )
        if e_code != 0:
            # process failed
            raise AdbRuntimeError(
                "adb failed with {ecode} when trying to "
                "execute command "
                "`adb shell dumpsys input`".format(ecode=e_code)
            )
        out, err = proc.communicate()
        out, err = out.decode(), err.decode()
        if "SurfaceOrientation" in out:
            # SurfaceOrientation gives the idea if the device is
            # landscape or portait. SurfaceOrientation: 1 mentions that
            # the mobile is oriented in the landscape orientation
            # SugrfaceOrientation: 0 indicates, default
            print("Detected SurfaceOrientation, processing...")
            if "SurfaceOrientation: 0" in out:
                print("Detected Portait orientation...")
                return 0
            elif "SurfaceOrientation: 1" in out:
                print("Detected Landscape orientation...")
                return 1
            else:
                print("Failed to detect orientation from device. " "Fallback to 0")
                return 0
        else:
            print(
                "Failed to detect Orientation. SurfaceOrientation" " key was not found"
            )
            return 0

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

        adb_screencap_process = self.adb.command(
            "shell screencap -p /sdcard/{uid}.png".format(uid=uid),
            device_id=self._device_id,
        )
        adb_screencap_process_ecode = adb_screencap_process.wait(500)
        if adb_screencap_process_ecode != 0:
            print("Screenshot failed. Exiting")
            print(adb_screencap_process.stdout.read().decode("utf-8"))
            return
        # sleep for two seconds so that the image is processed
        time.sleep(2)

        # pull screenshot from android using `adb pull`
        adb_pull_process = self.adb.command(
            "pull /sdcard/{uid}.png {dest}".format(
                uid=uid, dest=os.path.dirname(self.guiscrcpy_mapper_json)
            ),
            device_id=self._device_id,
        )
        adb_pull_process_ecode = adb_pull_process.wait(500)

        if adb_pull_process_ecode != 0:
            print("Screenshot pull failed. Exiting")
            print(adb_pull_process.stdout.read().decode("utf-8"))
            return

        # sleep for 1 second to get capture time
        time.sleep(1)

        # remove data from user sdcard
        self.adb.command(
            "shell rm /sdcard/{uid}.png".format(uid=uid), device_id=self._device_id
        )
        print(
            "[LOG] Screenshot captured. Saved to {cfgpath}".format(
                cfgpath=os.path.dirname(self.guiscrcpy_mapper_json)
            )
        )
        return os.path.join(
            os.path.dirname(self.guiscrcpy_mapper_json), "{uid}.png".format(uid=uid)
        )

    # The following functions handle key events on the mapper
    def on_key_press(self, key):
        try:
            if key.char in self.config.keys():
                print("[KEY] Hotkey command executing")
                position_to_tap = self.config.get(key.char)
                c = self.adb.command(
                    "shell input tap {} {}".format(*position_to_tap),
                    device_id=self.get_device_id(),
                )
                print(c.stdout.read().decode("utf-8"))
                print("[KEY][COMPLETE]")

        except AttributeError:
            if key == keyboard.Key.shift:
                print("[KEY][MOD] Shift key")
            elif key == keyboard.Key.esc:
                print("[KEY][ESC] Aborting")
                return False
            else:
                print("[KEY][MOD] Special key {}".format(key))

    def listen_keypress(self):
        """
        Listens to keypress using pynput and executes self.on_key_press
        on every keydown
        :return:
        :rtype:
        """
        print("[SERVER] LISTENING VALUES:" "Your keys are being listened by server. ")
        try:
            with keyboard.Listener(on_press=self.on_key_press) as listener:
                listener.join()
        except KeyboardInterrupt:
            print("guiscrcpy-mapper aborted on user request")

    # configuration
    def read_configuration(self):
        if not os.path.exists(self.guiscrcpy_mapper_json):
            self.create_configuration()
        with open(self.guiscrcpy_mapper_json, "r", encoding="utf-8") as f:
            self.config.update(json.load(f))

    def create_configuration(self):
        with open(self.guiscrcpy_mapper_json, "w") as w:
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
        if __name__ == "__main__" or initialize_qt:
            print("Creating QtCore window Application instance")
            self.app = QtWidgets.QApplication([])
        self.window = MapperUI(
            self,
            self.get_screenshot(),
            self.dimensions,
            fixed_pos=fixed_pos,
            final_pos=final_pos,
        )
        self.app.processEvents()
        self.app.exec_()


class MapperAsync(QThread):
    def __init__(self, parent, device_id, adb, initialize=True, config_path=None):
        QThread.__init__(self, parent)
        self.parent = parent
        self.adb = adb
        self.device_id = device_id
        self.initialize = initialize
        self._config_path = config_path

    def run(self):
        mp = Mapper(self.device_id, adb=self.adb, config_path=self._config_path)
        if self.initialize:
            mp.initialize(initialize_qt=False)
        else:
            mp.read_configuration()
            mp.listen_keypress()

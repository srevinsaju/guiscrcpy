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
import os

from guiscrcpy.lib.check import adb

try:
    import pyautogui as auto
    from pygetwindow import getWindowsWithTitle
except Exception as e:
    logging.debug("pygetwindow, pyautogui failed with error code {}".format(e))
    auto = None
    getWindowsWithTitle = None


class UXMapper:
    def __init__(self):
        logging.debug("Launching UX Mapper")
        self.has_modules = getWindowsWithTitle and auto
        logging.debug("Calculating Screen Size")
        self.android_dimensions = adb.get_dimensions(adb.path)

    def do_swipe(self, x1=10, y1=10, x2=10, y2=10):
        adb.shell_input(adb.path, "swipe {} {} {} {}".format(x1, y1, x2, y2))
        return True

    def do_keyevent(self, key):
        adb.shell_input(adb.path, "keyevent {}".format(key))
        return True

    def copy_devpc(self):
        if self.has_modules:
            scrcpywindow = getWindowsWithTitle("scrcpy")[0]
            scrcpywindow.focus()
            auto.hotkey("ctrl", "c")
        else:
            os.system(
                "wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+c")

    def key_power(self):
        logging.debug("Passing POWER")
        self.do_keyevent(26)

    def key_menu(self):
        logging.debug("Passing MENU")
        self.do_keyevent(82)

    def key_back(self):
        logging.debug("Passing BACK")
        self.do_keyevent(4)

    def key_volume_up(self):
        logging.debug("Passing BACK")
        self.do_keyevent(24)

    def key_volume_down(self):
        logging.debug("Passing BACK")
        self.do_keyevent(25)

    def key_home(self):
        logging.debug("Passing HOME")
        self.do_keyevent(3)

    def key_switch(self):
        logging.debug("Passing APP_SWITCH")
        self.do_keyevent("KEYCODE_APP_SWITCH")

    def reorientP(self):
        logging.debug("Passing REORIENT [POTRAIT]")
        adb.shell(adb.path, 'settings put system accelerometer_rotation 0')
        adb.shell(adb.path, "settings put system rotation 1")

    def reorientL(self):
        logging.debug("Passing REORIENT [LANDSCAPE]")
        adb.shell(adb.path, 'settings put system accelerometer_rotation 0')
        adb.shell(adb.path, "settings put system rotation 1")

    def expand_notifications(self):
        logging.debug("Passing NOTIF EXPAND")
        self.do_swipe(0, 0, 0, int(self.android_dimensions[1]) - 1)

    def collapse_notifications(self):
        logging.debug("Passing NOTIF COLLAPSE")
        self.do_swipe(0, int(self.android_dimensions[1]) - 1, 0, 0)

    def copy_pc2dev(self):
        if self.has_modules:
            scrcpywindow = getWindowsWithTitle("scrcpy")[0]
            scrcpywindow.focus()
            auto.hotkey("ctrl", "shift", "c")
            logging.warning(" NOT SUPPORTED ON WINDOWS")
        else:
            os.system(
                "wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+shift+c")

    def fullscreen(self):
        if self.has_modules:
            scrcpywindow = getWindowsWithTitle("scrcpy")[0]
            scrcpywindow.focus()
            auto.hotkey("ctrl", "f")
        else:
            os.system(
                "wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+f")

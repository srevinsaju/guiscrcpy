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

from guiscrcpy.platform.windows_tools.tools import make_shortcut


class Windows:
    def __init__(self):
        self.make_config()

    @staticmethod
    def make_config():
        path = os.path.expanduser(os.path.join("~", "AppData", "Local", "guiscrcpy"))
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                logging.error(
                    "Error creating configuration filename in dir {path}. "
                    "Error code:{e}".format(path=path, e=e)
                )
        return path

    @staticmethod
    def system():
        return "Windows"

    def cfgpath(self):
        return self.make_config()

    def increment(self):
        pass

    @staticmethod
    def paths():
        return ["bin"]

    @staticmethod
    def install_fonts():
        return True

    @staticmethod
    def create_desktop():
        try:
            make_shortcut()
        except Exception as e:
            # do not stop users from using guiscrcpy
            # in case this small exception happens
            print("Desktop shortcut generation failed: {}".format(e))

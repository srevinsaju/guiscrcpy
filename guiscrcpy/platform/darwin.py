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


class Darwin:
    def __init__(self):
        logging.error(
            "MacOS is untested. " "guiscrcpy is trying to use Linux config on Mac"
        )

    def cfgpath(self):
        return self.make_config()

    @staticmethod
    def make_config():
        if os.getenv("XDG_CONFIG_HOME") is None:
            path = os.path.expanduser("~/.config/guiscrcpy/")
        else:
            path = os.getenv("XDG_CONFIG_HOME").split(":")[0] + "/guiscrcpy"
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
        return "Darwin"

    def increment(self):
        pass

    @staticmethod
    def paths():
        return ["bin", "/usr/bin", "~/.local/bin", "~/bin", "/usr/local/bin"]

    @staticmethod
    def install_fonts():
        return True

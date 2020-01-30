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


class Windows:
    def __init__(self):
        self.make_config()
        self._cfgpath = self.cfgpath()

    @staticmethod
    def make_config():
        path = os.path.expanduser(os.path.join("~", "AppData", "Local", "guiscrcpy"))
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                return True
            except Exception as e:
                logging.error(
                    "Error creating configuration file in dir {path}. Error code:{e}"
                    .format(
                        path=path,
                        e=e
                    ))
        return path

    def system(self):
        return 'Windows'

    def cfgpath(self):
        return self.make_config()

    def increment(self):
        pass

    def paths(self):
        return ['bin']
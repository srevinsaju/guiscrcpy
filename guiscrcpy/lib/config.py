"""
guiscrcpy
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
import shutil
from guiscrcpy.platform import platform


class InvalidConfigurationError(RuntimeError):
    pass


class InterfaceConfig:
    def __init__(self, load=True):
        """
        Manages guiscrcpy's configuration files
        """
        self.os = platform.System()
        self.cfgpath = self.os.cfgpath()
        self.paths = self.os.paths()
        self.config = {
            "version": 1,
            "paths": self.paths,
            "scrcpy": None,
            "adb": None,
            "panels": {"swipe": True, "bottom": True, "toolkit": True},
            "mapper": "",
            "sha_shift": 5,
            "scrcpy-server": None,
            "dimension": None,
            "swtouches": False,
            "bitrate": 8000,
            "fullscreen": False,
            "dispRO": False,
            "extra": "",
            "cmx": "",
            "device": {},
            "theme": "Breeze",
        }
        self.json_file = "guiscrcpy.json"
        if load:
            self.load_config()

    def load_config(self):
        self.check_file()
        self.validate()

    def validate(self):
        # check scrcpy and adb are not None, else replace it with original
        # values
        if os.getenv("APPIMAGE") is not None:
            # no need further configuration for adb, scrcpy and scrcpy_server
            self.config["adb"] = os.getenv("GUISCRCPY_ADB")
            self.config["scrcpy"] = os.getenv("GUISCRCPY_SCRCPY")
            return True
        if self.config["adb"] is None:
            adb_path = shutil.which("adb")
            self.config["adb"] = adb_path
        else:
            _adb_path = self.config["adb"]
            if not os.path.exists(_adb_path):
                raise InvalidConfigurationError(
                    "The configuration key 'adb' is "
                    "invalid. {} does not exist. "
                    "If you did not set it on purpose, "
                    "run `guiscrcpy config -r` to reset "
                    "the configuration".format(self.config["adb"])
                )
        if self.config["scrcpy"] is None:
            scrcpy_path = shutil.which("scrcpy")
            self.config["scrcpy"] = scrcpy_path
        else:
            _scrcpy_path = self.config["scrcpy"]
            if not os.path.exists(_scrcpy_path):
                raise InvalidConfigurationError(
                    "The configuration key 'scrcpy' is "
                    "invalid. {} does not exist. "
                    "If you did not set it on purpose, "
                    "run `guiscrcpy config -r` to reset "
                    "the configuration".format(self.config["scrcpy"])
                )
        if (self.config["scrcpy-server"] is not None) and (
            platform.System() == "Windows"
        ):
            os.environ["SCRCPY_SERVER_PATH"] = self.config["scrcpy-server"]
        return True

    def __setitem__(self, key, value):
        self.config[key] = value
        self.write_file()

    def __getitem__(self, item):
        return self.config.get(item)

    def get_config(self):
        return self.config

    def get_scrcpy(self):
        if self.config["scrcpy"] is not None:
            return self.config["scrcpy"]
        else:
            return None

    def get_adb(self):
        if self.config["adb"] is not None:
            return self.config["adb"]
        else:
            return None

    def get_cfgpath(self):
        return self.cfgpath

    def read_file(self):
        with open(os.path.join(self.cfgpath, self.json_file), "r") as f:
            config = json.load(f)
        self.update_config(config)

    def write_file(self):
        with open(os.path.join(self.cfgpath, self.json_file), "w") as f:
            json.dump(self.config, f, indent=4, sort_keys=True)

    def check_file(self):

        if not os.path.exists(self.cfgpath):
            os.makedirs(self.cfgpath)
        if not os.path.exists(os.path.join(self.cfgpath, self.json_file)):
            self.write_file()
        self.read_file()

    def update_config(self, new_conf):
        for i in new_conf:
            for j in self.config:
                if i == j:
                    self.config[i] = new_conf[i]

    def reset_config(self):
        os.remove(os.path.join(self.get_cfgpath(), self.json_file))
        return True

    def __repr__(self):
        return 'GuiscrcpyConfig({}, "{}")'.format(
            json.dumps(self.config, indent=4), self.cfgpath
        )

import logging
import os


class Linux:
    def __init__(self):
        pass

    def cfgpath(self):
        return self.make_config()

    @staticmethod
    def make_config():
        if os.getenv('XDG_CONFIG_HOME') is None:
            path = os.path.expanduser("~/.config/guiscrcpy/")
        else:
            path = os.getenv('XDG_CONFIG_HOME').split(":")[0] + "/guiscrcpy"
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
        return 'Linux'

    def increment(self):
        pass

    def paths(self):
        return ['bin', '/usr/bin', '~/.local/bin', '~/bin', '/usr/local/bin']

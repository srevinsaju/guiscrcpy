import logging
import os


class Windows:
    def __init__(self):
        self.make_config()
        self._cfgpath = self.cfgpath()

    @staticmethod
    def make_config():
        path = os.path.expanduser("~/AppData/Local/guiscrcpy/")
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
        return os.path.expanduser("~/AppData/Local/guiscrcpy/")

    def increment(self):
        pass

    def paths(self):
        return ['bin']
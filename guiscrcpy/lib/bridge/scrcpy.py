import os
from subprocess import PIPE

from .base import Bridge
from ...lib.utils import shellify as _, open_process


class ScrcpyBridge(Bridge):
    name = "scrcpy"

    def post_init(self):
        if os.getenv("SCRCPY_LDD"):
            if os.getenv("LD_LIBRARY_PATH"):
                os.environ["LD_LIBRARY_PATH"] += os.getenv("SCRCPY_LDD")
            else:
                os.environ["LD_LIBRARY_PATH"] = os.getenv("SCRCPY_LDD")

    def start(self, args, stdout=PIPE, stderr=PIPE):
        proc = open_process(
            _("{} {}".format(self.path, args)),
            stdout=stdout,
            stderr=stderr,
        )
        return proc

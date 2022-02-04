import sys
import subprocess


from .base import AudioBridge
from ...utils import open_process


class USBAudioBridge(AudioBridge):
    name = "usbaudio"

    def run(self, device_id=None):
        if device_id is None:
            command = [self.get_path()]
        else:
            command = [self.get_path(), "--serial", device_id]
        open_process(
            command,
            stdout=sys.stdout,
            stderr=sys.stderr,
        )

import sys
import subprocess
import time

from .base import AudioBridge
from ...utils import shellify as _, show_message_box, open_process


class SndcpyBridge(AudioBridge):
    name = "sndcpy"

    def run(self, device_id=None):
        if device_id is None:
            command = "{sndcpy}"
        else:
            command = "{sndcpy} {device_id}"
        _proc = open_process(
            _(command.format(sndcpy=self.get_path(), device_id=device_id)),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        waiting_since = 0
        while True:
            if waiting_since > 30:
                # we should stop now
                _out = show_message_box(
                    text="sndcpy Failed to connect",
                    info_text="We couldn't establish a proper connection "
                    "to your device. Check if sndcpy is given stream permissions. "
                    "See https://github.com/rom1v/sndcpy for more information.",
                )
                _out.exec_()
            line = _proc.stdout.readline()
            if not line:
                break
            if "Press Enter" in line.decode():
                _out = show_message_box(
                    text="Sndcpy",
                    info_text="Click Accept on your Android device, and then click 'ok'",
                )
                _out.exec_()
                _proc.stdin.write(b"\n\r\n\r")
                _proc.stdin.close()
                break
            time.sleep(0.1)
            waiting_since += 0.1

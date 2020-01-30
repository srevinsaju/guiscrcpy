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
import platform
import time
import pystray
from subprocess import Popen, PIPE
from PIL import Image, ImageDraw

from guiscrcpy.lib.check import adb

logging.warning("Launching notification auditor")


class NotifyAuditor:
    def __init__(self):
        image = Image.new("RGBA", (128, 128), (255, 255, 255, 255))
        icon = pystray.Icon("Test Icon 1", image)
        icon.visible = True
        icon.run(setup=self.callback)

    def callback(self, icon):
        notif = Popen(
            adb.path +
            "adb shell dumpsys notification | grep ticker | cut -d= -f2",
            stdout=PIPE,
            shell=True,
        )
        image = Image.new("RGBA", (128, 128), (255, 255, 255, 255))
        # loop this block --->
        var1 = notif.stdout.readlines()
        var2 = var1
        while True:
            if platform.system() == "Windows":
                logging.warning(
                    "Notif Auditor is experimental on Windows. If you wish to help out on this issue. Open a PR on github"
                )
                notif = Popen(
                    adb.path +
                    "adb shell dumpsys notification | findstr ticker ",
                    stdout=PIPE,
                    shell=True,
                )
            else:
                "Notif Auditor is experimental on Linux. If you wish to help out on this issue. Open a PR on github"
                notif = Popen(
                    adb.path +
                    "adb shell dumpsys notification | grep ticker | cut -d= -f2",
                    stdout=PIPE,
                    shell=True,
                )
            image = Image.new(
                "RGBA", (128, 128), (255, 255, 255, 255))
            # loop this block --->
            var1 = notif.stdout.readlines()

            # <----
            if len(var1) > len(var2):
                d = ImageDraw.Draw(image)
                d.rectangle([0, 255, 128, 128], fill="green")
                icon.icon = image
                time.sleep(600)
                var2 = var1

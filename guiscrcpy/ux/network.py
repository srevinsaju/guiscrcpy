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

import time

from qtpy.QtWidgets import QMainWindow

from ..network.network import NetworkManager
from ..platform.platform import System
from . import Ui_NetworkUI


class InterfaceNetwork(QMainWindow, Ui_NetworkUI):
    """
    Network manager UI UX Kit for guiscrcpy
    Scans the open IP Addresses connected on the system,
    on Linux and Mac only, as far as tested
    Does not work satisfactorily on Windows.
    """

    def __init__(self, adb):
        QMainWindow.__init__(self)
        Ui_NetworkUI.__init__(self)
        self.os = System()
        self.setupUi(self)
        self.adb = adb
        self.nm = NetworkManager()

    def init(self):
        """
        Connect buttons to sig
        :return:
        """
        self.nm_connect.pressed.connect(self.connect)
        if self.os.system() == "Windows":
            # FIXME: Port scanning is not working on Windows at the moment.
            self.nm_det.setText(
                "Enter the IP address in the text box and press connect"
            )
            self.nm_refresh.setEnabled(False)
        else:
            self.nm_refresh.pressed.connect(self.refresh)
            self.nm_det.setText("Click Refresh to load IP addresses")
        self.tcpip.pressed.connect(self.tcpip_launch)

    def tcpip_launch(self):
        self.adb.command("-d tcpip 5555")
        self.nm_det.setText(
            "Now disconnect your device, and enter the IP address, and connect"
        )
        return

    def connect(self):
        try:
            ip = self.listView.currentItem().text()
        except AttributeError:
            # The IP Address in the ListView has precedence over the IP address
            # in the text box
            if (
                not self.lineEdit.text().strip().isspace()
                or len(self.lineEdit.text().strip()) != 0
            ):
                if ":" in self.lineEdit.text():
                    self.nm_det.setText(
                        "Please provide the port in the " "'port' text box"
                    )
                    return
                if self.lineEdit.text().count(".") == 3:
                    ip = self.lineEdit.text().strip().lower()
                else:
                    self.nm_det.setText("Invalid IP address in text box")
                    return
            else:
                if self.os.system() == "Windows":
                    self.nm_det.setText("Please enter an IP address in the text box")
                else:
                    self.nm_det.setText(
                        "Please enter an IP address in the text box. / " "Click refresh"
                    )
                return

        sp = self.adb.command("connect {}:5555".format(ip))
        count = 0
        while True:
            count += 1
            readout = sp.stdout.readline().decode()
            if "failed" in readout:
                self.nm_det.setText(
                    "Device failed to get connected (is it an Android dev?"
                )
                return
            if "connected" in readout:
                print(readout)
                break
            if count > 30:
                self.nm_det.setText("Device connect failed: Timeout")
            else:
                time.sleep(1)
        self.nm_det.setText("Connected to IP:{}:{}".format(ip, self.spinBox.value()))

    def refresh(self):
        self.listView.clear()
        nm_map_network_devices = self.nm.map_network()
        print("Detected IP Addresses:", nm_map_network_devices)
        self.listView.addItems(nm_map_network_devices)

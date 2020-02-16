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

import sys

from PyQt5.QtWidgets import QMainWindow

from guiscrcpy.network.network import NetworkManager
from guiscrcpy.ui.network import Ui_NetworkUI


class InterfaceNetwork(QMainWindow, Ui_NetworkUI):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_NetworkUI.__init__(self)
        self.setupUi(self)
        self.nm = NetworkManager()

    def init(self):
        self.nm_connect.pressed.connect(self.connect)
        self.nm_refresh.pressed.connect(self.refresh)
        self.nm_det.setText("Click Refresh to load IP addresses")

    def connect(self):
        print(self.listView.currentItem().text())


    def refresh(self):
        self.listView.clear()
        self.listView.addItems(self.nm.map_network())

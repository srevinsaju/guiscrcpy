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

from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow

from guiscrcpy.lib.toolkit import UXMapper
from guiscrcpy.ui.panel import Ui_HorizontalPanel


class Panel(QMainWindow, Ui_HorizontalPanel):
    # there was a Dialog in the bracket
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_HorizontalPanel.__init__(self)
        self.setupUi(self)
        self.oldpos = self.pos()
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )

    def init(self):
        self.ux = UXMapper()
        self.backk.clicked.connect(self.ux.key_back)
        self.menuUII.clicked.connect(self.ux.key_menu)
        self.homee.clicked.connect(self.ux.key_home)
        self.powerUII.clicked.connect(self.ux.key_power)
        self.vupp.clicked.connect(self.ux.key_volume_up)
        self.vdownn.clicked.connect(self.ux.key_volume_down)
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)

            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except (TypeError, AttributeError):
            pass

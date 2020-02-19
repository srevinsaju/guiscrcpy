
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

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow

from guiscrcpy.lib.toolkit import UXMapper


class SwipeUX(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super(SwipeUX, self).__init__()
        self.oldPos = None
        self.ux = None
        self.setObjectName("SwipeUX")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.resize(70, 70)
        # -----------------------
        # =====================
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "QWidget{background-color: rgba(0,0,0,0);}\nQPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.495098, fy:0.5, stop:0.887255 rgba(35, 35, 35, 255), stop:0.901961 rgba(0, 0, 0, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "\n"
            "}\\n\n"
            "QPushButton:pressed {\n"
            "border-radius: 15px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "   }\n"
            "QMainWindow{background-color: rgba(0,0,0,30);}\n"
            "QPushButton:hover {\n"
            "border-radius: 15px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.swirt = QtWidgets.QPushButton(self.centralwidget)
        self.swirt.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.swirt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-right.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swirt.setIcon(icon1)
        self.swirt.setObjectName("swirt")
        self.swilf = QtWidgets.QPushButton(self.centralwidget)
        self.swilf.setGeometry(QtCore.QRect(0, 20, 30, 30))
        self.swilf.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swilf.setIcon(icon2)
        self.swilf.setObjectName("swilf")
        self.swidn = QtWidgets.QPushButton(self.centralwidget)
        self.swidn.setGeometry(QtCore.QRect(20, 40, 30, 30))
        self.swidn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-down.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swidn.setIcon(icon3)
        self.swidn.setObjectName("swidn")
        self.swiup = QtWidgets.QPushButton(self.centralwidget)
        self.swiup.setGeometry(QtCore.QRect(20, 0, 30, 30))
        self.swiup.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-up.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swiup.setIcon(icon4)
        self.swiup.setObjectName("swiup")
        self.setCentralWidget(self.centralwidget)
        # -----------------
        # ================

        self.oldpos = self.pos()
        self.swiup.pressed.connect(self.swipup)
        self.swidn.pressed.connect(self.swipdn)
        self.swilf.pressed.connect(self.swipleft)
        self.swirt.pressed.connect(self.swipright)

    def init(self):
        self.ux = UXMapper()
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        qp.setBrush(QtGui.QColor(0, 0, 0, 127))
        qp.drawEllipse(0, 0, 70, 70)
        qp.end()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)

            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except (TypeError, AttributeError):
            pass

    def swipdn(self):
        logging.debug("Passing SWIPE DOWN")
        dimValues = self.ux.android_dimensions
        posy = int(dimValues[1]) - 200
        posx = int(dimValues[0])
        newposx = posx / 2  # find center
        self.ux.do_swipe(newposx, 200, newposx, posy)

    def swipup(self):
        logging.debug("Passing SWIPE UP")
        dimValues = self.ux.android_dimensions
        posy = int(dimValues[1]) - 100
        posx = int(dimValues[0])
        newposx = int(posx / 2)  # find center
        self.ux.do_swipe(newposx, posy, newposx, 200)

    def swipleft(self):
        logging.debug("Passing SWIPE LEFT")
        dimValues = self.ux.android_dimensions
        posy = int(dimValues[1])
        posx = int(dimValues[0]) - 10
        newposy = int(posy / 2)  # find center
        self.ux.do_swipe(10, newposy, posx, newposy)

    def swipright(self):
        logging.debug("Passing SWIPE RIGHT")
        dimValues = self.ux.android_dimensions
        posy = int(dimValues[1])
        posx = int(dimValues[0]) - 10
        newposy = int(posy / 2)  # find center
        self.ux.do_swipe(posx, newposy, 10, newposy)

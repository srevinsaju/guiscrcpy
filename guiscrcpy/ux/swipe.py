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
import uuid

from qtpy import QtGui, QtWidgets, QtCore
from qtpy.QtCore import Qt, QPoint
from qtpy.QtWidgets import QMainWindow

from guiscrcpy.lib.toolkit import UXMapper


class SwipeUX(QMainWindow):
    def __init__(self, ux_wrapper=None, frame=False, always_on_top=True):
        """
        Swipe UI
        :param ux_wrapper: UXMapper type object
        :param frame: bool
        :param always_on_top: bool
        """
        QMainWindow.__init__(self)
        self.oldPos = None
        self.name = "swipe"
        self.uid = uuid.uuid4()

        # =================
        if ux_wrapper:
            self.ux = ux_wrapper
        else:
            self.ux = UXMapper()
        hexdigest = self.ux.get_sha()[:6]

        self.setObjectName("SwipeUX")
        __flags = QtCore.Qt.Window
        if not frame:
            __flags |= QtCore.Qt.FramelessWindowHint
            self.setAttribute(Qt.WA_NoSystemBackground, True)
            self.setAttribute(Qt.WA_TranslucentBackground, True)
        if always_on_top:
            __flags |= QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(__flags)

        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint
        # QtCore.Qt.FramelessWindowHint)
        self.resize(70, 70)
        # -----------------------

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "QWidget {"
            "background-color: rgba(0,0,0,0);}\nQPushButton {\n"
            "border-radius: 15px;\n"
            "background-color: qradialgradient("
            "spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.495098, fy:0.5, "
            "stop:0.887255 rgba(35, 35, 35, 255), "
            "stop:0.901961 rgba(0, 0, 0, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "}\n\n"
            "QPushButton:pressed {\n"
            "border-radius: 15px;\n"
            "\n"
            "background-color: qlineargradient("
            "spread:pad, x1:0, y1:0, x2:1, y2:1, "
            "stop:0 rgba(0, 255, 255, 255), "
            "stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "   }\n"
            "QMainWindow{background-color: rgba(0,0,0,30);}\n"
            "QPushButton:hover {\n"
            "border-radius: 15px;\n"
            "background-color: qlineargradient("
            "spread:pad, x1:0, y1:0, x2:1, y2:1, "
            "stop:0 rgba(0, 199, 199, 255), "
            "stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.lol = QtWidgets.QPushButton(self.centralwidget)
        self.lol.setGeometry(QtCore.QRect(24, 24, 25, 25))
        self.lol.setText("")
        self.lol.setObjectName("lol")
        self.lol.setStyleSheet(
            f"background-color: #{hexdigest};" f"border-radius: 12px; "
        )
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
        self.oldpos = self.pos()
        self.swiup.pressed.connect(self.swipup)
        self.swidn.pressed.connect(self.swipdn)
        self.swilf.pressed.connect(self.swipleft)
        self.swirt.pressed.connect(self.swipright)

    def init(self):
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
        dim_values = self.ux.android_dimensions
        pos_y = int(dim_values[1]) - 200
        pos_x = int(dim_values[0])
        new_pos_x = pos_x / 2  # find center
        self.ux.do_swipe(new_pos_x, 200, new_pos_x, pos_y)

    def swipup(self):
        logging.debug("Passing SWIPE UP")
        dim_values = self.ux.android_dimensions
        pos_y = int(dim_values[1]) - 100
        pos_x = int(dim_values[0])
        new_pos_x = int(pos_x / 2)  # find center
        self.ux.do_swipe(new_pos_x, pos_y, new_pos_x, 200)

    def swipleft(self):
        logging.debug("Passing SWIPE LEFT")
        dim_values = self.ux.android_dimensions
        pos_y = int(dim_values[1])
        pos_x = int(dim_values[0]) - 10
        new_pos_y = int(pos_y / 2)  # find center
        self.ux.do_swipe(10, new_pos_y, pos_x, new_pos_y)

    def swipright(self):
        logging.debug("Passing SWIPE RIGHT")
        dim_values = self.ux.android_dimensions
        pos_y = int(dim_values[1])
        pos_x = int(dim_values[0]) - 10
        new_pos_y = int(pos_y / 2)  # find center
        self.ux.do_swipe(pos_x, new_pos_y, 10, new_pos_y)

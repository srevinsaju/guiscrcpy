import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow

from guiscrcpy.lib.toolkit import UXMapper
from guiscrcpy.ui.toolkit import Ui_ToolbarPanel


class InterfaceToolkit(QMainWindow, Ui_ToolbarPanel):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_ToolbarPanel.__init__(self)
        self.setupUi(self)
        self.oldPos = None
        self.ux = None
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )

    def init(self):
        self.ux = UXMapper()
        self.clipD2PC.clicked.connect(self.ux.copy_devpc)
        self.clipPC2D.clicked.connect(self.ux.copy_pc2dev)
        self.back.clicked.connect(self.ux.key_back)
        self.screenfreeze.clicked.connect(self.quitn)
        self.appswi.clicked.connect(self.ux.key_switch)
        self.menuUI.clicked.connect(self.ux.key_menu)
        self.home.clicked.connect(self.ux.key_home)
        self.notif_pull.clicked.connect(self.ux.expand_notifications)
        self.notif_collapse.clicked.connect(self.ux.collapse_notifications)
        self.fullscreenUI.clicked.connect(self.ux.fullscreen)
        self.powerUI.clicked.connect(self.ux.key_power)
        self.vup.clicked.connect(self.ux.key_volume_up)
        self.vdown.clicked.connect(self.ux.key_volume_down)
        self.potraitUI.clicked.connect(self.ux.reorientP)
        self.landscapeUI.clicked.connect(self.ux.reorientL)
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except TypeError:
            pass

    def quitn(self):
        print("Bye Bye")
        sys.exit()

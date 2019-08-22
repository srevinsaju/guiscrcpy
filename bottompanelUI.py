# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bottompanelui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName("Panel")
        Panel.resize(312, 26)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsrc/android_circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Panel.setWindowIcon(icon)
        self.backk = QtWidgets.QPushButton(Panel)
        self.backk.setEnabled(True)
        self.backk.setGeometry(QtCore.QRect(190, 0, 81, 25))
        self.backk.setStyleSheet("background-color:rgb(171, 171, 171)")
        self.backk.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rsrc/left-arrow-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backk.setIcon(icon1)
        self.backk.setObjectName("backk")
        self.powerUII = QtWidgets.QPushButton(Panel)
        self.powerUII.setEnabled(True)
        self.powerUII.setGeometry(QtCore.QRect(40, 0, 31, 25))
        self.powerUII.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.powerUII.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("rsrc/power.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.powerUII.setIcon(icon2)
        self.powerUII.setCheckable(False)
        self.powerUII.setObjectName("powerUII")
        self.menuUII = QtWidgets.QPushButton(Panel)
        self.menuUII.setEnabled(True)
        self.menuUII.setGeometry(QtCore.QRect(70, 0, 51, 25))
        self.menuUII.setStyleSheet("background-color:rgb(171, 171, 171)")
        self.menuUII.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("rsrc/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUII.setIcon(icon3)
        self.menuUII.setObjectName("menuUII")
        self.vupp = QtWidgets.QPushButton(Panel)
        self.vupp.setEnabled(True)
        self.vupp.setGeometry(QtCore.QRect(0, 0, 31, 25))
        self.vupp.setStyleSheet("background-color:rgb(171, 171, 171)")
        self.vupp.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("rsrc/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vupp.setIcon(icon4)
        self.vupp.setObjectName("vupp")
        self.homee = QtWidgets.QPushButton(Panel)
        self.homee.setEnabled(True)
        self.homee.setGeometry(QtCore.QRect(120, 0, 71, 25))
        self.homee.setStyleSheet("background-color:rgb(171, 171, 171);\n"
"border-color: rgb(0, 0, 0);")
        self.homee.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("rsrc/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homee.setIcon(icon5)
        self.homee.setObjectName("homee")
        self.vdownn = QtWidgets.QPushButton(Panel)
        self.vdownn.setEnabled(True)
        self.vdownn.setGeometry(QtCore.QRect(280, 0, 31, 25))
        self.vdownn.setStyleSheet("background-color:rgb(171, 171, 171)")
        self.vdownn.setText("")
        self.vdownn.setIcon(icon4)
        self.vdownn.setObjectName("vdownn")

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        _translate = QtCore.QCoreApplication.translate
        Panel.setWindowTitle(_translate("Panel", "Main Panel"))
        self.backk.setToolTip(_translate("Panel", "Back key"))
        self.powerUII.setToolTip(_translate("Panel", "Power on/off"))
        self.menuUII.setToolTip(_translate("Panel", "Menu key"))
        self.vupp.setToolTip(_translate("Panel", "Volume Up"))
        self.homee.setToolTip(_translate("Panel", "Home key"))



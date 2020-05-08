# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiscrcpy/ui/bottompanelui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HorizontalPanel(object):
    def setupUi(self, HorizontalPanel):
        HorizontalPanel.setObjectName("HorizontalPanel")
        HorizontalPanel.resize(397, 24)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HorizontalPanel.setWindowIcon(icon)
        HorizontalPanel.setStyleSheet("\n"
".QPushButton {\n"
"border-radius: 1px;\n"
"color: rgb(0, 0, 0);\n"
" \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 5px;\n"
"                      \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"QPushButton:hover {\n"
"border-radius: 5px;\n"
"                      \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"")
        self.backk = QtWidgets.QPushButton(HorizontalPanel)
        self.backk.setEnabled(True)
        self.backk.setGeometry(QtCore.QRect(230, 0, 51, 25))
        self.backk.setStyleSheet("")
        self.backk.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backk.setIcon(icon1)
        self.backk.setObjectName("backk")
        self.powerUII = QtWidgets.QPushButton(HorizontalPanel)
        self.powerUII.setEnabled(True)
        self.powerUII.setGeometry(QtCore.QRect(20, 0, 81, 25))
        self.powerUII.setStyleSheet("")
        self.powerUII.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.powerUII.setIcon(icon2)
        self.powerUII.setCheckable(False)
        self.powerUII.setObjectName("powerUII")
        self.menuUII = QtWidgets.QPushButton(HorizontalPanel)
        self.menuUII.setEnabled(True)
        self.menuUII.setGeometry(QtCore.QRect(110, 0, 51, 25))
        self.menuUII.setStyleSheet("")
        self.menuUII.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/reorder-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUII.setIcon(icon3)
        self.menuUII.setObjectName("menuUII")
        self.vdownn = QtWidgets.QPushButton(HorizontalPanel)
        self.vdownn.setEnabled(True)
        self.vdownn.setGeometry(QtCore.QRect(290, 0, 31, 25))
        self.vdownn.setStyleSheet("")
        self.vdownn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/reduced-volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vdownn.setIcon(icon4)
        self.vdownn.setObjectName("vdownn")
        self.homee = QtWidgets.QPushButton(HorizontalPanel)
        self.homee.setEnabled(True)
        self.homee.setGeometry(QtCore.QRect(160, 0, 71, 25))
        self.homee.setStyleSheet("")
        self.homee.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homee.setIcon(icon5)
        self.homee.setObjectName("homee")
        self.vupp = QtWidgets.QPushButton(HorizontalPanel)
        self.vupp.setEnabled(True)
        self.vupp.setGeometry(QtCore.QRect(320, 0, 31, 25))
        self.vupp.setStyleSheet("")
        self.vupp.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vupp.setIcon(icon6)
        self.vupp.setObjectName("vupp")
        self.label = QtWidgets.QLabel(HorizontalPanel)
        self.label.setGeometry(QtCore.QRect(0, -10, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bp_close = QtWidgets.QPushButton(HorizontalPanel)
        self.bp_close.setEnabled(True)
        self.bp_close.setGeometry(QtCore.QRect(350, 0, 31, 25))
        self.bp_close.setStyleSheet("")
        self.bp_close.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/cross-mark-on-a-black-circle-background.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bp_close.setIcon(icon7)
        self.bp_close.setObjectName("bp_close")
        self.bp_device_id = QtWidgets.QPushButton(HorizontalPanel)
        self.bp_device_id.setGeometry(QtCore.QRect(380, 0, 20, 31))
        self.bp_device_id.setStyleSheet("")
        self.bp_device_id.setText("")
        self.bp_device_id.setObjectName("bp_device_id")
        self.homee.raise_()
        self.backk.raise_()
        self.powerUII.raise_()
        self.menuUII.raise_()
        self.vdownn.raise_()
        self.vupp.raise_()
        self.label.raise_()
        self.bp_close.raise_()
        self.bp_device_id.raise_()

        self.retranslateUi(HorizontalPanel)
        QtCore.QMetaObject.connectSlotsByName(HorizontalPanel)

    def retranslateUi(self, HorizontalPanel):
        _translate = QtCore.QCoreApplication.translate
        HorizontalPanel.setWindowTitle(_translate("HorizontalPanel", "guiscrcpy"))
        self.backk.setToolTip(_translate("HorizontalPanel", "Back key"))
        self.powerUII.setToolTip(_translate("HorizontalPanel", "Power on/off"))
        self.menuUII.setToolTip(_translate("HorizontalPanel", "Menu key"))
        self.vdownn.setToolTip(_translate("HorizontalPanel", "Volume Up"))
        self.homee.setToolTip(_translate("HorizontalPanel", "Home key"))
        self.label.setText(_translate("HorizontalPanel", "::"))
from . import rsrc_rc

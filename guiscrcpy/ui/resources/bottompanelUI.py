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
        Panel.resize(328, 26)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Panel.setWindowIcon(icon)
        Panel.setStyleSheet("\n"
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
        self.backk = QtWidgets.QPushButton(Panel)
        self.backk.setEnabled(True)
        self.backk.setGeometry(QtCore.QRect(210, 0, 51, 25))
        self.backk.setStyleSheet("")
        self.backk.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backk.setIcon(icon1)
        self.backk.setObjectName("backk")
        self.powerUII = QtWidgets.QPushButton(Panel)
        self.powerUII.setEnabled(True)
        self.powerUII.setGeometry(QtCore.QRect(20, 0, 61, 25))
        self.powerUII.setStyleSheet("")
        self.powerUII.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/power.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.powerUII.setIcon(icon2)
        self.powerUII.setCheckable(False)
        self.powerUII.setObjectName("powerUII")
        self.menuUII = QtWidgets.QPushButton(Panel)
        self.menuUII.setEnabled(True)
        self.menuUII.setGeometry(QtCore.QRect(90, 0, 51, 25))
        self.menuUII.setStyleSheet("")
        self.menuUII.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/reorder-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuUII.setIcon(icon3)
        self.menuUII.setObjectName("menuUII")
        self.vdownn = QtWidgets.QPushButton(Panel)
        self.vdownn.setEnabled(True)
        self.vdownn.setGeometry(QtCore.QRect(270, 0, 31, 25))
        self.vdownn.setStyleSheet("")
        self.vdownn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/reduced-volume.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vdownn.setIcon(icon4)
        self.vdownn.setObjectName("vdownn")
        self.homee = QtWidgets.QPushButton(Panel)
        self.homee.setEnabled(True)
        self.homee.setGeometry(QtCore.QRect(140, 0, 71, 25))
        self.homee.setStyleSheet("")
        self.homee.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homee.setIcon(icon5)
        self.homee.setObjectName("homee")
        self.vupp = QtWidgets.QPushButton(Panel)
        self.vupp.setEnabled(True)
        self.vupp.setGeometry(QtCore.QRect(300, 0, 31, 25))
        self.vupp.setStyleSheet("")
        self.vupp.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vupp.setIcon(icon6)
        self.vupp.setObjectName("vupp")
        self.label = QtWidgets.QLabel(Panel)
        self.label.setGeometry(QtCore.QRect(0, -10, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.homee.raise_()
        self.backk.raise_()
        self.powerUII.raise_()
        self.menuUII.raise_()
        self.vdownn.raise_()
        self.vupp.raise_()
        self.label.raise_()

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        _translate = QtCore.QCoreApplication.translate
        Panel.setWindowTitle(_translate("Panel", "guiscrcpy"))
        self.backk.setToolTip(_translate("Panel", "Back key"))
        self.powerUII.setToolTip(_translate("Panel", "Power on/off"))
        self.menuUII.setToolTip(_translate("Panel", "Menu key"))
        self.vdownn.setToolTip(_translate("Panel", "Volume Up"))
        self.homee.setToolTip(_translate("Panel", "Home key"))
        self.label.setText(_translate("Panel", "::"))


import rsrc_rc

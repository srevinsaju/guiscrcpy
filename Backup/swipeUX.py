# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_self(object):
    def setupUi(self, self):
        self.setObjectName("self")
        self.resize(104, 70)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.swirt.setIcon(icon1)
        self.swirt.setObjectName("swirt")
        self.swilf = QtWidgets.QPushButton(self.centralwidget)
        self.swilf.setGeometry(QtCore.QRect(0, 20, 30, 30))
        self.swilf.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.swilf.setIcon(icon2)
        self.swilf.setObjectName("swilf")
        self.swidn = QtWidgets.QPushButton(self.centralwidget)
        self.swidn.setGeometry(QtCore.QRect(20, 40, 30, 30))
        self.swidn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.swidn.setIcon(icon3)
        self.swidn.setObjectName("swidn")
        self.swiup = QtWidgets.QPushButton(self.centralwidget)
        self.swiup.setGeometry(QtCore.QRect(20, 0, 30, 30))
        self.swiup.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-sign-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.swiup.setIcon(icon4)
        self.swiup.setObjectName("swiup")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))


import rsrc_rc

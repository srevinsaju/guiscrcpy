# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiscrcpy/ui/downloader.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(222, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 221, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.stat = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.stat.setFont(font)
        self.stat.setScaledContents(False)
        self.stat.setAlignment(QtCore.Qt.AlignCenter)
        self.stat.setObjectName("stat")
        self.verticalLayout.addWidget(self.stat)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Initializing"))
        self.stat.setText(_translate("Dialog", "guiscrcpy"))
        self.label_3.setText(_translate("Dialog", "Initializing"))
from . import rsrc_rc

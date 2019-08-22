# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notif_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(270, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rsrc/android_circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.0742574 rgba(43, 43, 43, 255));")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(5, 5, 261, 320))
        self.listWidget.setMaximumSize(QtCore.QSize(261, 320))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.listWidget.setFont(font)
        self.listWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.0742574 rgba(43, 43, 43, 255));\n"
"\n"
"color: rgb(238, 238, 236);\n"
"alternate-background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(25, 25, 25, 255), stop:0.0845771 rgba(81, 81, 81, 255));")
        self.listWidget.setLineWidth(10)
        self.listWidget.setMidLineWidth(10)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragEnabled(False)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setIconSize(QtCore.QSize(2, 4))
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setMovement(QtWidgets.QListView.Free)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setBatchSize(100)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setItemAlignment(QtCore.Qt.AlignHCenter)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GUI ScrcPy - Toolkit"))



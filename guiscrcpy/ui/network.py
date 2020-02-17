# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NetworkUI(object):
    def setupUi(self, NetworkUI):
        NetworkUI.setObjectName("NetworkUI")
        NetworkUI.setWindowModality(QtCore.Qt.ApplicationModal)
        NetworkUI.resize(324, 299)
        self.centralwidget = QtWidgets.QWidget(NetworkUI)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 4, 325, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setToolTipDuration(2)
        self.spinBox.setMinimum(1000)
        self.spinBox.setMaximum(9999)
        self.spinBox.setProperty("value", 5555)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 8, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 3)
        self.nm_connect = QtWidgets.QPushButton(self.layoutWidget)
        self.nm_connect.setObjectName("nm_connect")
        self.gridLayout.addWidget(self.nm_connect, 8, 2, 1, 1)
        self.nm_det = QtWidgets.QPushButton(self.layoutWidget)
        self.nm_det.setEnabled(False)
        self.nm_det.setText("")
        self.nm_det.setObjectName("nm_det")
        self.gridLayout.addWidget(self.nm_det, 2, 0, 1, 3)
        self.listView = QtWidgets.QListWidget(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 3)
        self.nm_refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.nm_refresh.setObjectName("nm_refresh")
        self.gridLayout.addWidget(self.nm_refresh, 8, 1, 1, 1)
        NetworkUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NetworkUI)
        self.statusbar.setObjectName("statusbar")
        NetworkUI.setStatusBar(self.statusbar)

        self.retranslateUi(NetworkUI)
        QtCore.QMetaObject.connectSlotsByName(NetworkUI)

    def retranslateUi(self, NetworkUI):
        _translate = QtCore.QCoreApplication.translate
        NetworkUI.setWindowTitle(_translate("NetworkUI", "Network Manager"))
        self.label.setText(_translate("NetworkUI", "List of Network Devices"))
        self.spinBox.setToolTip(_translate("NetworkUI", "Port number"))
        self.spinBox.setStatusTip(_translate("NetworkUI", "Port number"))
        self.nm_connect.setStatusTip(_translate("NetworkUI", "Establish connection"))
        self.nm_connect.setText(_translate("NetworkUI", "CONNECT"))
        self.nm_refresh.setStatusTip(_translate("NetworkUI", "Refresh Devices list"))
        self.nm_refresh.setText(_translate("NetworkUI", "REFRESH"))

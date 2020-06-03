# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'network.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_NetworkUI(object):
    def setupUi(self, NetworkUI):
        if not NetworkUI.objectName():
            NetworkUI.setObjectName(u"NetworkUI")
        NetworkUI.setWindowModality(Qt.ApplicationModal)
        NetworkUI.resize(374, 414)
        self.centralwidget = QWidget(NetworkUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 5, 371, 381))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.listView = QListWidget(self.widget)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 0, 0, 1, 2)

        self.nm_refresh = QPushButton(self.widget)
        self.nm_refresh.setObjectName(u"nm_refresh")

        self.gridLayout.addWidget(self.nm_refresh, 5, 0, 1, 1)

        self.tcpip = QPushButton(self.widget)
        self.tcpip.setObjectName(u"tcpip")

        self.gridLayout.addWidget(self.tcpip, 4, 1, 1, 1)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setToolTipDuration(2)
        self.spinBox.setMinimum(1000)
        self.spinBox.setMaximum(9999)
        self.spinBox.setValue(5555)

        self.gridLayout.addWidget(self.spinBox, 4, 0, 1, 1)

        self.nm_connect = QPushButton(self.widget)
        self.nm_connect.setObjectName(u"nm_connect")

        self.gridLayout.addWidget(self.nm_connect, 5, 1, 1, 1)

        self.nm_det = QPushButton(self.widget)
        self.nm_det.setObjectName(u"nm_det")
        self.nm_det.setEnabled(False)

        self.gridLayout.addWidget(self.nm_det, 2, 0, 1, 2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        NetworkUI.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(NetworkUI)
        self.statusbar.setObjectName(u"statusbar")
        NetworkUI.setStatusBar(self.statusbar)

        self.retranslateUi(NetworkUI)

        QMetaObject.connectSlotsByName(NetworkUI)
    # setupUi

    def retranslateUi(self, NetworkUI):
        NetworkUI.setWindowTitle(QCoreApplication.translate("NetworkUI", u"Network Manager", None))
        self.label.setText(QCoreApplication.translate("NetworkUI", u"List of Network Devices", None))
#if QT_CONFIG(statustip)
        self.nm_refresh.setStatusTip(QCoreApplication.translate("NetworkUI", u"Refresh Devices list", None))
#endif // QT_CONFIG(statustip)
        self.nm_refresh.setText(QCoreApplication.translate("NetworkUI", u"REFRESH", None))
        self.tcpip.setText(QCoreApplication.translate("NetworkUI", u"TCPIP", None))
#if QT_CONFIG(tooltip)
        self.spinBox.setToolTip(QCoreApplication.translate("NetworkUI", u"Port number", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spinBox.setStatusTip(QCoreApplication.translate("NetworkUI", u"Port number", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.nm_connect.setStatusTip(QCoreApplication.translate("NetworkUI", u"Establish connection", None))
#endif // QT_CONFIG(statustip)
        self.nm_connect.setText(QCoreApplication.translate("NetworkUI", u"CONNECT", None))
        self.nm_det.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("NetworkUI", u"Cannot find your IP address? Enter it manually here", None))
    # retranslateUi


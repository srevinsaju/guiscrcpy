# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bottompanelui.ui'
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

from  . import rsrc_rc

class Ui_HorizontalPanel(object):
    def setupUi(self, HorizontalPanel):
        if not HorizontalPanel.objectName():
            HorizontalPanel.setObjectName(u"HorizontalPanel")
        HorizontalPanel.resize(397, 24)
        icon = QIcon()
        icon.addFile(u":/res/ui/guiscrcpy_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        HorizontalPanel.setWindowIcon(icon)
        HorizontalPanel.setStyleSheet(u"\n"
".QPushButton {\n"
"border-radius: 1px;\n"
"color: rgb(0, 0, 0);\n"
" \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
"                    }\n"
"\n"
"QPushButton:pressed {\n"
"border-radius: 5px;\n"
"					  \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"QPushButton:hover {\n"
"border-radius: 5px;\n"
"					  \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        }\n"
"")
        self.backk = QPushButton(HorizontalPanel)
        self.backk.setObjectName(u"backk")
        self.backk.setEnabled(True)
        self.backk.setGeometry(QRect(230, 0, 51, 25))
        self.backk.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/chevron-sign-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backk.setIcon(icon1)
        self.powerUII = QPushButton(HorizontalPanel)
        self.powerUII.setObjectName(u"powerUII")
        self.powerUII.setEnabled(True)
        self.powerUII.setGeometry(QRect(20, 0, 81, 25))
        self.powerUII.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.powerUII.setIcon(icon2)
        self.powerUII.setCheckable(False)
        self.menuUII = QPushButton(HorizontalPanel)
        self.menuUII.setObjectName(u"menuUII")
        self.menuUII.setEnabled(True)
        self.menuUII.setGeometry(QRect(110, 0, 51, 25))
        self.menuUII.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/reorder-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuUII.setIcon(icon3)
        self.vdownn = QPushButton(HorizontalPanel)
        self.vdownn.setObjectName(u"vdownn")
        self.vdownn.setEnabled(True)
        self.vdownn.setGeometry(QRect(290, 0, 31, 25))
        self.vdownn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/reduced-volume.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vdownn.setIcon(icon4)
        self.homee = QPushButton(HorizontalPanel)
        self.homee.setObjectName(u"homee")
        self.homee.setEnabled(True)
        self.homee.setGeometry(QRect(160, 0, 71, 25))
        self.homee.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homee.setIcon(icon5)
        self.vupp = QPushButton(HorizontalPanel)
        self.vupp.setObjectName(u"vupp")
        self.vupp.setEnabled(True)
        self.vupp.setGeometry(QRect(320, 0, 31, 25))
        self.vupp.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/volume-up-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vupp.setIcon(icon6)
        self.label = QLabel(HorizontalPanel)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -10, 20, 41))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.bp_close = QPushButton(HorizontalPanel)
        self.bp_close.setObjectName(u"bp_close")
        self.bp_close.setEnabled(True)
        self.bp_close.setGeometry(QRect(350, 0, 31, 25))
        self.bp_close.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cross-mark-on-a-black-circle-background.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bp_close.setIcon(icon7)
        self.bp_device_id = QPushButton(HorizontalPanel)
        self.bp_device_id.setObjectName(u"bp_device_id")
        self.bp_device_id.setGeometry(QRect(380, 0, 20, 31))
        self.bp_device_id.setStyleSheet(u"")
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

        QMetaObject.connectSlotsByName(HorizontalPanel)
    # setupUi

    def retranslateUi(self, HorizontalPanel):
        HorizontalPanel.setWindowTitle(QCoreApplication.translate("HorizontalPanel", u"guiscrcpy", None))
#if QT_CONFIG(tooltip)
        self.backk.setToolTip(QCoreApplication.translate("HorizontalPanel", u"Back key", None))
#endif // QT_CONFIG(tooltip)
        self.backk.setText("")
#if QT_CONFIG(tooltip)
        self.powerUII.setToolTip(QCoreApplication.translate("HorizontalPanel", u"Power on/off", None))
#endif // QT_CONFIG(tooltip)
        self.powerUII.setText("")
#if QT_CONFIG(tooltip)
        self.menuUII.setToolTip(QCoreApplication.translate("HorizontalPanel", u"Menu key", None))
#endif // QT_CONFIG(tooltip)
        self.menuUII.setText("")
#if QT_CONFIG(tooltip)
        self.vdownn.setToolTip(QCoreApplication.translate("HorizontalPanel", u"Volume Up", None))
#endif // QT_CONFIG(tooltip)
        self.vdownn.setText("")
#if QT_CONFIG(tooltip)
        self.homee.setToolTip(QCoreApplication.translate("HorizontalPanel", u"Home key", None))
#endif // QT_CONFIG(tooltip)
        self.homee.setText("")
        self.vupp.setText("")
        self.label.setText(QCoreApplication.translate("HorizontalPanel", u"::", None))
        self.bp_close.setText("")
        self.bp_device_id.setText("")
    # retranslateUi


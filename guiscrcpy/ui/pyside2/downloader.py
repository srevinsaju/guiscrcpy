# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloader.ui'
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

class Ui_Initializer(object):
    def setupUi(self, Initializer):
        if not Initializer.objectName():
            Initializer.setObjectName(u"Initializer")
        Initializer.resize(222, 320)
        icon = QIcon()
        icon.addFile(u":/res/ui/guiscrcpy_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Initializer.setWindowIcon(icon)
        self.widget = QWidget(Initializer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 221, 311))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setPixmap(QPixmap(u":/res/ui/guiscrcpy_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(15)

        self.verticalLayout.addWidget(self.label_2)

        self.stat = QLabel(self.widget)
        self.stat.setObjectName(u"stat")
        font = QFont()
        font.setFamily(u"Titillium Web")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.stat.setFont(font)
        self.stat.setScaledContents(False)
        self.stat.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.stat)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.retranslateUi(Initializer)

        QMetaObject.connectSlotsByName(Initializer)
    # setupUi

    def retranslateUi(self, Initializer):
        Initializer.setWindowTitle(QCoreApplication.translate("Initializer", u"Initializing", None))
        self.label_2.setText("")
        self.stat.setText(QCoreApplication.translate("Initializer", u"guiscrcpy", None))
        self.label_3.setText(QCoreApplication.translate("Initializer", u"Initializing", None))
    # retranslateUi


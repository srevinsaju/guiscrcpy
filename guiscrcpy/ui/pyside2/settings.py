# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(441, 447)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 441, 408))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.b1c2 = QLineEdit(self.layoutWidget)
        self.b1c2.setObjectName(u"b1c2")

        self.gridLayout.addWidget(self.b1c2, 10, 4, 1, 2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 11, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 11, 1, 1, 1)

        self.a1 = QCheckBox(self.layoutWidget)
        self.a1.setObjectName(u"a1")

        self.gridLayout.addWidget(self.a1, 0, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(25, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 10, 3, 1, 1)

        self.a4 = QCheckBox(self.layoutWidget)
        self.a4.setObjectName(u"a4")

        self.gridLayout.addWidget(self.a4, 4, 0, 1, 1)

        self.a6d1 = QToolButton(self.layoutWidget)
        self.a6d1.setObjectName(u"a6d1")

        self.gridLayout.addWidget(self.a6d1, 6, 1, 1, 1)

        self.b2c1 = QLineEdit(self.layoutWidget)
        self.b2c1.setObjectName(u"b2c1")

        self.gridLayout.addWidget(self.b2c1, 11, 2, 1, 1)

        self.a3 = QCheckBox(self.layoutWidget)
        self.a3.setObjectName(u"a3")

        self.gridLayout.addWidget(self.a3, 3, 0, 1, 1)

        self.a8c1 = QLineEdit(self.layoutWidget)
        self.a8c1.setObjectName(u"a8c1")

        self.gridLayout.addWidget(self.a8c1, 7, 1, 1, 5)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.a9 = QCheckBox(self.layoutWidget)
        self.a9.setObjectName(u"a9")

        self.gridLayout.addWidget(self.a9, 8, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 10, 1, 1, 1)

        self.updatebutton = QPushButton(self.layoutWidget)
        self.updatebutton.setObjectName(u"updatebutton")

        self.gridLayout.addWidget(self.updatebutton, 12, 2, 1, 4)

        self.a6 = QCheckBox(self.layoutWidget)
        self.a6.setObjectName(u"a6")

        self.gridLayout.addWidget(self.a6, 6, 0, 1, 1)

        self.a5c1 = QLineEdit(self.layoutWidget)
        self.a5c1.setObjectName(u"a5c1")

        self.gridLayout.addWidget(self.a5c1, 5, 1, 1, 5)

        self.a8 = QCheckBox(self.layoutWidget)
        self.a8.setObjectName(u"a8")

        self.gridLayout.addWidget(self.a8, 7, 0, 1, 1)

        self.b1c1 = QLineEdit(self.layoutWidget)
        self.b1c1.setObjectName(u"b1c1")

        self.gridLayout.addWidget(self.b1c1, 10, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.b1 = QCheckBox(self.layoutWidget)
        self.b1.setObjectName(u"b1")

        self.gridLayout.addWidget(self.b1, 10, 0, 1, 1)

        self.a2c1 = QLineEdit(self.layoutWidget)
        self.a2c1.setObjectName(u"a2c1")
        self.a2c1.setEnabled(False)

        self.gridLayout.addWidget(self.a2c1, 1, 2, 1, 1)

        self.b2c2 = QLineEdit(self.layoutWidget)
        self.b2c2.setObjectName(u"b2c2")

        self.gridLayout.addWidget(self.b2c2, 11, 4, 1, 2)

        self.b2 = QCheckBox(self.layoutWidget)
        self.b2.setObjectName(u"b2")

        self.gridLayout.addWidget(self.b2, 11, 0, 1, 1)

        self.a2 = QCheckBox(self.layoutWidget)
        self.a2.setObjectName(u"a2")
        self.a2.setEnabled(False)

        self.gridLayout.addWidget(self.a2, 1, 0, 1, 1)

        self.b0 = QCheckBox(self.layoutWidget)
        self.b0.setObjectName(u"b0")

        self.gridLayout.addWidget(self.b0, 9, 0, 1, 1)

        self.b0c1 = QLineEdit(self.layoutWidget)
        self.b0c1.setObjectName(u"b0c1")

        self.gridLayout.addWidget(self.b0c1, 9, 1, 1, 5)

        self.a5 = QCheckBox(self.layoutWidget)
        self.a5.setObjectName(u"a5")

        self.gridLayout.addWidget(self.a5, 5, 0, 1, 1)

        self.a6c1 = QLineEdit(self.layoutWidget)
        self.a6c1.setObjectName(u"a6c1")

        self.gridLayout.addWidget(self.a6c1, 6, 2, 1, 4)

        self.a2c2 = QLineEdit(self.layoutWidget)
        self.a2c2.setObjectName(u"a2c2")
        self.a2c2.setEnabled(False)

        self.gridLayout.addWidget(self.a2c2, 1, 4, 1, 2)

        self.a3e1 = QSpinBox(self.layoutWidget)
        self.a3e1.setObjectName(u"a3e1")

        self.gridLayout.addWidget(self.a3e1, 3, 1, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"w", None))
        self.a1.setText(QCoreApplication.translate("MainWindow", u"Always on Top", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.a4.setText(QCoreApplication.translate("MainWindow", u"Prefer Text", None))
        self.a6d1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.a3.setText(QCoreApplication.translate("MainWindow", u"Max Frame / second (FPS)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.a9.setText(QCoreApplication.translate("MainWindow", u"Borderless Window", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.updatebutton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.a6.setText(QCoreApplication.translate("MainWindow", u"Record File", None))
        self.a8.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"Window position", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"Window size", None))
        self.a2.setText(QCoreApplication.translate("MainWindow", u"Crop Width", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"Window Title", None))
        self.a5.setText(QCoreApplication.translate("MainWindow", u"Push Target", None))
    # retranslateUi


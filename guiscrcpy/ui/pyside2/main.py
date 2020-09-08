# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide2.QtGui import QGradient
from PySide2.QtWidgets import *

from  . import rsrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(539, 629)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 420))
        font = QFont()
        font.setFamily(u"Titillium Web")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/ui/guiscrcpy_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"border-radius: 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
"color: rgb(0, 0, 0);\n"
"}\n"
".QPushButton:hover {\n"
"border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
"color: rgb(0, 0, 0);\n"
" }\n"
".QPushButton#quit{\n"
"                        background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 155, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
" }\n"
".QPushButton#quit:hover{             \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(172, 0, 0,"
                        " 255), stop:1 rgba(175, 106, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
" }\n"
".QPushButton#usbaud{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.901961 rgba(152, 0, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
".QPushButton#usbaud:hover{                        \n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(172, 0, 0, 255), stop:1 rgba(175, 106, 0, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
".QPushButton#mapnow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(253, 0, 255, 255), stop:0.990196 rgba(88, 0, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
" }\n"
".QPushButton#initmapnow{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.0196078 rgba(0, 141, 255, 255), stop:1 rgba(52, 0, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"."
                        "QPushButton#initmapnow:hover{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.0196078 rgba(0, 72, 131, 255), stop:1 rgba(24, 0, 122, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
" }\n"
".QPushButton#mapnow:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(199, 0, 255, 255), stop:0.990196 rgba(88, 0, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
".QPushButton#network_button{\n"
"background-color: rgb(10, 10, 10);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;	\n"
" }\n"
".QPushButton#settings_button{\n"
"background-color: rgb(10, 10, 10);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;	\n"
" }\n"
".QPushButton#refreshdevices{\n"
"background-color: rgb(10, 10, 10);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;	\n"
" }\n"
".QPushButton#restart_adb_server{\n"
"background-color: rgb(10, 10, 10);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;	\n"
" }\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(24)
        sizePolicy1.setVerticalStretch(25)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(500, 300))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(7, 1, 7, -1)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_4.setVerticalSpacing(1)
        self.fullscreen = QCheckBox(self.frame)
        self.fullscreen.setObjectName(u"fullscreen")
        sizePolicy2.setHeightForWidth(self.fullscreen.sizePolicy().hasHeightForWidth())
        self.fullscreen.setSizePolicy(sizePolicy2)
        self.fullscreen.setMinimumSize(QSize(10, 20))
        font1 = QFont()
        font1.setFamily(u"Noto Sans")
        font1.setPointSize(10)
        self.fullscreen.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/increase-size-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen.setIcon(icon1)

        self.gridLayout_4.addWidget(self.fullscreen, 0, 4, 1, 1)

        self.aotop = QCheckBox(self.frame)
        self.aotop.setObjectName(u"aotop")
        sizePolicy2.setHeightForWidth(self.aotop.sizePolicy().hasHeightForWidth())
        self.aotop.setSizePolicy(sizePolicy2)
        self.aotop.setMinimumSize(QSize(10, 20))
        self.aotop.setFont(font1)
        self.aotop.setToolTipDuration(2)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/fire-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.aotop.setIcon(icon2)

        self.gridLayout_4.addWidget(self.aotop, 1, 5, 1, 1)

        self.refreshdevices = QPushButton(self.frame)
        self.refreshdevices.setObjectName(u"refreshdevices")
        sizePolicy2.setHeightForWidth(self.refreshdevices.sizePolicy().hasHeightForWidth())
        self.refreshdevices.setSizePolicy(sizePolicy2)
        self.refreshdevices.setMinimumSize(QSize(22, 22))
        self.refreshdevices.setMaximumSize(QSize(30, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/refresh-page-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshdevices.setIcon(icon3)
        self.refreshdevices.setIconSize(QSize(15, 15))

        self.gridLayout_4.addWidget(self.refreshdevices, 7, 2, 1, 1)

        self.check_swipe_panel = QCheckBox(self.frame)
        self.check_swipe_panel.setObjectName(u"check_swipe_panel")
        self.check_swipe_panel.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/guiscrcpy_swipe_panel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.check_swipe_panel.setIcon(icon4)

        self.gridLayout_4.addWidget(self.check_swipe_panel, 2, 0, 1, 4)

        self.showTouches = QCheckBox(self.frame)
        self.showTouches.setObjectName(u"showTouches")
        sizePolicy2.setHeightForWidth(self.showTouches.sizePolicy().hasHeightForWidth())
        self.showTouches.setSizePolicy(sizePolicy2)
        self.showTouches.setMinimumSize(QSize(10, 20))
        self.showTouches.setFont(font1)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/hand-finger-pointing-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.showTouches.setIcon(icon5)

        self.gridLayout_4.addWidget(self.showTouches, 2, 4, 1, 1)

        self.recScui = QCheckBox(self.frame)
        self.recScui.setObjectName(u"recScui")
        self.recScui.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.recScui.sizePolicy().hasHeightForWidth())
        self.recScui.setSizePolicy(sizePolicy2)
        self.recScui.setMinimumSize(QSize(10, 20))
        font2 = QFont()
        font2.setFamily(u"Noto Sans")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.recScui.setFont(font2)
        self.recScui.setToolTipDuration(2)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/facetime-button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recScui.setIcon(icon6)

        self.gridLayout_4.addWidget(self.recScui, 0, 5, 1, 1)

        self.displayForceOn = QCheckBox(self.frame)
        self.displayForceOn.setObjectName(u"displayForceOn")
        sizePolicy2.setHeightForWidth(self.displayForceOn.sizePolicy().hasHeightForWidth())
        self.displayForceOn.setSizePolicy(sizePolicy2)
        self.displayForceOn.setMinimumSize(QSize(10, 20))
        self.displayForceOn.setFont(font1)
        self.displayForceOn.setToolTipDuration(2)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/bullseye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.displayForceOn.setIcon(icon7)

        self.gridLayout_4.addWidget(self.displayForceOn, 1, 4, 1, 1)

        self.lock_rotation = QCheckBox(self.frame)
        self.lock_rotation.setObjectName(u"lock_rotation")
        self.lock_rotation.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/padlock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.lock_rotation.setIcon(icon8)

        self.gridLayout_4.addWidget(self.lock_rotation, 2, 5, 1, 1)

        self.check_bottom_panel = QCheckBox(self.frame)
        self.check_bottom_panel.setObjectName(u"check_bottom_panel")
        self.check_bottom_panel.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/guiscrcpy_bottom_panel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.check_bottom_panel.setIcon(icon9)

        self.gridLayout_4.addWidget(self.check_bottom_panel, 0, 0, 1, 4)

        self.network_button = QPushButton(self.frame)
        self.network_button.setObjectName(u"network_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.network_button.sizePolicy().hasHeightForWidth())
        self.network_button.setSizePolicy(sizePolicy3)
        self.network_button.setToolTipDuration(2)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.network_button.setIcon(icon10)

        self.gridLayout_4.addWidget(self.network_button, 7, 0, 1, 1)

        self.check_side_panel = QCheckBox(self.frame)
        self.check_side_panel.setObjectName(u"check_side_panel")
        self.check_side_panel.setFont(font1)
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/guiscrcpy_side_panel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.check_side_panel.setIcon(icon11)

        self.gridLayout_4.addWidget(self.check_side_panel, 1, 0, 1, 4)

        self.settings_button = QPushButton(self.frame)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy3.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy3)
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/gear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon12)

        self.gridLayout_4.addWidget(self.settings_button, 7, 1, 1, 1)

        self.device_rotation = QComboBox(self.frame)
        self.device_rotation.addItem("")
        self.device_rotation.addItem("")
        self.device_rotation.addItem("")
        self.device_rotation.addItem("")
        self.device_rotation.addItem("")
        self.device_rotation.setObjectName(u"device_rotation")
        font3 = QFont()
        font3.setFamily(u"Noto Sans")
        font3.setPointSize(11)
        self.device_rotation.setFont(font3)

        self.gridLayout_4.addWidget(self.device_rotation, 7, 5, 1, 1)

        self.restart_adb_server = QPushButton(self.frame)
        self.restart_adb_server.setObjectName(u"restart_adb_server")
        sizePolicy2.setHeightForWidth(self.restart_adb_server.sizePolicy().hasHeightForWidth())
        self.restart_adb_server.setSizePolicy(sizePolicy2)
        self.restart_adb_server.setMinimumSize(QSize(22, 22))
        self.restart_adb_server.setMaximumSize(QSize(30, 16777215))
        self.restart_adb_server.setToolTipDuration(2)
        self.restart_adb_server.setIcon(icon7)
        self.restart_adb_server.setIconSize(QSize(15, 15))

        self.gridLayout_4.addWidget(self.restart_adb_server, 7, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.devices_view = QListWidget(self.frame)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/android.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.devices_view)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem.setIcon(icon13);
        self.devices_view.setObjectName(u"devices_view")
        sizePolicy2.setHeightForWidth(self.devices_view.sizePolicy().hasHeightForWidth())
        self.devices_view.setSizePolicy(sizePolicy2)
        self.devices_view.setMaximumSize(QSize(16777215, 90))
        font4 = QFont()
        font4.setFamily(u"Noto Sans")
        font4.setPointSize(9)
        self.devices_view.setFont(font4)
        self.devices_view.setAutoFillBackground(True)
        self.devices_view.setStyleSheet(u"alternate-background-color: rgb(35, 35, 35);")
        self.devices_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.devices_view.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.devices_view.setAutoScrollMargin(9)
        self.devices_view.setAlternatingRowColors(True)
        self.devices_view.setIconSize(QSize(35, 35))
        self.devices_view.setTextElideMode(Qt.ElideMiddle)
        self.devices_view.setProperty("isWrapping", False)
        self.devices_view.setResizeMode(QListView.Adjust)
        self.devices_view.setViewMode(QListView.IconMode)
        self.devices_view.setUniformItemSizes(True)
        self.devices_view.setBatchSize(100)
        self.devices_view.setItemAlignment(Qt.AlignCenter)
        self.devices_view.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.devices_view)

        self.private_message_box_adb = QPushButton(self.frame)
        self.private_message_box_adb.setObjectName(u"private_message_box_adb")
        sizePolicy2.setHeightForWidth(self.private_message_box_adb.sizePolicy().hasHeightForWidth())
        self.private_message_box_adb.setSizePolicy(sizePolicy2)
        self.private_message_box_adb.setFont(font3)

        self.verticalLayout.addWidget(self.private_message_box_adb)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dimensionDefaultCheckbox = QCheckBox(self.frame)
        self.dimensionDefaultCheckbox.setObjectName(u"dimensionDefaultCheckbox")
        sizePolicy2.setHeightForWidth(self.dimensionDefaultCheckbox.sizePolicy().hasHeightForWidth())
        self.dimensionDefaultCheckbox.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamily(u"Noto Sans")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.dimensionDefaultCheckbox.setFont(font5)
        self.dimensionDefaultCheckbox.setChecked(True)

        self.gridLayout_3.addWidget(self.dimensionDefaultCheckbox, 0, 3, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font3)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.bitrateText = QLineEdit(self.frame)
        self.bitrateText.setObjectName(u"bitrateText")
        sizePolicy2.setHeightForWidth(self.bitrateText.sizePolicy().hasHeightForWidth())
        self.bitrateText.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamily(u"Titillium Web")
        font6.setPointSize(26)
        font6.setBold(True)
        font6.setWeight(75)
        self.bitrateText.setFont(font6)
        self.bitrateText.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 0, 255));")
        self.bitrateText.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.bitrateText, 2, 1, 1, 1)

        self.dial = QDial(self.frame)
        self.dial.setObjectName(u"dial")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy4)
        self.dial.setFont(font3)
        self.dial.setCursor(QCursor(Qt.SizeHorCursor))
        self.dial.setToolTipDuration(2)
        self.dial.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"color: rgb(255, 0, 127);\n"
"gridline-color: rgb(255, 0, 0);\n"
"selection-background-color: rgb(12, 255, 0);\n"
"\n"
"image: url(:/res/ui/guiscrcpy_logo.png);")
        self.dial.setMinimum(64)
        self.dial.setMaximum(16000)
        self.dial.setSingleStep(2)
        self.dial.setValue(8000)
        self.dial.setOrientation(Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(20.000000000000000)
        self.dial.setNotchesVisible(True)

        self.gridLayout_3.addWidget(self.dial, 0, 0, 4, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 5, 1, 1)

        self.dimensionSlider = QSlider(self.frame)
        self.dimensionSlider.setObjectName(u"dimensionSlider")
        self.dimensionSlider.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.dimensionSlider.sizePolicy().hasHeightForWidth())
        self.dimensionSlider.setSizePolicy(sizePolicy2)
        self.dimensionSlider.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dimensionSlider.setMinimum(320)
        self.dimensionSlider.setMaximum(2048)
        self.dimensionSlider.setValue(1280)
        self.dimensionSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.dimensionSlider, 3, 2, 1, 4)

        self.dimensionText = QLineEdit(self.frame)
        self.dimensionText.setObjectName(u"dimensionText")
        sizePolicy2.setHeightForWidth(self.dimensionText.sizePolicy().hasHeightForWidth())
        self.dimensionText.setSizePolicy(sizePolicy2)
        self.dimensionText.setFont(font6)
        self.dimensionText.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 17, 17);\n"
"border-radius: 10px;\n"
"")
        self.dimensionText.setMaxLength(32767)
        self.dimensionText.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.dimensionText, 2, 3, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.flaglineedit = QLineEdit(self.frame)
        self.flaglineedit.setObjectName(u"flaglineedit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.flaglineedit.sizePolicy().hasHeightForWidth())
        self.flaglineedit.setSizePolicy(sizePolicy5)
        font7 = QFont()
        font7.setFamily(u"Monospace")
        self.flaglineedit.setFont(font7)

        self.verticalLayout.addWidget(self.flaglineedit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.quit = QPushButton(self.frame)
        self.quit.setObjectName(u"quit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy6)
        self.quit.setMinimumSize(QSize(45, 45))
        self.quit.setToolTipDuration(2)
        self.quit.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/cross-mark-on-a-black-circle-background.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quit.setIcon(icon14)

        self.horizontalLayout.addWidget(self.quit)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy7)
        self.pushButton.setMinimumSize(QSize(45, 45))
        font8 = QFont()
        font8.setFamily(u"Titillium Web")
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.pushButton.setFont(font8)
        self.pushButton.setToolTipDuration(2)

        self.horizontalLayout.addWidget(self.pushButton)

        self.abtgit = QPushButton(self.frame)
        self.abtgit.setObjectName(u"abtgit")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.abtgit.sizePolicy().hasHeightForWidth())
        self.abtgit.setSizePolicy(sizePolicy8)
        self.abtgit.setMinimumSize(QSize(45, 45))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/github.logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.abtgit.setIcon(icon15)
        self.abtgit.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.abtgit)

        self.usbaud = QPushButton(self.frame)
        self.usbaud.setObjectName(u"usbaud")
        sizePolicy9 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(11)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.usbaud.sizePolicy().hasHeightForWidth())
        self.usbaud.setSizePolicy(sizePolicy9)
        self.usbaud.setMinimumSize(QSize(45, 45))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/volume-up-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.usbaud.setIcon(icon16)

        self.horizontalLayout.addWidget(self.usbaud)

        self.initmapnow = QPushButton(self.frame)
        self.initmapnow.setObjectName(u"initmapnow")
        sizePolicy9.setHeightForWidth(self.initmapnow.sizePolicy().hasHeightForWidth())
        self.initmapnow.setSizePolicy(sizePolicy9)
        self.initmapnow.setMinimumSize(QSize(45, 45))
        self.initmapnow.setToolTipDuration(3)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/mapper_init.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.initmapnow.setIcon(icon17)
        self.initmapnow.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.initmapnow)

        self.executeaction = QPushButton(self.frame)
        self.executeaction.setObjectName(u"executeaction")
        sizePolicy5.setHeightForWidth(self.executeaction.sizePolicy().hasHeightForWidth())
        self.executeaction.setSizePolicy(sizePolicy5)
        self.executeaction.setMinimumSize(QSize(45, 45))
        font9 = QFont()
        font9.setFamily(u"Titillium Web")
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.executeaction.setFont(font9)
        self.executeaction.setStyleSheet(u"")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/small-rocket-ship-silhouette.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.executeaction.setIcon(icon18)
        self.executeaction.setIconSize(QSize(20, 16))

        self.horizontalLayout.addWidget(self.executeaction)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(0, 255, 255, 255))
        gradient.setColorAt(1, QColor(0, 255, 0, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(0, 255, 255, 255))
        gradient1.setColorAt(1, QColor(0, 255, 0, 255))
        brush2 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(0, 255, 255, 255))
        gradient2.setColorAt(1, QColor(0, 255, 0, 255))
        brush3 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(85, 255, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(0, 255, 255, 255))
        gradient3.setColorAt(1, QColor(0, 255, 0, 255))
        brush6 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(0, 255, 255, 255))
        gradient4.setColorAt(1, QColor(0, 255, 0, 255))
        brush7 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(0, 255, 255, 255))
        gradient5.setColorAt(1, QColor(0, 255, 0, 255))
        brush8 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(0, 255, 255, 255))
        gradient6.setColorAt(1, QColor(0, 255, 0, 255))
        brush10 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(0, 255, 255, 255))
        gradient7.setColorAt(1, QColor(0, 255, 0, 255))
        brush11 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(0, 255, 255, 255))
        gradient8.setColorAt(1, QColor(0, 255, 0, 255))
        brush12 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
        brush13 = QBrush(QColor(255, 255, 255, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.progressBar.setPalette(palette)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(100)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout_5.addWidget(self.frame, 1, 0, 1, 1)

        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.horizontalLayout_2 = QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy10)
        self.label_4.setMinimumSize(QSize(60, 60))
        self.label_4.setMaximumSize(QSize(60, 60))
        self.label_4.setPixmap(QPixmap(u":/res/ui/guiscrcpy_logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_3 = QLabel(self.frame1)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)
        font10 = QFont()
        font10.setFamily(u"Titillium Web")
        font10.setPointSize(28)
        font10.setBold(True)
        font10.setItalic(False)
        font10.setWeight(75)
        self.label_3.setFont(font10)
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.build_label = QLabel(self.frame1)
        self.build_label.setObjectName(u"build_label")
        sizePolicy5.setHeightForWidth(self.build_label.sizePolicy().hasHeightForWidth())
        self.build_label.setSizePolicy(sizePolicy5)
        font11 = QFont()
        font11.setFamily(u"Noto Sans")
        self.build_label.setFont(font11)
        self.build_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.build_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout_5.addWidget(self.frame1, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"guiscrcpy", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(QCoreApplication.translate("MainWindow", u"GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
"                https://github.com/srevinsaju/guiscrcpy\n"
"            ", None))
#endif // QT_CONFIG(statustip)
        self.fullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
#if QT_CONFIG(tooltip)
        self.aotop.setToolTip(QCoreApplication.translate("MainWindow", u"Keep display always on top of other windows", None))
#endif // QT_CONFIG(tooltip)
        self.aotop.setText(QCoreApplication.translate("MainWindow", u"Always on Top", None))
        self.refreshdevices.setText("")
        self.check_swipe_panel.setText(QCoreApplication.translate("MainWindow", u"Swipe Panel", None))
        self.showTouches.setText(QCoreApplication.translate("MainWindow", u"Show touches", None))
#if QT_CONFIG(tooltip)
        self.recScui.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Record your screen mirroring to your home directory. In Linux, it is in ~guiscrcpy directory. In Windows, it is in C:\\Users\\&lt;username&gt;\\ with the UNIX date, followed by .mp4; For manual configuration and path selection, use the settings icon</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.recScui.setStatusTip(QCoreApplication.translate("MainWindow", u"See tooltip", None))
#endif // QT_CONFIG(statustip)
        self.recScui.setText(QCoreApplication.translate("MainWindow", u"Record screen", None))
#if QT_CONFIG(tooltip)
        self.displayForceOn.setToolTip(QCoreApplication.translate("MainWindow", u"Use your computer screen as your android device's HD Display", None))
#endif // QT_CONFIG(tooltip)
        self.displayForceOn.setText(QCoreApplication.translate("MainWindow", u"Keep display off ", None))
        self.lock_rotation.setText(QCoreApplication.translate("MainWindow", u"Lock Rotation", None))
        self.check_bottom_panel.setText(QCoreApplication.translate("MainWindow", u"Bottom Panel", None))
#if QT_CONFIG(tooltip)
        self.network_button.setToolTip(QCoreApplication.translate("MainWindow", u"Launch Network Manager", None))
#endif // QT_CONFIG(tooltip)
        self.network_button.setText("")
        self.check_side_panel.setText(QCoreApplication.translate("MainWindow", u"Side Panel", None))
        self.settings_button.setText("")
        self.device_rotation.setItemText(0, QCoreApplication.translate("MainWindow", u"Default Rotation", None))
        self.device_rotation.setItemText(1, QCoreApplication.translate("MainWindow", u"Potrait", None))
        self.device_rotation.setItemText(2, QCoreApplication.translate("MainWindow", u"Landscape", None))
        self.device_rotation.setItemText(3, QCoreApplication.translate("MainWindow", u"Potrait (flipped)", None))
        self.device_rotation.setItemText(4, QCoreApplication.translate("MainWindow", u"Landscape (flipped)", None))

#if QT_CONFIG(tooltip)
        self.restart_adb_server.setToolTip(QCoreApplication.translate("MainWindow", u"Restart the adb-server", None))
#endif // QT_CONFIG(tooltip)
        self.restart_adb_server.setText("")

        __sortingEnabled = self.devices_view.isSortingEnabled()
        self.devices_view.setSortingEnabled(False)
        ___qlistwidgetitem = self.devices_view.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nothing here", None));
        self.devices_view.setSortingEnabled(__sortingEnabled)

        self.private_message_box_adb.setText("")
        self.dimensionDefaultCheckbox.setText(QCoreApplication.translate("MainWindow", u"Keep Default Dimensions", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bitrate", None))
        self.bitrateText.setInputMask(QCoreApplication.translate("MainWindow", u"00000 A\\B/s", None))
        self.bitrateText.setText(QCoreApplication.translate("MainWindow", u"8000 KB/s", None))
#if QT_CONFIG(tooltip)
        self.dial.setToolTip(QCoreApplication.translate("MainWindow", u"Changing the bitrate of the screen mirrorring. Useful to show playback at normal speed without lags", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.dial.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjust Bitrate. Leave it untouched for defualts", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText("")
        self.dimensionText.setInputMask("")
        self.dimensionText.setText(QCoreApplication.translate("MainWindow", u"DEFAULT", None))
        self.flaglineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter additional flags to pass to scrcpy", None))
#if QT_CONFIG(statustip)
        self.quit.setStatusTip(QCoreApplication.translate("MainWindow", u"Quit GUI and end all subprocess windows ", None))
#endif // QT_CONFIG(statustip)
        self.quit.setText("")
#if QT_CONFIG(statustip)
        self.pushButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Reset guiscrcpy configuration files", None))
#endif // QT_CONFIG(statustip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"  RESET  ", None))
#if QT_CONFIG(statustip)
        self.abtgit.setStatusTip(QCoreApplication.translate("MainWindow", u"Check me out on Github", None))
#endif // QT_CONFIG(statustip)
        self.abtgit.setText("")
#if QT_CONFIG(statustip)
        self.usbaud.setStatusTip(QCoreApplication.translate("MainWindow", u"Start @rom1v's usbaudio. Needs usbaudio to be on PATH", None))
#endif // QT_CONFIG(statustip)
        self.usbaud.setText("")
#if QT_CONFIG(tooltip)
        self.initmapnow.setToolTip(QCoreApplication.translate("MainWindow", u"Initialize mapper", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.initmapnow.setStatusTip(QCoreApplication.translate("MainWindow", u"Initialize mapper", None))
#endif // QT_CONFIG(statustip)
        self.initmapnow.setText("")
#if QT_CONFIG(statustip)
        self.executeaction.setStatusTip(QCoreApplication.translate("MainWindow", u"Start Scrcpy Executable right now. Please check if Scrcpy is added to path", None))
#endif // QT_CONFIG(statustip)
        self.executeaction.setText(QCoreApplication.translate("MainWindow", u"START SCRCPY", None))
#if QT_CONFIG(statustip)
        self.progressBar.setStatusTip(QCoreApplication.translate("MainWindow", u"Progress Bar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
"                        https://github.com/srevinsaju/guiscrcpy\n"
"                    ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip(QCoreApplication.translate("MainWindow", u"GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
"                        https://github.com/srevinsaju/guiscrcpy\n"
"                    ", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText("")
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
"                        https://github.com/srevinsaju/guiscrcpy\n"
"                    ", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"guiscrcpy                          ", None))
        self.build_label.setText(QCoreApplication.translate("MainWindow", u"Build", None))
    # retranslateUi


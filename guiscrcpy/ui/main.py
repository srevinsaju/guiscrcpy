# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from . import rsrc_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(547, 482)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 420))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton {\n"
                                 "border-radius: 10px;\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "}\n"
                                 "QPushButton:pressed {\n"
                                 "border-radius: 10px;\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "}\n"
                                 ".QPushButton:hover {\n"
                                 "border-radius: 10px;\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 " }\n"
                                 ".QPushButton#quit{\n"
                                 "                        background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 155, 0, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;\n"
                                 " }\n"
                                 ".QPushButton#quit:hover{             \n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(172, 0, 0, 255), stop:1 rgba(175, 106, 0, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;\n"
                                 " }\n"
                                 ".QPushButton#usbaud{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.901961 rgba(152, 0, 255, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 ".QPushButton#usbaud:hover{                        \n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(172, 0, 0, 255), stop:1 rgba(175, 106, 0, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 ".QPushButton#mapnow{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(253, 0, 255, 255), stop:0.990196 rgba(88, 0, 255, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;\n"
                                 " }\n"
                                 ".QPushButton#mapnow{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(199, 0, 255, 255), stop:0.990196 rgba(88, 0, 255, 255));\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;\n"
                                 "}\n"
                                 ".QPushButton#network_button{\n"
                                 "background-color: rgb(60, 60, 60);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;    \n"
                                 " }\n"
                                 "\n"
                                 ".QPushButton#settings_button{\n"
                                 "background-color: rgb(60, 60, 60);\n"
                                 "color: rgb(0, 0, 0);\n"
                                 "border-radius: 10px;    \n"
                                 " }\n"
                                 "\n"
                                 "")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 300))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_4.setMaximumSize(QtCore.QSize(60, 60))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.build_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.build_label.sizePolicy().hasHeightForWidth())
        self.build_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        self.build_label.setFont(font)
        self.build_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.build_label.setObjectName("build_label")
        self.verticalLayout_2.addWidget(self.build_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setObjectName("frame1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(7, 1, 7, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setVerticalSpacing(1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.displayForceOn = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.displayForceOn.sizePolicy().hasHeightForWidth())
        self.displayForceOn.setSizePolicy(sizePolicy)
        self.displayForceOn.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.displayForceOn.setFont(font)
        self.displayForceOn.setToolTipDuration(2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/bullseye.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.displayForceOn.setIcon(icon1)
        self.displayForceOn.setObjectName("displayForceOn")
        self.gridLayout_4.addWidget(self.displayForceOn, 1, 0, 1, 3)
        self.showTouches = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.showTouches.sizePolicy().hasHeightForWidth())
        self.showTouches.setSizePolicy(sizePolicy)
        self.showTouches.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.showTouches.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            ":/icons/icons/hand-finger-pointing-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.showTouches.setIcon(icon2)
        self.showTouches.setObjectName("showTouches")
        self.gridLayout_4.addWidget(self.showTouches, 0, 4, 1, 1)
        self.network_button = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.network_button.sizePolicy().hasHeightForWidth())
        self.network_button.setSizePolicy(sizePolicy)
        self.network_button.setToolTipDuration(2)
        self.network_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/wifi.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.network_button.setIcon(icon3)
        self.network_button.setObjectName("network_button")
        self.gridLayout_4.addWidget(self.network_button, 2, 0, 1, 1)
        self.notifChecker = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.notifChecker.sizePolicy().hasHeightForWidth())
        self.notifChecker.setSizePolicy(sizePolicy)
        self.notifChecker.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.notifChecker.setFont(font)
        self.notifChecker.setToolTipDuration(2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(
            ":/icons/icons/bell-musical-tool.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notifChecker.setIcon(icon4)
        self.notifChecker.setObjectName("notifChecker")
        self.gridLayout_4.addWidget(self.notifChecker, 1, 3, 1, 1)
        self.recScui = QtWidgets.QCheckBox(self.frame1)
        self.recScui.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.recScui.sizePolicy().hasHeightForWidth())
        self.recScui.setSizePolicy(sizePolicy)
        self.recScui.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.recScui.setFont(font)
        self.recScui.setToolTipDuration(2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(
            ":/icons/icons/facetime-button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recScui.setIcon(icon5)
        self.recScui.setObjectName("recScui")
        self.gridLayout_4.addWidget(self.recScui, 1, 4, 1, 1)
        self.runningNot = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.runningNot.sizePolicy().hasHeightForWidth())
        self.runningNot.setSizePolicy(sizePolicy)
        self.runningNot.setText("")
        self.runningNot.setObjectName("runningNot")
        self.gridLayout_4.addWidget(self.runningNot, 2, 2, 1, 3)
        self.fullscreen = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fullscreen.sizePolicy().hasHeightForWidth())
        self.fullscreen.setSizePolicy(sizePolicy)
        self.fullscreen.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.fullscreen.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(
            ":/icons/icons/increase-size-option.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fullscreen.setIcon(icon6)
        self.fullscreen.setObjectName("fullscreen")
        self.gridLayout_4.addWidget(self.fullscreen, 0, 3, 1, 1)
        self.aotop = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.aotop.sizePolicy().hasHeightForWidth())
        self.aotop.setSizePolicy(sizePolicy)
        self.aotop.setMinimumSize(QtCore.QSize(10, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.aotop.setFont(font)
        self.aotop.setToolTipDuration(2)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/fire-symbol.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aotop.setIcon(icon7)
        self.aotop.setObjectName("aotop")
        self.gridLayout_4.addWidget(self.aotop, 0, 0, 1, 3)
        self.settings_button = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/gear.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_button.setIcon(icon8)
        self.settings_button.setObjectName("settings_button")
        self.gridLayout_4.addWidget(self.settings_button, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bitrateText = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bitrateText.sizePolicy().hasHeightForWidth())
        self.bitrateText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.bitrateText.setFont(font)
        self.bitrateText.setStatusTip("")
        self.bitrateText.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       "border-radius: 10px;\n"
                                       "\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 0, 255));")
        self.bitrateText.setTextFormat(QtCore.Qt.AutoText)
        self.bitrateText.setAlignment(QtCore.Qt.AlignCenter)
        self.bitrateText.setObjectName("bitrateText")
        self.gridLayout_3.addWidget(self.bitrateText, 1, 1, 1, 1)
        self.dimensionSlider = QtWidgets.QSlider(self.frame1)
        self.dimensionSlider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dimensionSlider.sizePolicy().hasHeightForWidth())
        self.dimensionSlider.setSizePolicy(sizePolicy)
        self.dimensionSlider.setStyleSheet("color: rgb(255, 255, 255);")
        self.dimensionSlider.setMinimum(320)
        self.dimensionSlider.setMaximum(2048)
        self.dimensionSlider.setProperty("value", 1280)
        self.dimensionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.dimensionSlider.setObjectName("dimensionSlider")
        self.gridLayout_3.addWidget(self.dimensionSlider, 2, 2, 1, 1)
        self.dial = QtWidgets.QDial(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dial.sizePolicy().hasHeightForWidth())
        self.dial.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        self.dial.setFont(font)
        self.dial.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.dial.setToolTipDuration(2)
        self.dial.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                "color: rgb(255, 0, 127);\n"
                                "gridline-color: rgb(255, 0, 0);\n"
                                "selection-background-color: rgb(12, 255, 0);\n"
                                "\n"
                                "image: url(:/res/ui/guiscrcpy_logo.png);")
        self.dial.setMinimum(64)
        self.dial.setMaximum(16000)
        self.dial.setSingleStep(2)
        self.dial.setProperty("value", 8000)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(20.0)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.gridLayout_3.addWidget(self.dial, 0, 0, 3, 1)
        self.label = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.dimensionDefaultCheckbox = QtWidgets.QCheckBox(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dimensionDefaultCheckbox.sizePolicy().hasHeightForWidth())
        self.dimensionDefaultCheckbox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dimensionDefaultCheckbox.setFont(font)
        self.dimensionDefaultCheckbox.setChecked(True)
        self.dimensionDefaultCheckbox.setObjectName("dimensionDefaultCheckbox")
        self.gridLayout_3.addWidget(self.dimensionDefaultCheckbox, 0, 2, 1, 1)
        self.dimensionText = QtWidgets.QLabel(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dimensionText.sizePolicy().hasHeightForWidth())
        self.dimensionText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.dimensionText.setFont(font)
        self.dimensionText.setToolTipDuration(2)
        self.dimensionText.setStatusTip("")
        self.dimensionText.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(17, 17, 17);\n"
                                         "border-radius: 10px;\n"
                                         "")
        self.dimensionText.setTextFormat(QtCore.Qt.AutoText)
        self.dimensionText.setAlignment(QtCore.Qt.AlignCenter)
        self.dimensionText.setObjectName("dimensionText")
        self.gridLayout_3.addWidget(self.dimensionText, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.flaglineedit = QtWidgets.QLineEdit(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.flaglineedit.sizePolicy().hasHeightForWidth())
        self.flaglineedit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        self.flaglineedit.setFont(font)
        self.flaglineedit.setObjectName("flaglineedit")
        self.verticalLayout.addWidget(self.flaglineedit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.quit = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)
        self.quit.setMinimumSize(QtCore.QSize(45, 45))
        self.quit.setStyleSheet("")
        self.quit.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(
            ":/icons/icons/cross-mark-on-a-black-circle-background.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit.setIcon(icon9)
        self.quit.setObjectName("quit")
        self.horizontalLayout.addWidget(self.quit)
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.abtgit = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.abtgit.sizePolicy().hasHeightForWidth())
        self.abtgit.setSizePolicy(sizePolicy)
        self.abtgit.setMinimumSize(QtCore.QSize(45, 45))
        self.abtgit.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(
            ":/icons/icons/github.logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abtgit.setIcon(icon10)
        self.abtgit.setIconSize(QtCore.QSize(20, 20))
        self.abtgit.setObjectName("abtgit")
        self.horizontalLayout.addWidget(self.abtgit)
        self.abtme = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.abtme.sizePolicy().hasHeightForWidth())
        self.abtme.setSizePolicy(sizePolicy)
        self.abtme.setMinimumSize(QtCore.QSize(33, 45))
        self.abtme.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(
            ":/icons/icons/ss-branding.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.abtme.setIcon(icon11)
        self.abtme.setIconSize(QtCore.QSize(20, 20))
        self.abtme.setObjectName("abtme")
        self.horizontalLayout.addWidget(self.abtme)
        self.usbaud = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.usbaud.sizePolicy().hasHeightForWidth())
        self.usbaud.setSizePolicy(sizePolicy)
        self.usbaud.setMinimumSize(QtCore.QSize(45, 45))
        self.usbaud.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(
            ":/icons/icons/volume-up-interface-symbol.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.usbaud.setIcon(icon12)
        self.usbaud.setObjectName("usbaud")
        self.horizontalLayout.addWidget(self.usbaud)
        self.mapnow = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mapnow.sizePolicy().hasHeightForWidth())
        self.mapnow.setSizePolicy(sizePolicy)
        self.mapnow.setMinimumSize(QtCore.QSize(45, 45))
        self.mapnow.setToolTipDuration(3)
        self.mapnow.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(
            ":/icons/icons/four-black-squares.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mapnow.setIcon(icon13)
        self.mapnow.setObjectName("mapnow")
        self.horizontalLayout.addWidget(self.mapnow)
        self.executeaction = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.executeaction.sizePolicy().hasHeightForWidth())
        self.executeaction.setSizePolicy(sizePolicy)
        self.executeaction.setMinimumSize(QtCore.QSize(45, 45))
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.executeaction.setFont(font)
        self.executeaction.setStyleSheet("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(
            ":/icons/icons/small-rocket-ship-silhouette.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.executeaction.setIcon(icon14)
        self.executeaction.setIconSize(QtCore.QSize(20, 16))
        self.executeaction.setObjectName("executeaction")
        self.horizontalLayout.addWidget(self.executeaction)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.frame1)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 255, 255))
        gradient.setColorAt(1.0, QtGui.QColor(0, 255, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.progressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 0, 255));\n"
                                       "color: rgb(255,255,255);\n"
                                       "selection-color: rgb(255, 255, 255);\n"
                                       "selection-background-color: rgb(38, 255, 0);\n"
                                       "selection-background-color: rgb(85, 255, 0);")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.gridLayout_5.addWidget(self.frame1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "guiscrcpy"))
        MainWindow.setStatusTip(_translate("MainWindow", "GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
                                           "                https://github.com/srevinsaju/guiscrcpy\n"
                                           "            "))
        self.label_4.setToolTip(_translate("MainWindow", "GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
                                           "                        https://github.com/srevinsaju/guiscrcpy\n"
                                           "                    "))
        self.label_4.setStatusTip(_translate("MainWindow", "GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
                                             "                        https://github.com/srevinsaju/guiscrcpy\n"
                                             "                    "))
        self.label_3.setStatusTip(_translate("MainWindow", "GUI by srevinsaju, scrcpy engine by rom1v. Hosted on GitHub\n"
                                             "                        https://github.com/srevinsaju/guiscrcpy\n"
                                             "                    "))
        self.label_3.setText(_translate(
            "MainWindow", "guiscrcpy                          "))
        self.build_label.setText(_translate("MainWindow", "Build"))
        self.displayForceOn.setToolTip(_translate(
            "MainWindow", "Use your computer screen as your android device\'s HD Display"))
        self.displayForceOn.setText(_translate(
            "MainWindow", "Keep display off "))
        self.showTouches.setText(_translate("MainWindow", "Show touches"))
        self.network_button.setToolTip(_translate(
            "MainWindow", "Launch Network Manager"))
        self.notifChecker.setToolTip(_translate(
            "MainWindow", "Make guiscrcpy check for new notifications on your device. A status bar icon indicating new notifications will be visible. (Experimental)"))
        self.notifChecker.setText(_translate(
            "MainWindow", "Notification Auditor"))
        self.recScui.setToolTip(_translate(
            "MainWindow", "Record your screen mirroring to your home directory. In Linux, it is in ~guiscrcpy directory. In Windows, it is in C:Users<USER NAME> with the date in seconds, followed by .mp4"))
        self.recScui.setStatusTip(_translate("MainWindow", "See tooltip"))
        self.recScui.setText(_translate("MainWindow", "Record screen"))
        self.fullscreen.setText(_translate("MainWindow", "Fullscreen"))
        self.aotop.setToolTip(_translate(
            "MainWindow", "Keep display always on top of other windows"))
        self.aotop.setText(_translate("MainWindow", "Always on Top"))
        self.bitrateText.setText(_translate("MainWindow", "8000 KB/s"))
        self.dial.setToolTip(_translate(
            "MainWindow", "Changing the bitrate of the screen mirrorring. Useful to show playback at normal speed without lags"))
        self.dial.setStatusTip(_translate(
            "MainWindow", "Adjust Bitrate. Leave it untouched for defualts"))
        self.label.setText(_translate("MainWindow", "Bitrate"))
        self.dimensionDefaultCheckbox.setText(
            _translate("MainWindow", "Keep Default Dimensions"))
        self.dimensionText.setToolTip(_translate(
            "MainWindow", "Change device dimensions. scrcpy has some rendering problems upon changing dimensions"))
        self.dimensionText.setText(_translate("MainWindow", "DEFAULT"))
        self.flaglineedit.setPlaceholderText(_translate(
            "MainWindow", "Enter additional flags to pass to scrcpy"))
        self.quit.setStatusTip(_translate("MainWindow", "quit GUI"))
        self.pushButton.setText(_translate("MainWindow", "  RESET  "))
        self.mapnow.setToolTip(_translate(
            "MainWindow", "Device Point to Key mapping launcher. Click to register keys for the first time. For the subsequent launches, the button will start key listeners"))
        self.mapnow.setStatusTip(_translate(
            "MainWindow", "Device Point to Key mapping launcher. Click to register keys for the first time. For the subsequent launches, the button will start key listeners"))
        self.executeaction.setStatusTip(_translate(
            "MainWindow", "Start Scrcpy Executable right now. Please check if Scrcpy is added to path"))
        self.executeaction.setText(_translate("MainWindow", "START SCRCPY"))
        self.progressBar.setStatusTip(_translate("MainWindow", "Progress Bar"))

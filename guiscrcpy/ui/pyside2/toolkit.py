# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolkit_ui.ui'
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

class Ui_ToolbarPanel(object):
    def setupUi(self, ToolbarPanel):
        if not ToolbarPanel.objectName():
            ToolbarPanel.setObjectName(u"ToolbarPanel")
        ToolbarPanel.resize(30, 600)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ToolbarPanel.sizePolicy().hasHeightForWidth())
        ToolbarPanel.setSizePolicy(sizePolicy)
        ToolbarPanel.setMinimumSize(QSize(30, 337))
        ToolbarPanel.setMaximumSize(QSize(30, 600))
        ToolbarPanel.setBaseSize(QSize(30, 403))
        ToolbarPanel.setWindowTitle(u"guiscrcpy")
        icon = QIcon()
        icon.addFile(u":/res/ui/guiscrcpy_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        ToolbarPanel.setWindowIcon(icon)
        ToolbarPanel.setWindowOpacity(1.000000000000000)
        ToolbarPanel.setStyleSheet(u"QDialog{\n"
"width: 30px\n"
"}\n"
"QPushButton {\n"
"                        \n"
"\n"
"border-radius: 1px;\n"
"		background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
"color: rgb(0, 0, 0);\n"
"                        \n"
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
        self.layoutWidget = QWidget(ToolbarPanel)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 33, 601))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.screenfreeze = QPushButton(self.layoutWidget)
        self.screenfreeze.setObjectName(u"screenfreeze")
        self.screenfreeze.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.screenfreeze.sizePolicy().hasHeightForWidth())
        self.screenfreeze.setSizePolicy(sizePolicy1)
        self.screenfreeze.setMouseTracking(True)
        self.screenfreeze.setTabletTracking(True)
        self.screenfreeze.setAutoFillBackground(False)
        self.screenfreeze.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cross-mark-on-a-black-circle-background.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.screenfreeze.setIcon(icon1)
        self.screenfreeze.setFlat(True)

        self.verticalLayout.addWidget(self.screenfreeze)

        self.fullscreenUI = QPushButton(self.layoutWidget)
        self.fullscreenUI.setObjectName(u"fullscreenUI")
        self.fullscreenUI.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.fullscreenUI.sizePolicy().hasHeightForWidth())
        self.fullscreenUI.setSizePolicy(sizePolicy1)
        self.fullscreenUI.setMouseTracking(True)
        self.fullscreenUI.setTabletTracking(True)
        self.fullscreenUI.setAutoFillBackground(False)
        self.fullscreenUI.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/increase-size-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreenUI.setIcon(icon2)
        self.fullscreenUI.setFlat(True)

        self.verticalLayout.addWidget(self.fullscreenUI)

        self.notif_pull = QPushButton(self.layoutWidget)
        self.notif_pull.setObjectName(u"notif_pull")
        self.notif_pull.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.notif_pull.sizePolicy().hasHeightForWidth())
        self.notif_pull.setSizePolicy(sizePolicy1)
        self.notif_pull.setMouseTracking(True)
        self.notif_pull.setTabletTracking(True)
        self.notif_pull.setAutoFillBackground(False)
        self.notif_pull.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/bell-musical-tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notif_pull.setIcon(icon3)
        self.notif_pull.setFlat(True)

        self.verticalLayout.addWidget(self.notif_pull)

        self.notif_collapse = QPushButton(self.layoutWidget)
        self.notif_collapse.setObjectName(u"notif_collapse")
        self.notif_collapse.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.notif_collapse.sizePolicy().hasHeightForWidth())
        self.notif_collapse.setSizePolicy(sizePolicy1)
        self.notif_collapse.setMouseTracking(True)
        self.notif_collapse.setTabletTracking(True)
        self.notif_collapse.setAutoFillBackground(False)
        self.notif_collapse.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/bell-musical-tool(2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notif_collapse.setIcon(icon4)
        self.notif_collapse.setFlat(True)

        self.verticalLayout.addWidget(self.notif_collapse)

        self.clipD2PC = QPushButton(self.layoutWidget)
        self.clipD2PC.setObjectName(u"clipD2PC")
        self.clipD2PC.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.clipD2PC.sizePolicy().hasHeightForWidth())
        self.clipD2PC.setSizePolicy(sizePolicy1)
        self.clipD2PC.setMouseTracking(True)
        self.clipD2PC.setTabletTracking(True)
        self.clipD2PC.setAutoFillBackground(False)
        self.clipD2PC.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/copy-document.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clipD2PC.setIcon(icon5)
        self.clipD2PC.setFlat(True)

        self.verticalLayout.addWidget(self.clipD2PC)

        self.clipPC2D = QPushButton(self.layoutWidget)
        self.clipPC2D.setObjectName(u"clipPC2D")
        self.clipPC2D.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.clipPC2D.sizePolicy().hasHeightForWidth())
        self.clipPC2D.setSizePolicy(sizePolicy1)
        self.clipPC2D.setMouseTracking(True)
        self.clipPC2D.setTabletTracking(True)
        self.clipPC2D.setAutoFillBackground(False)
        self.clipPC2D.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/copy-document(1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clipPC2D.setIcon(icon6)
        self.clipPC2D.setFlat(True)

        self.verticalLayout.addWidget(self.clipPC2D)

        self.vup = QPushButton(self.layoutWidget)
        self.vup.setObjectName(u"vup")
        self.vup.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.vup.sizePolicy().hasHeightForWidth())
        self.vup.setSizePolicy(sizePolicy1)
        self.vup.setMouseTracking(True)
        self.vup.setTabletTracking(True)
        self.vup.setAutoFillBackground(False)
        self.vup.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/volume-up-interface-symbol.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vup.setIcon(icon7)
        self.vup.setFlat(True)

        self.verticalLayout.addWidget(self.vup)

        self.vdown = QPushButton(self.layoutWidget)
        self.vdown.setObjectName(u"vdown")
        self.vdown.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.vdown.sizePolicy().hasHeightForWidth())
        self.vdown.setSizePolicy(sizePolicy1)
        self.vdown.setMouseTracking(True)
        self.vdown.setTabletTracking(True)
        self.vdown.setAutoFillBackground(False)
        self.vdown.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/reduced-volume.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vdown.setIcon(icon8)
        self.vdown.setFlat(True)

        self.verticalLayout.addWidget(self.vdown)

        self.powerUI = QPushButton(self.layoutWidget)
        self.powerUI.setObjectName(u"powerUI")
        self.powerUI.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.powerUI.sizePolicy().hasHeightForWidth())
        self.powerUI.setSizePolicy(sizePolicy1)
        self.powerUI.setMouseTracking(True)
        self.powerUI.setTabletTracking(True)
        self.powerUI.setAutoFillBackground(False)
        self.powerUI.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/power.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.powerUI.setIcon(icon9)
        self.powerUI.setIconSize(QSize(16, 16))
        self.powerUI.setCheckable(False)
        self.powerUI.setFlat(True)

        self.verticalLayout.addWidget(self.powerUI)

        self.home = QPushButton(self.layoutWidget)
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy1)
        self.home.setMouseTracking(True)
        self.home.setTabletTracking(True)
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home.setIcon(icon10)
        self.home.setFlat(True)

        self.verticalLayout.addWidget(self.home)

        self.back = QPushButton(self.layoutWidget)
        self.back.setObjectName(u"back")
        self.back.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.back.sizePolicy().hasHeightForWidth())
        self.back.setSizePolicy(sizePolicy1)
        self.back.setMouseTracking(True)
        self.back.setTabletTracking(True)
        self.back.setAutoFillBackground(False)
        self.back.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/chevron-sign-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.back.setIcon(icon11)
        self.back.setFlat(True)

        self.verticalLayout.addWidget(self.back)

        self.menuUI = QPushButton(self.layoutWidget)
        self.menuUI.setObjectName(u"menuUI")
        self.menuUI.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.menuUI.sizePolicy().hasHeightForWidth())
        self.menuUI.setSizePolicy(sizePolicy1)
        self.menuUI.setMouseTracking(True)
        self.menuUI.setTabletTracking(True)
        self.menuUI.setAutoFillBackground(False)
        self.menuUI.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/reorder-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuUI.setIcon(icon12)
        self.menuUI.setFlat(True)

        self.verticalLayout.addWidget(self.menuUI)

        self.appswi = QPushButton(self.layoutWidget)
        self.appswi.setObjectName(u"appswi")
        self.appswi.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.appswi.sizePolicy().hasHeightForWidth())
        self.appswi.setSizePolicy(sizePolicy1)
        self.appswi.setMouseTracking(True)
        self.appswi.setTabletTracking(True)
        self.appswi.setAutoFillBackground(False)
        self.appswi.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/four-black-squares.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.appswi.setIcon(icon13)
        self.appswi.setFlat(True)

        self.verticalLayout.addWidget(self.appswi)

        self.pinchinUI = QPushButton(self.layoutWidget)
        self.pinchinUI.setObjectName(u"pinchinUI")
        self.pinchinUI.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pinchinUI.sizePolicy().hasHeightForWidth())
        self.pinchinUI.setSizePolicy(sizePolicy1)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pinchinUI.setIcon(icon14)
        self.pinchinUI.setFlat(True)

        self.verticalLayout.addWidget(self.pinchinUI)

        self.pinchoutUI = QPushButton(self.layoutWidget)
        self.pinchoutUI.setObjectName(u"pinchoutUI")
        self.pinchoutUI.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pinchoutUI.sizePolicy().hasHeightForWidth())
        self.pinchoutUI.setSizePolicy(sizePolicy1)
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pinchoutUI.setIcon(icon15)
        self.pinchoutUI.setFlat(True)

        self.verticalLayout.addWidget(self.pinchoutUI)

        self.potraitUI = QPushButton(self.layoutWidget)
        self.potraitUI.setObjectName(u"potraitUI")
        self.potraitUI.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.potraitUI.sizePolicy().hasHeightForWidth())
        self.potraitUI.setSizePolicy(sizePolicy1)
        self.potraitUI.setToolTipDuration(2)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/vertical-resizing-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.potraitUI.setIcon(icon16)
        self.potraitUI.setFlat(True)

        self.verticalLayout.addWidget(self.potraitUI)

        self.landscapeUI = QPushButton(self.layoutWidget)
        self.landscapeUI.setObjectName(u"landscapeUI")
        self.landscapeUI.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.landscapeUI.sizePolicy().hasHeightForWidth())
        self.landscapeUI.setSizePolicy(sizePolicy1)
        self.landscapeUI.setToolTipDuration(2)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/horizontal-resize-option.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.landscapeUI.setIcon(icon17)
        self.landscapeUI.setFlat(True)

        self.verticalLayout.addWidget(self.landscapeUI)

        self.tk_device_id = QPushButton(self.layoutWidget)
        self.tk_device_id.setObjectName(u"tk_device_id")
        self.tk_device_id.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.tk_device_id.sizePolicy().hasHeightForWidth())
        self.tk_device_id.setSizePolicy(sizePolicy1)
        self.tk_device_id.setMinimumSize(QSize(0, 2))
        self.tk_device_id.setMaximumSize(QSize(16777215, 20))
        self.tk_device_id.setToolTipDuration(2)
        self.tk_device_id.setFlat(True)

        self.verticalLayout.addWidget(self.tk_device_id)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(ToolbarPanel)

        QMetaObject.connectSlotsByName(ToolbarPanel)
    # setupUi

    def retranslateUi(self, ToolbarPanel):
        self.screenfreeze.setText("")
#if QT_CONFIG(tooltip)
        self.fullscreenUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Fullscreen", None))
#endif // QT_CONFIG(tooltip)
        self.fullscreenUI.setText("")
#if QT_CONFIG(tooltip)
        self.notif_pull.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Expand notification panel", None))
#endif // QT_CONFIG(tooltip)
        self.notif_pull.setText("")
#if QT_CONFIG(tooltip)
        self.notif_collapse.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Expand notification panel", None))
#endif // QT_CONFIG(tooltip)
        self.notif_collapse.setText("")
#if QT_CONFIG(tooltip)
        self.clipD2PC.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Copy device clipbioard to PC", None))
#endif // QT_CONFIG(tooltip)
        self.clipD2PC.setText("")
#if QT_CONFIG(tooltip)
        self.clipPC2D.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Copy PC clipboard to Device", None))
#endif // QT_CONFIG(tooltip)
        self.clipPC2D.setText("")
#if QT_CONFIG(tooltip)
        self.vup.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Volume Up", None))
#endif // QT_CONFIG(tooltip)
        self.vup.setText("")
        self.vdown.setText("")
#if QT_CONFIG(tooltip)
        self.powerUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Power on/off", None))
#endif // QT_CONFIG(tooltip)
        self.powerUI.setText("")
#if QT_CONFIG(tooltip)
        self.home.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Home key", None))
#endif // QT_CONFIG(tooltip)
        self.home.setText("")
#if QT_CONFIG(tooltip)
        self.back.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Back key", None))
#endif // QT_CONFIG(tooltip)
        self.back.setText("")
#if QT_CONFIG(tooltip)
        self.menuUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Menu key", None))
#endif // QT_CONFIG(tooltip)
        self.menuUI.setText("")
#if QT_CONFIG(tooltip)
        self.appswi.setToolTip(QCoreApplication.translate("ToolbarPanel", u"press the APP_SWITCH button", None))
#endif // QT_CONFIG(tooltip)
        self.appswi.setText("")
#if QT_CONFIG(tooltip)
        self.pinchinUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Pinch in the screen", None))
#endif // QT_CONFIG(tooltip)
        self.pinchinUI.setStyleSheet("")
        self.pinchinUI.setText("")
#if QT_CONFIG(tooltip)
        self.pinchoutUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Pinch out in the screen", None))
#endif // QT_CONFIG(tooltip)
        self.pinchoutUI.setStyleSheet("")
        self.pinchoutUI.setText("")
#if QT_CONFIG(tooltip)
        self.potraitUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Potrait", None))
#endif // QT_CONFIG(tooltip)
        self.potraitUI.setStyleSheet("")
        self.potraitUI.setText("")
#if QT_CONFIG(tooltip)
        self.landscapeUI.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Landscape", None))
#endif // QT_CONFIG(tooltip)
        self.landscapeUI.setStyleSheet("")
        self.landscapeUI.setText("")
#if QT_CONFIG(tooltip)
        self.tk_device_id.setToolTip(QCoreApplication.translate("ToolbarPanel", u"Landscape", None))
#endif // QT_CONFIG(tooltip)
        self.tk_device_id.setStyleSheet("")
        self.tk_device_id.setText("")
        self.label_2.setText(QCoreApplication.translate("ToolbarPanel", u"....", None))
        self.label.setText(QCoreApplication.translate("ToolbarPanel", u"::::", None))
        pass
    # retranslateUi


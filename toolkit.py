import os
import sys
import time

try:
    from PyQt4 import QtCore, QtGui, uic
except ModuleNotFoundError:
    print("PyQt4 is not installed. Please install it with pip install PyQt5 pyside2."
          "Read the README.md on github.com/srevinsaju/guiscrcpy")
try:
    import pyautogui as auto
except ModuleNotFoundError:
    print("PyAutoGUI is not installed. Please install it with pip install pyautogui."
          "Read the README.md on github.com/srevinsaju/guiscrcpy")
try:
    from pygetwindow import getWindowsWithTitle
except NotImplementedError:
    pass

qtCreatorFile = "toolkit_ui.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def clipd2pc():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "c")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+c")


def power():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "p")
    except NameError:
        os.system("wmctrl -x -a scrcpy && xdotool keydown --clearmodifiers ctrl")
        os.system("wmctrl -x -a scrcpy && xdotool keydown ctrl+P")

        # os.system("wmctrl -x -a scrcpy && xdotool keydown --clearmodifiers ctrl+h sleep 0.1 keyup ctrl+h")
        # os.system("xdotool key --clearmodifiers ctrl+h")
        time.sleep(0.1)
        os.system("xdotool key --clearmodifiers BackSpace")


def menu():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "m")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+m")


def Back():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "b")
    except NameError:
        os.system("wmctrl -x -a scrcpy && xdotool keydown --clearmodifiers ctrl")
        os.system("wmctrl -x -a scrcpy && xdotool keydown ctrl+B")

        # os.system("wmctrl -x -a scrcpy && xdotool keydown --clearmodifiers ctrl+h sleep 0.1 keyup ctrl+h")
        # os.system("xdotool key --clearmodifiers ctrl+h")
        time.sleep(0.1)
        os.system("xdotool key --clearmodifiers BackSpace")


def homekey():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "h")
    except NameError:
        os.system("wmctrl -x -a scrcpy && xdotool keydown --clearmodifiers ctrl")
        os.system("wmctrl -x -a scrcpy && xdotool keydown ctrl+h")

        # os.system("wmctrl -x -a scrcpy && xdotool keydown --clearmodifiers ctrl+h sleep 0.1 keyup ctrl+h")
        # os.system("xdotool key --clearmodifiers ctrl+h")
        time.sleep(0.1)
        os.system("wmctrl -x -a scrcpy && xdotool keyup ctrl+h")
        os.system("xdotool key --clearmodifiers ctrl")


def switch():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "s")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+s")
    except ModuleNotFoundError:
        print("please Install the dependencies")


def notifExpand():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "n")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+n")


def clippc2d():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "shift", "c")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+shift+c")


def fullscreen():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "f")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+f")


class MyAppv(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.clipD2PC.released.connect(clipd2pc)
        self.clipPC2D.released.connect(clippc2d)
        self.back.released.connect(Back)
        self.appswi.released.connect(switch)
        self.menuUI.released.connect(menu)
        self.home.released.connect(homekey)
        self.notif_pull.released.connect(notifExpand)
        self.fullscreenUI.released.connect(fullscreen)


appo = QtGui.QApplication(sys.argv)
window = MyAppv()
window.show()
sys.exit(appo.exec_())

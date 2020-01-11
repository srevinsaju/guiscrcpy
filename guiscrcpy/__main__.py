#!/usr/bin/env python3

"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy
Licensed under GNU Public License

Icon made by Dave Gandy from www.flaticon.com used under
Creative Commons 3.0 Unported. The original SVG black work
by Dave Gandy has ben re-oriented, flipped or color-changed.
The rest of Terms and Conditions put formward by
CC-3.0:Unported has been feverently followed by the developer.
Icons have been adapeted in all the three windows.

Icons pack obtained from www.flaticon.com
All rights reserved.

"""

# Prelaunch
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
import qdarkstyle
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import json
import sys
import platform
import argparse
import time
from subprocess import PIPE
from subprocess import Popen as po, STDOUT
import os
import os.path
from subprocess import PIPE, Popen
from pynput import keyboard
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

__version__ = '2.0.0-raw'
sha = None
try:
    import git
    try:
        repo = git.Repo(search_parent_directories=True)
        sha = "-" + repo.head.object.hexsha
        __version__ = repo.git.describe("--tags")
    except BaseException:
        print("LOG: This is not running from Source. No git sha retrievable")
        print("LOG: Extracting version number from pip")
        try:
            import pkg_resources
            __version__ = pkg_resources.get_distribution(
                "guiscrcpy").version
        except BaseException:
            print("LOG: guiscrcpy not installed as pip package." +
                  "Version retrieve failed.")
            
except ModuleNotFoundError:
    print(
        "ERR: gitpython is not found. It is not a dependency,"
        " but you can optionally install it "
        "with python3 -m pip install gitpython"
        )
if sha:
    build = __version__ + " by srevinsaju"
else:
    build = __version__ + " by srevinsaju"

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--install', action='store_true',
                    help="Install guiscrcpy system wide on Linux")
parser.add_argument('-s', '--start', action='store_true',
                    help="Start scrcpy first before loading the GUI")
parser.add_argument(
    '-v',
    '--version',
    action='store_true',
    help="Display guiscrcpy version")

# parser.add_argument('-b', '--bar-value', default=3.14)

args = parser.parse_args()
print("LOG: Received flag", args.start)

os.chdir(os.path.dirname(__file__))


class bcolors:
    if platform.system() == "Linux":
        HEADER = "\033[95m"
        OKBLUE = "\033[94m"
        OKGREEN = "\033[92m"
        WARNING = "\033[93m"
        FAIL = "\033[91mERR:"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
    else:
        HEADER = ""
        OKBLUE = ""
        OKGREEN = ""
        WARNING = ""
        FAIL = "ERR:"
        ENDC = ""
        BOLD = ""
        UNDERLINE = ""


# import pdb
# removed multiprocess modules

if not sha:
    commit1 = __version__
else:
    commit1 = __version__ + " commit" + sha

print(
    bcolors.UNDERLINE +
    "                                  " +
    bcolors.ENDC)
print()
print("guiscrcpy")
print("by srevinsaju")
print(bcolors.OKBLUE + commit1 + bcolors.ENDC)
print(
    bcolors.OKBLUE +
    "Licensed under GNU GPL v3 (c) 2019  " +
    bcolors.ENDC)
print(
    bcolors.UNDERLINE +
    "                                  " +
    bcolors.ENDC)
print(bcolors.OKBLUE + "" + bcolors.ENDC)

# chk version argument given or not
if(args.version):
    sys.exit(0)
# chk install value given
if(args.install):
    if platform.system() == "Linux":
        # print("Supported on Linux only")

        import subprocess
        inf = subprocess.Popen(
            "find .. -iname 'guiscrcpy-src-installer.sh'",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        a1 = inf.stdout.read().decode("utf-8")
        dirch = a1[:a1.find("guiscrcpy-src-installer.sh")]
        cmd = "cd " + dirch + " ; " + "./guiscrcpy-src-installer.sh"
        os.system(cmd)
        sys.exit()
    else:
        print("Installation supported on Linux only")
        sys.exit()


print()
print(
    "MSG: Please ensure you have enabled",
    bcolors.OKGREEN + "USB Debugging" + bcolors.ENDC,
    "on your device. See README.md for more details",
)
# print("LOG: Current Working Directory >> ", os.getcwd())
# print('LOG: __file__ name             >> ', str(__file__))
# print("LOG: os.path Absolute Path     >> ", os.path.abspath(__file__))
print("LOG: Current Working Directory", os.getcwd())

print("")


# ******************************
# CONFIGURATION FILE CHECKER
# *****************************
# Pre declare variable for handlin NameError, AttributeError exception
config = {
    'dimension': None,
    'swtouches': False,
    'bitrate': 8000,
    'fullscreen': False,
    'dispRO': False,
    'extra': ""}
dimension0 = None
dimension = None
swtouches0 = "False"
bitrate0 = 8000
fullscreen0 = "False"
dispRO0 = "False"
jsonf = 'guiscrcpy.json'
# Declare Config path position
if (platform.system() == 'Windows'):
    cfgpath = os.path.expanduser("~/AppData/Local/guiscrcpy/")
else:
    if (os.getenv('XDG_CONFIG_HOME') is None):
        cfgpath = os.path.expanduser("~/.config/guiscrcpy/")
    else:
        cfgpath = os.getenv('XDG_CONFIG_HOME').split(":")[0]+"/guiscrcpy"
        

try:
    with open(cfgpath + jsonf, 'r') as f:
        config = json.load(f)
    fileExist = True
    print("LOG: Configuration file found in ", cfgpath, " directory")

except FileNotFoundError:

    print("LOG: Initializing guiscrcpy for first time use...")
    try:
        os.makedirs(cfgpath)
    except FileExistsError:
        print("LOG: Folder guiscrcpy aldready exists.")
    with open(cfgpath + jsonf, 'w') as f:
        json.dump(config, f)

    print("LOG: Configuration file created in ", cfgpath, " directory")
    fileExist = False

    if platform.system() == "Windows":
        print(
            "LOG: Detected a Windows Operating System :: ",
            platform.release(),
            platform.version(),
        )
        pass
    elif platform.system() == "Linux":

        print(
            "LOG: Detected a Linux Operating System :: ",
            platform.release(),
            platform.version(),
        )
        print("LOG: Installing Trebuchet MS font ...")
        os.system("mkdir ~/.fonts/")
        os.system("cp -r fonts/* ~/.fonts/")

    else:
        print(
            bcolors.FAIL,
            " MacOS :: Untested OS detected. Continuing >>> " +
            bcolors.ENDC,
        )
        pass

if not fileExist:

    # Init json file for first time use
    config = {
        'dimension': None,
        'swtouches': False,
        'bitrate': 8000,
        'fullscreen': False,
        'dispRO': False,
        'extra': ""}
    with open(cfgpath + jsonf, 'w') as f:
        json.dump(config, f)


elif fileExist:
    with open(cfgpath + jsonf, 'r') as f:
        config = json.load(f)

    """
    try:
        bitrate0 = a[4].strip("\n")
    except IndexError:
        bitrate0 = 8000
    try:
        dimension0 = a[5].strip("\n")
    except IndexError:
        dimension0 = None
    try:
        fullscreen0 = a[7].strip("\n")
    except IndexError:
        fullscreen0 = "False"
    try:
        swtouches0 = a[6].strip("\n")
    except IndexError:
        swtouches0 = "False"

    try:
        dispRO0 = a[8].strip("\n")
        # print("SUCCESS dispRO")
    except IndexError:
        dispRO0 = "False"
        # print("FAILED dispRO")
    """
    # print("LOG: Bitrate : ", bitrate0, " + Dimensions", dimension0, "")
    # print("LOG: Bitrate: ", bitrate0)
    # print("dispRO:", dispRO0)

if platform.system() == "Windows":
    if os.path.isfile("./scrcpy.exe"):
        increment = ".\\"
        # print(bcolors.BOLD + "LOG: Found scrcpy.exe in current directory.")
    else:
        print(
            bcolors.FAIL
            + " Found scrcpy.exe not found in current directory."
            + bcolors.ENDC
        )
        print(
            bcolors.BOLD +
            "LOG: Fallback to system PATH variable."+
            "Please add scrcpy to path." +
            bcolors.ENDC)
        increment = ""


else:
    if not fileExist:
        print(
            "LOG: One time checking for scrcpy executable." +
            "(Use RESET for rechecking)"
        )
        increment = ""
        scrcpy_checker = po(
            "scrcpy -v",
            stdout=PIPE,
            stderr=PIPE,
            shell=True)
        if scrcpy_checker.stderr.read().decode("utf-8").find("not found") != -1:
            print(
                bcolors.FAIL +
                " Failed to find scrcpy on path. 'Start Scrcpy' may not work" +
                bcolors.ENDC)
        else:
            print(
                "LOG: Scrcpy found " +
                scrcpy_checker.stdout.read().decode("utf-8"))

    else:
        increment = ""


# ***************************
# BEGIN ENGIN CODE
# ***************************

def invokeScrcpy():
    optPass = ""

    optPass += " -b " + str(config['bitrate'])
    if(config['fullscreen']):
        optPass += " -f "
    if(config['swtouches']):
        optPass += " -t "
    if(config['dispRO']):
        optPass += " --turn-screen-off "
    backup0r = po(
        increment + "scrcpy " + str(optPass),
        shell=True,
        stdin=PIPE,
        stdout=PIPE,
        stderr=STDOUT,
    )
    print("LOG: ", backup0r.stdout)

# ******************************


if (args.start):
    print("RUNNING SCRCPY DIRECTLY")
    invokeScrcpy()


print("LOG: Importing modules...")


try:
    from .mainui import Ui_MainWindow
except (ModuleNotFoundError, ImportError):
    try:
    
        from guiscrcpy.mainui import Ui_MainWindow

        print("LOG: Safe submodule import of mainui")
    except Exception as e:

        print(
            "ERR: An Error with Code: {c} has occured explicitly, {m}. Please report to https://github.com/srevinsaju/guiscrcpy/issues".format(
                c=type(e).__name__,
                m=str(e)))


# from bottompanelUI import Ui_Panel
# import breeze_resources
# from toolUI import Ui_Dialog
try:
    import psutil
except ModuleNotFoundError:
    print(
        "WARNING : psutil is not installed in the python3 directory. "
        "Install with \n $ pip3 install psutil"
    )

# Uncomment this if you would like to test experimental features
"""
try:
    import pyautogui as auto
except ModuleNotFoundError:
    print("PyAutoGUI is not installed. Please install it with pip install pyautogui."
          "Read the README.md on github.com/srevinsaju/guiscrcpy. \n You might want to continue without "
          "pyAutoGUI limited functionality")
try:
    from pygetwindow import getWindowsWithTitle
except NotImplementedError:
    pass
"""


# BEGIN TOOLKIT.UI


def clipd2pc():
    print(
        "WARNING : Copy device to PC is implemented only in source code due to "
        "its development stage")
    print(" If you are a developer, uncomment the import statements of PyAutoGui")
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "c")
    except NameError:
        os.system(
            "wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+c")


def power():
    print("LOG: Passing POWER")
    po(
        increment +
        "adb shell input keyevent 26",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)


def menu():
    print("LOG: Passing MENU")
    adb_menu = po(
        increment +
        "adb shell input keyevent 82",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)


def Back():
    print("LOG: Passing BACK")
    adb_back = po(
        increment +
        "adb shell input keyevent 4",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)


def volUP():
    print("LOG: Passing BACK")
    adb_back = po(
        increment +
        "adb shell input keyevent 24",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)


def volDN():
    print("LOG: Passing BACK")
    adb_back = po(
        increment +
        "adb shell input keyevent 25",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)


def homekey():
    print("LOG: Passing HOME")
    adb_home = po(
        increment +
        "adb shell input keyevent 3",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)


def switch():
    print("LOG: Passing APP_SWITCH")
    adb_home = po(
        increment + "adb shell input keyevent KEYCODE_APP_SWITCH",
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
    )


def reorientP():
    print("LOG: Passing REORIENT [POTRAIT]")
    adb_reo = po(
        increment +
        "adb shell settings put system accelerometer_rotation 0",
        shell=True)

    adb_reosl = po(
        increment +
        " adb shell settings put system rotation 1",
        shell=True)


def reorientL():
    print("LOG: Passing REORIENT [LANDSCAPE]")
    adb_reoo = po(
        increment +
        "adb shell settings put system accelerometer_rotation 0",
        shell=True)
    adb_reool = po(
        increment +
        " adb shell settings put system rotation 1",
        shell=True)


def notifExpand():
    print("LOG: Passing NOTIF EXPAND")
    adb_dim = po(
        increment +
        "adb shell wm size",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)
    out = adb_dim.stdout.read()
    out_decoded = out.decode("utf-8")
    out_decoded = out_decoded[:-1]
    dimVal = out_decoded.split(": ")
    dimensions_ = dimVal[1]
    dimValues = dimensions_.split("x")
    adb_pull = po(
        increment + "adb shell input swipe 0 0 0 " + str(int(dimValues[1]) - 1),
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
    )


def notifCollapse():
    print("LOG: Passing NOTIF COLLAPSE")
    adb_dim = po(
        increment +
        "adb shell wm size",
        shell=True,
        stdout=PIPE,
        stderr=PIPE)
    out = adb_dim.stdout.read()
    out_decoded = out.decode("utf-8")
    out_decoded = out_decoded[:-1]
    dimVal = out_decoded.split(": ")
    dimensions_ = dimVal[1]
    dimValues = dimensions_.split("x")
    adb_pull = po(
        increment + "adb shell input swipe 0 " + str(int(dimValues[1]) - 1) + " 0 0",
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
    )


def clippc2d():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "shift", "c")
        print("E: NOT SUPPORTED ON WINDOWS")
    except NameError:
        os.system(
            "wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+shift+c")


def fullscreen():
    print(
        bcolors.FAIL +
        " Fullscreen button is not currently supported on Binary due to safety reasons" +
        bcolors.ENDC)
    print("If you are in")
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "f")
    except NameError:
        os.system(
            "wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+f")


class MyAppv(QMainWindow):
    def __init__(self):
        self.oldPos = None
        super(MyAppv, self).__init__()
        # Ui_Dialog.__init__(self)
        # print("Class entered : MyAppv")
        self.setObjectName("Dialog")
        self.resize(30, 461)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(30, 340))
        self.setMaximumSize(QtCore.QSize(104, 600))
        self.setBaseSize(QtCore.QSize(30, 403))
        self.setWindowTitle("guiscrcpy")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setWindowOpacity(1.0)
        self.setStyleSheet(
            "QDialog{\n"
            "width: 30px\n"
            "}\n"
            "QPushButton {\n"
            "                        \n"
            "\n"
            "border-radius: 1px;\n"
            "        background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        \n"
            "                    }\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "QPushButton:hover {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "")
        self.notif_collapse = QtWidgets.QPushButton(self)
        self.notif_collapse.setEnabled(True)
        self.notif_collapse.setGeometry(QtCore.QRect(0, 75, 30, 25))
        self.notif_collapse.setMouseTracking(True)
        # self.notif_collapse.setTabletTracking(True)
        self.notif_collapse.setAutoFillBackground(False)
        self.notif_collapse.setStyleSheet("")
        self.notif_collapse.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/bell-musical-tool(2).svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.notif_collapse.setIcon(icon1)
        self.notif_collapse.setFlat(True)
        self.notif_collapse.setObjectName("notif_collapse")
        self.menuUI = QtWidgets.QPushButton(self)
        self.menuUI.setEnabled(True)
        self.menuUI.setGeometry(QtCore.QRect(0, 275, 30, 25))
        self.menuUI.setMouseTracking(True)
        # self.menuUI.setTabletTracking(True)
        self.menuUI.setAutoFillBackground(False)
        self.menuUI.setStyleSheet("")
        self.menuUI.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/reorder-option.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.menuUI.setIcon(icon2)
        self.menuUI.setFlat(True)
        self.menuUI.setObjectName("menuUI")
        self.appswi = QtWidgets.QPushButton(self)
        self.appswi.setEnabled(True)
        self.appswi.setGeometry(QtCore.QRect(0, 300, 30, 25))
        self.appswi.setMouseTracking(True)
        # self.appswi.setTabletTracking(True)
        self.appswi.setAutoFillBackground(False)
        self.appswi.setStyleSheet("")
        self.appswi.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/four-black-squares.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.appswi.setIcon(icon3)
        self.appswi.setFlat(True)
        self.appswi.setObjectName("appswi")
        self.pinchoutUI = QtWidgets.QPushButton(self)
        self.pinchoutUI.setEnabled(False)
        self.pinchoutUI.setGeometry(QtCore.QRect(0, 350, 30, 25))
        self.pinchoutUI.setStyleSheet("")
        self.pinchoutUI.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/zoom-out.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pinchoutUI.setIcon(icon4)
        self.pinchoutUI.setFlat(True)
        self.pinchoutUI.setObjectName("pinchoutUI")
        self.screenfreeze = QtWidgets.QPushButton(self)
        self.screenfreeze.setEnabled(True)
        self.screenfreeze.setGeometry(QtCore.QRect(0, 0, 30, 25))
        self.screenfreeze.setMouseTracking(True)
        # self.screenfreeze.setTabletTracking(True)
        self.screenfreeze.setAutoFillBackground(False)
        self.screenfreeze.setStyleSheet("")
        self.screenfreeze.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/icons/icons/cross-mark-on-a-black-circle-background.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.screenfreeze.setIcon(icon5)
        self.screenfreeze.setFlat(True)
        self.screenfreeze.setObjectName("screenfreeze")
        self.back = QtWidgets.QPushButton(self)
        self.back.setEnabled(True)
        self.back.setGeometry(QtCore.QRect(0, 250, 30, 25))
        self.back.setMouseTracking(True)
        # self.back.setTabletTracking(True)
        self.back.setAutoFillBackground(False)
        self.back.setStyleSheet("")
        self.back.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.back.setIcon(icon6)
        self.back.setFlat(True)
        self.back.setObjectName("back")
        self.notif_pull = QtWidgets.QPushButton(self)
        self.notif_pull.setEnabled(True)
        self.notif_pull.setGeometry(QtCore.QRect(0, 50, 30, 25))
        self.notif_pull.setMouseTracking(True)
        # self.notif_pull.setTabletTracking(True)
        self.notif_pull.setAutoFillBackground(False)
        self.notif_pull.setStyleSheet("")
        self.notif_pull.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/icons/icons/bell-musical-tool.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.notif_pull.setIcon(icon7)
        self.notif_pull.setFlat(True)
        self.notif_pull.setObjectName("notif_pull")
        self.powerUI = QtWidgets.QPushButton(self)
        self.powerUI.setEnabled(True)
        self.powerUI.setGeometry(QtCore.QRect(0, 200, 30, 25))
        self.powerUI.setMouseTracking(True)
        # self.powerUI.setTabletTracking(True)
        self.powerUI.setAutoFillBackground(False)
        self.powerUI.setStyleSheet("")
        self.powerUI.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/icons/icons/power.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.powerUI.setIcon(icon8)
        self.powerUI.setIconSize(QtCore.QSize(16, 16))
        self.powerUI.setCheckable(False)
        self.powerUI.setFlat(True)
        self.powerUI.setObjectName("powerUI")
        self.pinchinUI = QtWidgets.QPushButton(self)
        self.pinchinUI.setEnabled(False)
        self.pinchinUI.setGeometry(QtCore.QRect(0, 325, 30, 25))
        self.pinchinUI.setStyleSheet("")
        self.pinchinUI.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/icons/icons/zoom-in.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pinchinUI.setIcon(icon9)
        self.pinchinUI.setFlat(True)
        self.pinchinUI.setObjectName("pinchinUI")
        self.clipD2PC = QtWidgets.QPushButton(self)
        self.clipD2PC.setEnabled(True)
        self.clipD2PC.setGeometry(QtCore.QRect(0, 100, 30, 25))
        self.clipD2PC.setMouseTracking(True)
        # self.clipD2PC.setTabletTracking(True)
        self.clipD2PC.setAutoFillBackground(False)
        self.clipD2PC.setStyleSheet("")
        self.clipD2PC.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/icons/icons/copy-document.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.clipD2PC.setIcon(icon10)
        self.clipD2PC.setFlat(True)
        self.clipD2PC.setObjectName("clipD2PC")
        self.potraitUI = QtWidgets.QPushButton(self)
        self.potraitUI.setEnabled(True)
        self.potraitUI.setGeometry(QtCore.QRect(0, 375, 30, 25))

        self.potraitUI.setStyleSheet("")
        self.potraitUI.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/icons/icons/vertical-resizing-option.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.potraitUI.setIcon(icon11)
        self.potraitUI.setFlat(True)
        self.potraitUI.setObjectName("potraitUI")
        self.landscapeUI = QtWidgets.QPushButton(self)
        self.landscapeUI.setEnabled(True)
        self.landscapeUI.setGeometry(QtCore.QRect(0, 400, 30, 25))

        self.landscapeUI.setStyleSheet("")
        self.landscapeUI.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/icons/icons/horizontal-resize-option.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.landscapeUI.setIcon(icon12)
        self.landscapeUI.setFlat(True)
        self.landscapeUI.setObjectName("landscapeUI")
        self.home = QtWidgets.QPushButton(self)
        self.home.setEnabled(True)
        self.home.setGeometry(QtCore.QRect(0, 225, 30, 25))
        self.home.setMouseTracking(True)
        # self.home.setTabletTracking(True)
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet("")
        self.home.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(":/icons/icons/home.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.home.setIcon(icon13)
        self.home.setFlat(True)
        self.home.setObjectName("home")
        self.vup = QtWidgets.QPushButton(self)
        self.vup.setEnabled(True)
        self.vup.setGeometry(QtCore.QRect(0, 150, 30, 25))
        self.vup.setMouseTracking(True)
        # self.vup.setTabletTracking(True)
        self.vup.setAutoFillBackground(False)
        self.vup.setStyleSheet("")
        self.vup.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap(":/icons/icons/volume-up-interface-symbol.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.vup.setIcon(icon14)
        self.vup.setFlat(True)
        self.vup.setObjectName("vup")
        self.vdown = QtWidgets.QPushButton(self)
        self.vdown.setEnabled(True)
        self.vdown.setGeometry(QtCore.QRect(0, 175, 30, 25))
        self.vdown.setMouseTracking(True)
        # self.vdown.setTabletTracking(True)
        self.vdown.setAutoFillBackground(False)
        self.vdown.setStyleSheet("")
        self.vdown.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap(":/icons/icons/reduced-volume.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.vdown.setIcon(icon15)
        self.vdown.setFlat(True)
        self.vdown.setObjectName("vdown")
        self.fullscreenUI = QtWidgets.QPushButton(self)
        self.fullscreenUI.setEnabled(True)
        self.fullscreenUI.setGeometry(QtCore.QRect(0, 25, 30, 25))
        self.fullscreenUI.setMouseTracking(True)
        # self.fullscreenUI.setTabletTracking(True)
        self.fullscreenUI.setAutoFillBackground(False)
        self.fullscreenUI.setStyleSheet("")
        self.fullscreenUI.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
            QtGui.QPixmap(":/icons/icons/increase-size-option.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.fullscreenUI.setIcon(icon16)
        self.fullscreenUI.setFlat(True)
        self.fullscreenUI.setObjectName("fullscreenUI")
        self.clipPC2D = QtWidgets.QPushButton(self)
        self.clipPC2D.setEnabled(True)
        self.clipPC2D.setGeometry(QtCore.QRect(0, 125, 30, 25))
        self.clipPC2D.setMouseTracking(True)
        # self.clipPC2D.setTabletTracking(True)
        self.clipPC2D.setAutoFillBackground(False)
        self.clipPC2D.setStyleSheet("")
        self.clipPC2D.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap(":/icons/icons/copy-document(1).svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.clipPC2D.setIcon(icon17)
        self.clipPC2D.setFlat(True)
        self.clipPC2D.setObjectName("clipPC2D")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 410, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(0, 420, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.notif_collapse.raise_()
        self.menuUI.raise_()
        self.appswi.raise_()
        self.pinchoutUI.raise_()
        self.screenfreeze.raise_()
        self.back.raise_()
        self.notif_pull.raise_()
        self.powerUI.raise_()
        self.pinchinUI.raise_()
        self.clipD2PC.raise_()
        self.potraitUI.raise_()
        self.home.raise_()
        self.vup.raise_()
        self.vdown.raise_()
        self.fullscreenUI.raise_()
        self.clipPC2D.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.landscapeUI.raise_()

        _translate = QtCore.QCoreApplication.translate
        self.notif_collapse.setToolTip(
            _translate("self", "Expand notification panel"))
        self.menuUI.setToolTip(_translate("self", "Menu key"))
        self.appswi.setToolTip(
            _translate(
                "self",
                "press the APP_SWITCH button"))
        self.pinchoutUI.setToolTip(_translate(
            "self", "Pinch out in the screen"))
        self.back.setToolTip(_translate("self", "Back key"))
        self.notif_pull.setToolTip(_translate(
            "self", "Expand notification panel"))
        self.powerUI.setToolTip(_translate("self", "Power on/off"))
        self.pinchinUI.setToolTip(
            _translate("self", "Pinch in the screen"))
        self.clipD2PC.setToolTip(
            _translate(
                "self",
                "Copy device clipbioard to PC"))
        self.potraitUI.setToolTip(_translate("self", "Potrait"))
        self.landscapeUI.setToolTip(_translate("self", "Landscape"))
        self.home.setToolTip(_translate("self", "Home key"))
        self.vup.setToolTip(_translate("self", "Volume Up"))
        self.fullscreenUI.setToolTip(_translate("self", "Fullscreen"))
        self.clipPC2D.setToolTip(
            _translate(
                "self",
                "Copy PC clipboard to Device"))
        self.label.setText(_translate("self", "...."))
        self.label_2.setText(_translate("self", "...."))
        # -----------------------------------

        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )
        # self.setupUi(Dialog)
        self.clipD2PC.clicked.connect(clipd2pc)
        self.clipPC2D.clicked.connect(clippc2d)
        self.back.clicked.connect(Back)
        self.screenfreeze.clicked.connect(self.quitn)
        self.appswi.clicked.connect(switch)
        self.menuUI.clicked.connect(menu)
        self.home.clicked.connect(homekey)
        self.notif_pull.clicked.connect(notifExpand)
        self.notif_collapse.clicked.connect(notifCollapse)
        self.fullscreenUI.clicked.connect(fullscreen)
        self.powerUI.clicked.connect(power)
        self.vup.clicked.connect(volUP)
        self.vdown.clicked.connect(volDN)
        self.potraitUI.clicked.connect(reorientP)
        self.landscapeUI.clicked.connect(reorientL)
        self.show()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def quitn(self):
        print("LOG: Bye Bye")
        sys.exit()


class SwipeUX(QMainWindow):
    def __init__(self):
        super(SwipeUX, self).__init__()
        self.oldPos = None
        self.setObjectName("SwipeUX")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.resize(70, 70)
        # -----------------------
        # =====================
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "QWidget{background-color: rgba(0,0,0,0);}\nQPushButton {\n"
            "border-radius: 15px;\n"
            "    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.495098, fy:0.5, stop:0.887255 rgba(35, 35, 35, 255), stop:0.901961 rgba(0, 0, 0, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "\n"
            "}\\n\n"
            "QPushButton:pressed {\n"
            "border-radius: 15px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "   }\n"
            "QMainWindow{background-color: rgba(0,0,0,30);}\n"
            "QPushButton:hover {\n"
            "border-radius: 15px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.swirt = QtWidgets.QPushButton(self.centralwidget)
        self.swirt.setGeometry(QtCore.QRect(40, 20, 30, 30))
        self.swirt.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-right.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swirt.setIcon(icon1)
        self.swirt.setObjectName("swirt")
        self.swilf = QtWidgets.QPushButton(self.centralwidget)
        self.swilf.setGeometry(QtCore.QRect(0, 20, 30, 30))
        self.swilf.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swilf.setIcon(icon2)
        self.swilf.setObjectName("swilf")
        self.swidn = QtWidgets.QPushButton(self.centralwidget)
        self.swidn.setGeometry(QtCore.QRect(20, 40, 30, 30))
        self.swidn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-down.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swidn.setIcon(icon3)
        self.swidn.setObjectName("swidn")
        self.swiup = QtWidgets.QPushButton(self.centralwidget)
        self.swiup.setGeometry(QtCore.QRect(20, 0, 30, 30))
        self.swiup.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-up.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.swiup.setIcon(icon4)
        self.swiup.setObjectName("swiup")
        self.setCentralWidget(self.centralwidget)
        # -----------------
        # ================

        self.oldpos = self.pos()

        self.swiup.pressed.connect(self.swipup)
        self.swidn.pressed.connect(self.swipdn)
        self.swilf.pressed.connect(self.swipleft)
        self.swirt.pressed.connect(self.swipright)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)
        qp.setBrush(QtGui.QColor(0, 0, 0, 127))
        qp.drawEllipse(0, 0, 70, 70)
        qp.end()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        # print("HIT")

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def swipdn(self):
        print("LOG: Passing SWIPE DOWN")
        adb_dim = po(
            increment +
            "adb shell wm size",
            shell=True,
            stdout=PIPE,
            stderr=PIPE)
        out = adb_dim.stdout.read()
        out_decoded = out.decode("utf-8")
        out_decoded = out_decoded[:-1]
        dimVal = out_decoded.split(": ")
        dimensions_ = dimVal[1]
        dimValues = dimensions_.split("x")
        posy = int(dimValues[1])
        posx = int(dimValues[0])

        newposx = posx / 2  # find center

        adb_pull = po(
            increment
            + "adb shell input swipe "
            + str(newposx)
            + " 200 "
            + str(newposx)
            + " "
            + str(posy - 200),
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

    def swipup(self):
        print("LOG: Passing SWIPE UP")
        adb_dim = po(
            increment +
            "adb shell wm size",
            shell=True,
            stdout=PIPE,
            stderr=PIPE)
        out = adb_dim.stdout.read()
        out_decoded = out.decode("utf-8")
        out_decoded = out_decoded[:-1]
        dimVal = out_decoded.split(": ")
        dimensions__ = dimVal[1]
        dimValues = dimensions__.split("x")
        posy = int(dimValues[1])
        posx = int(dimValues[0])

        newposx = posx / 2  # find center

        adb_pull = po(
            increment
            + "adb shell input swipe "
            + str(newposx)
            + " "
            + str(posy - 200)
            + " "
            + str(newposx)
            + " 200",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

    def swipleft(self):
        print("LOG: Passing SWIPE LEFT")
        adb_dim = po(
            increment +
            "adb shell wm size",
            shell=True,
            stdout=PIPE,
            stderr=PIPE)
        out = adb_dim.stdout.read()
        out_decoded = out.decode("utf-8")
        out_decoded = out_decoded[:-1]
        dimVal = out_decoded.split(": ")
        dimensions__ = dimVal[1]
        dimValues = dimensions__.split("x")
        posy = int(dimValues[1])
        posx = int(dimValues[0])

        newposy = posy / 2  # find center

        adb_pull = po(
            increment
            + "adb shell input swipe "
            + str(10)
            + " "
            + str(newposy)
            + " "
            + str(posx - 10)
            + " "
            + str(newposy),
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

    def swipright(self):
        print("LOG: Passing SWIPE RIGHT")
        adb_dim = po(
            increment +
            "adb shell wm size",
            shell=True,
            stdout=PIPE,
            stderr=PIPE)
        out = adb_dim.stdout.read()
        out_decoded = out.decode("utf-8")
        out_decoded = out_decoded[:-1]
        dimVal = out_decoded.split(": ")
        dimensions_ = dimVal[1]
        dimValues = dimensions_.split("x")
        posy = int(dimValues[1])
        posx = int(dimValues[0])

        newposy = posy / 2  # find center

        adb_pull = po(
            increment
            + "adb shell input swipe "
            + str(posx - 10)
            + " "
            + str(newposy)
            + " "
            + str(10)
            + " "
            + str(newposy),
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )


class Panel(QMainWindow):
    # there was a Dialog in the bracket
    def __init__(self):

        super(Panel, self).__init__()
        # print("POSITION OF PANEL:")
        # ---------------------------------
        # BETA test
        # -----------------------------------
        # imported bottompanelUI.py into main module
        # -----------------------------------

        self.setObjectName("self")
        self.resize(328, 26)
        self.oldPos = None
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/res/ui/guiscrcpy_logo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "\n"
            ".QPushButton {\n"
            "border-radius: 1px;\n"
            "color: rgb(0, 0, 0);\n"
            " \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.915182, x2:0, y2:0.926, stop:0.897059 rgba(41, 41, 41, 255), stop:1 rgba(30, 30, 30, 255));\n"
            "                    }\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "QPushButton:hover {\n"
            "border-radius: 5px;\n"
            "                      \n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "color: rgb(0, 0, 0);\n"
            "                        }\n"
            "")
        self.backk = QtWidgets.QPushButton(self)
        self.backk.setEnabled(True)
        self.backk.setGeometry(QtCore.QRect(210, 0, 51, 25))
        self.backk.setStyleSheet("")
        self.backk.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/chevron-sign-left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.backk.setIcon(icon1)
        self.backk.setObjectName("backk")
        self.powerUII = QtWidgets.QPushButton(self)
        self.powerUII.setEnabled(True)
        self.powerUII.setGeometry(QtCore.QRect(20, 0, 61, 25))
        self.powerUII.setStyleSheet("")
        self.powerUII.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/power.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.powerUII.setIcon(icon2)
        self.powerUII.setCheckable(False)
        self.powerUII.setObjectName("powerUII")
        self.menuUII = QtWidgets.QPushButton(self)
        self.menuUII.setEnabled(True)
        self.menuUII.setGeometry(QtCore.QRect(90, 0, 51, 25))
        self.menuUII.setStyleSheet("")
        self.menuUII.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/reorder-option.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.menuUII.setIcon(icon3)
        self.menuUII.setObjectName("menuUII")
        self.vdownn = QtWidgets.QPushButton(self)
        self.vdownn.setEnabled(True)
        self.vdownn.setGeometry(QtCore.QRect(270, 0, 31, 25))
        self.vdownn.setStyleSheet("")
        self.vdownn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/reduced-volume.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.vdownn.setIcon(icon4)
        self.vdownn.setObjectName("vdownn")
        self.homee = QtWidgets.QPushButton(self)
        self.homee.setEnabled(True)
        self.homee.setGeometry(QtCore.QRect(140, 0, 71, 25))
        self.homee.setStyleSheet("")
        self.homee.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/icons/icons/home.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.homee.setIcon(icon5)
        self.homee.setObjectName("homee")
        self.vupp = QtWidgets.QPushButton(self)
        self.vupp.setEnabled(True)
        self.vupp.setGeometry(QtCore.QRect(300, 0, 31, 25))
        self.vupp.setStyleSheet("")
        self.vupp.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/icons/icons/volume-up-interface-symbol.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.vupp.setIcon(icon6)
        self.vupp.setObjectName("vupp")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, -10, 20, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.homee.raise_()
        self.backk.raise_()
        self.powerUII.raise_()
        self.menuUII.raise_()
        self.vdownn.raise_()
        self.vupp.raise_()
        self.label.raise_()
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Panel", "guiscrcpy"))
        self.backk.setToolTip(_translate("Panel", "Back key"))
        self.powerUII.setToolTip(_translate("Panel", "Power on/off"))
        self.menuUII.setToolTip(_translate("Panel", "Menu key"))
        self.vdownn.setToolTip(_translate("Panel", "Volume Up"))
        self.homee.setToolTip(_translate("Panel", "Home key"))
        self.label.setText(_translate("Panel", "::"))

        # -----------------------------------
        self.oldpos = self.pos()
        # Ui_Panel.__init__(self)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )

        # self.setupUi(Dialog)
        self.backk.clicked.connect(Back)
        self.menuUII.clicked.connect(menu)
        self.homee.clicked.connect(homekey)
        self.powerUII.clicked.connect(power)
        self.vupp.clicked.connect(volUP)
        self.vdownn.clicked.connect(volDN)

        self.show()
        # print("self.oldpos", self.oldpos)
        # print("FINE TILL HERE")
        # pdb.set_trace()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        # print("HIT")

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    """
        def __init__(self, Dialog):
        super(Panel, self).__init__()

        Ui_Panel.__init__(self)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.setupUi(Dialog)
        self.backk.clicked.connect(Back)
        self.menuUII.clicked.connect(menu)
        self.homee.clicked.connect(homekey)
        self.powerUII.clicked.connect(power)
        self.vupp.clicked.connect(volUP)
        self.vdownn.clicked.connect(volDN)





        self.mwidget = Ui_Panel()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        #size
        self.setFixedSize(320, 450)
        self.center()
        self.oldPos = self.pos()

        self.show()

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def __init__(self, Dialog):
        super(Panel, self).__init__()

        Ui_Panel.__init__(self)
        # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.setupUi(Dialog)
        self.backk.clicked.connect(Back)
        self.menuUII.clicked.connect(menu)
        self.homee.clicked.connect(homekey)
        self.powerUII.clicked.connect(power)
        self.vupp.clicked.connect(volUP)
        self.vdownn.clicked.connect(volDN)
        self.oldPos = self.pos()


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        print("LOG: Delta: ", delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)
    """


# END TOOLKIT


def update_terminal():
    """
        self.new_thread = Terminal()
        self.connect(self.new_thread, SIGNAL("line"), self.show_variable)
        self.new_thread.start()
    """
    tmpTerminal = open("usercfgGUISCRCPY.cfg", "r")
    tmpRead = tmpTerminal.read()
    return tmpRead


"""
class StartScrcpy(QThread):
    print("Hello")

    def __init__(self, options):
        QThread.__init__(self)
        print("SCRCPY launch")
        # backup = po(increment+"scrcpy" + str(options),
        #                          shell=True,
        #                          stdin=PIPE,
        #                          stdout=PIPE,
        #                          stderr=STDOUT)

    def __del__(self):
        self.wait()

    def startSact(self):
        # TODO FIX OPTIONS
        # this block is for instantaneous reading the output
        # block ends out
        if checkProcessRunning("scrcpy"):
            print("SCRCPY RUNNING")
            # self.runningNot.setText("SCRCPY SERVER RUNNING")
        else:
            print("SCRCPY SERVER IS INACTIVE")
            # self.runningNot.setText("SCRCPY SERVER NOT RUNNING")

    def run(self):
        pass
"""


def readThreadStdOut():
    someFile = open("user.history", "w+")
    out, err = StartScrcpy.backup.stdout, StartScrcpy.backup.stderr
    out_decoded = out.decode("utf-8")
    someFile.write(str(out_decoded))
    someFile.flush()


runme = True
full = []

"""
def loop():
    for line in iter(StartScrcpy.backup.stdout.readline, b''):  # TODO NOT IMPLEMENTED
        line = line.rstrip().decode('utf8')
        print(">>>", line)
        full.append(line)
        output = '\n'.join(full)


loopprocess = multiprocessing.Process(target=loop)
loopprocess.start()
loopprocess.join()
print("Scrcpy proceed")
print(StartScrcpy.backup.stdout)
""" ""


def checkProcessRunning(processName):
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


class MyApp(Ui_MainWindow):
    def __init__(self, MainWindow):

        super(MyApp, self).__init__()
        # uic.loadUi(qtCreatorFile, self)

        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        # self.setupUi(self)
        # self.menuAbout.itemPressed.connect(self.menu_about)

        # check if process Scrcpy is running right now in while loop
        """
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));
color: rgb(0, 0, 0);
border-radius: 10px;
border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));
        """

        #bit_rate = bitrate0
        #dimensions = dimension0
        #swtouches = swtouches0
        #dispRO = dispRO0
        #fullscreen_opt = fullscreen0
        print(
            "LOG: Options received by class are : ",
            config['bitrate'],
            config['dimension'],
            config['swtouches'],
            config['dispRO'],
            config['fullscreen'],
        )
        self.dial.setValue(int(config['bitrate']))
        if config['swtouches']:
            self.showTouches.setChecked(True)
        else:
            self.showTouches.setChecked(False)
        if config['dispRO']:
            self.displayForceOn.setChecked(True)
        else:
            self.displayForceOn.setChecked(False)
        if config['dimension'] is not None:
            self.dimensionDefaultCheckbox.setChecked(False)
            try:
                self.dimensionSlider.setValue(config['dimension'])
            except TypeError:
                self.dimensionDefaultCheckbox.setChecked(True)
        if config['fullscreen']:
            self.fullscreen.setChecked(True)
        else:
            self.fullscreen.setChecked(False)
        if checkProcessRunning("scrcpy"):
            print("SCRCPY RUNNING")
            self.runningNot.setText("SCRCPY SERVER RUNNING")
        else:
            print("SCRCPY SERVER IS INACTIVE")
            self.runningNot.setText("SCRCPY SERVER NOT RUNNING")

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(
            self.dimensionChange)
        self.build_label.setText("Build " + str(build))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.dial_text_refresh)
        self.dial.sliderReleased.connect(self.dial_text_refresh)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)
        try:
            if config['extra']:
                self.flaglineedit.setText(config['extra'])
            else:
                pass
        except:
            pass

        self.quit.clicked.connect(self.quitAct)
        self.dimensionText.setText("DEFAULT")
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(" " + str(config['bitrate']) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtme.clicked.connect(self.openme)
        self.abtgit.clicked.connect(self.opengit)
        self.usbaud.clicked.connect(self.usbaudi)
        self.mapnow.clicked.connect(self.mapp)
    
    
    def mapp(self):
        if(os.path.exists(cfgpath + "guiscrcpy.mapper.json")):
            from guiscrcpy import mapper
            mapper.file_check()
        else:
            print("guiscrcpy ~ mapper is not initialized. Initialize by running","$ guiscrcpy-mapper", "reset points by", "$ guiscrcpy-mapper -r", sep="\n")

            
    def fin(self):
        result = []
        try:
            from guiscrcpy import __path__ as xz
            str1 = xz
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", str1)
        except:
            str1 = []
        for path in os.getenv('PATH').split(":")+str1:
            print("PATH:", path)
            for files in os.listdir(path):
                print("FILE: ", files)
                if "mapper.py" in files:
                    result.append(os.path.join(path, "mapper.py"))
                    break
            else:
                print("Mapper.py not found")
                
        return result
        
        
        
    def usbaudi(self):
        print("LOG: Called usbaudio")
        runnow = po("usbaudio", shell=True, stdout=PIPE, stderr=PIPE)
    
    
    """
    def mapper(self):
        
        fixedpos = [0,0]

        class Window(QtWidgets.QWidget):
            def __init__(self):
                QtWidgets.QWidget.__init__(self)
                self.label = QtWidgets.QLabel(self)
                self.drawing = False
                adb_dim = po(
                    "adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE
                )
                out = adb_dim.stdout.read()
                out_decoded = out.decode("utf-8")
                out_decoded = out_decoded[:-1]
                dimVal = out_decoded.split(": ")
                dimensions_ = dimVal[1]
                dimValues = dimensions_.split("x")
                print(dimValues, "HH")
                def on_press(key):
                    try:

                        if key.char == ",":
                            a = Popen(
                                "adb shell screencap -p /sdcard/scr.png",
                                shell=True,
                                stdout=PIPE,
                            )
                            b = Popen("adb pull /sdcard/scr.png", shell=True, stdout=PIPE)
                            

                            print(a.stdout)
                    except AttributeError:
                        print("special key {0} pressed".format(key))

                def on_release(key):
                    print("{0} released".format(key))
                    if key == keyboard.Key.esc:
                        # Stop listener
                        return False
                    if key.char == "o":
                        # Stop listener
                        print("REL POS :: ", fixedpos)
                        relx = fixedpos[0]/self.label.width()
                        rely = fixedpos[1]/self.label.height()
                        fixx = relx * int(dimValues[0])
                        fixy = rely * int(dimValues[1])
                        print("FINALIZED POS :: ", fixx, fixy)
                        sys.exit(fixx, fixy)

                # Collect events until released
                with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()

                # ...or, in a non-blocking fashion:
                listener = keyboard.Listener(on_press=on_press, on_release=on_release)
                listener.start()

                self.label.setSizePolicy(
                    QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
                )
                self.label.resize(800, 600)
                self.label.setContentsMargins(0, 0, 0, 0)
                self.pixmap = QtGui.QPixmap("scr.png")
                self.label.resize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
                self.resize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
                print("Lets Check")
                self.label.setPixmap(self.pixmap)
                self.label.setMinimumSize(1, 1)
                self.label.setMaximumSize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
                self.setMaximumSize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
                self.label.installEventFilter(self)
                layout = QtWidgets.QVBoxLayout(self)
                layout.addWidget(self.label)
                print("NICE LOOK")
                print("image.width == ", self.label.width())
                print("image.height == ", self.label.height())

            def eventFilter(self, source, event):
                if source is self.label and event.type() == QtCore.QEvent.Resize:
                    self.label.setPixmap(
                        self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
                    )
                return super(Window, self).eventFilter(source, event)


            def mousePressEvent(self, event):
                if event.button() == Qt.LeftButton:
                    
                    self.lastPoint= event.pos()
                    fixedpos[0] =int(event.pos().x())
                    fixedpos[1] =int(event.pos().y())
                    print(self.lastPoint , "LAST")
                    self.lastPoint=self.label.mapFromParent(event .pos()) #this is working fine now
                    # self.label.setPixmap(QPixmap.fromImage(self.image))

            def mouseMoveEvent(self,event):
                if (event.buttons() & Qt.LeftButton):
                    
                    #painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap,Qt.RoundJoin))
                    # painter.drawLine(self.label.mapFromParent(event.pos()),self.lastPoint)
                    self.lastPoint=self.label.mapFromParent(event.pos()) #this is working fine now
                    print(self.lastPoint , "MOVE")
                    fixedpos[0] =int(event.pos().x())
                    fixedpos[1] =int(event.pos().y())
                    # self.label.setPixmap(QPixmap.fromImage(self.image))
                
            def mouseReleaseEvent(self,event):
                if event.button == Qt.LeftButton:
                    #self.drawing = False
                    self.label.setPixmap(QPixmap.fromImage(self.image))


        if __name__ == "__main__":

            import sys

            app = QtWidgets.QApplication(sys.argv)
            window = Window()
            window.show()
            
            sys.exit(app.exec_())
    """
    
    
    def openme(self):
        webbrowser.open("https://srevinsaju.github.io")

    def opengit(self):
        webbrowser.open("https://github.com/srevinsaju/guiscrcpy")

    def about(self):
        abtBox = QMessageBox().window()
        abtBox.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. guiscrcpy will now exit",
        )
        abtBox.addButton("OK", abtBox.hide())
        abtBox.show()

    def reset(self):

        os.remove(cfgpath + jsonf)
        print("LOG: CONFIGURATION FILE REMOVED SUCCESSFULLY")
        print("RESTART")
        msgBox = QMessageBox().window()
        msgBox.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. guiscrcpy will now exit",
        )
        msgBox.addButton("OK", self.quitAct())
        msgBox.show()

    def quitAct(self):

        sys.exit()

    def menu_about(self):
        pass

    def dimensionChange(self):

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            config['dimension'] = None
            self.dimensionText.setText("DEFAULT")

        else:
            self.dimensionSlider.setEnabled(True)
            config['dimension'] = int(self.dimensionSlider.value())

            self.dimensionText.setText(
                " " + str(config['dimension']) + "px")
            self.dimensionSlider.sliderMoved.connect(
                self.slider_text_refresh)
            self.dimensionSlider.sliderReleased.connect(
                self.slider_text_refresh)

    def slider_text_refresh(self):
        config['dimension'] = int(self.dimensionSlider.value())

        self.dimensionText.setText(str(config['dimension']) + "px")
        pass

    def dial_text_refresh(self):
        config['bitrate'] = int(self.dial.value())

        # print("xcx" + str(bitrate0))
        self.bitrateText.setText(str(config['bitrate']) + "KB/s")
        pass

    def start_act(self):

        self.runningNot.setText("CHECKING DEVICE CONNECTION")
        timei = time.time()
        self.progressBar.setValue(5)
        adb_chk = po(increment + "adb devices", shell=True, stdout=PIPE)
        output = adb_chk.stdout.readlines()

        needed_output = output[1]

        deco = needed_output.decode("utf-8")
        det = deco.split("\t")
        print("ADB: ", det)

        if det[0] == "\n":
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0
        try:
            exc = det[1].find("device")
        except IndexError:
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0

        if det[1].find("device") > -1:
            self.runningNot.setText(
                "DEVICE " + str(det[0]) + " IS CONNECTED")
            self.progressBar.setValue(10)

        elif det[1][:-1] == "unauthorized":
            self.runningNot.setText(
                "DEVICE IS UNAUTHORIZED. PLEASE CLICK 'OK' ON DEVICE WHEN ASKED FOR"
            )
            self.progressBar.setValue(0)
            return 0

        else:
            self.runningNot.setText(
                "DEVICE CONNECTED BUT FAILED TO ESTABLISH CONNECTION"
            )
            self.progressBar.setValue(0)
            return 0
        # check if the defaultDimension is checked or not for giving signal
        # ADB READ DIMENSIONS :: BEGIN
        adb_dim = po(
            increment +
            "adb shell wm size",
            shell=True,
            stdout=PIPE,
            stderr=PIPE)
        out = adb_dim.stdout.read()
        out_decoded = out.decode("utf-8")
        out_decoded = out_decoded[:-1]
        dimVal = out_decoded.split(": ")
        dimensions_ = dimVal[1]
        dimValues = dimensions_.split("x")

        self.progressBar.setValue(15)

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.dimensionText.setText("DEFAULT")
            config['dimension'] = None

        else:
            self.dimensionSlider.setEnabled(True)
            config['dimension'] = int(self.dimensionSlider.value())
            self.dimensionSlider.setValue(config['dimension'])
            self.dimensionText.setText(str(config['dimension']) + "px")

        # check if the defaultDimension is checked or not for giving signal
        self.progressBar.setValue(20)
        """
        proc =run(["scrcpy"], stdout=PIPE,
                                stderr=PIPE)
        out, err = proc.stdout, proc.stderr
        out_decoded = out.decode("utf-8")
        tmp.append(out_decoded)
        self.terminal.setText(str(tmp))
        """

        # process dimension
        if config['dimension'] is None:
            self.options = " "
            pass
        elif config['dimension'] is not None:
            self.options = " -m " + str(config['dimension'])
        else:
            self.options = ""

        self.progressBar.setValue(25)
        # CHECK BOX GROUP CONNECT
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
            config['fullscreen'] = True
        else:
            config['fullscreen'] = False
        """
        if self.keepdisplayRO.isChecked():
            self.options += " --no-control"
        """
        self.progressBar.setValue(30)
        if self.showTouches.isChecked():
            self.options += " --show-touches"
            config['swtouches'] = True

            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """

        else:
            config['swtouches'] = False
        if self.recScui.isChecked():
            self.options += " -r " + str(int(time.time())) + ".mp4 "

            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """
        if self.displayForceOn.isChecked():
            self.options += " -S"
            config['dispRO'] = True
            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """

        else:
            config['dispRO'] = False

        self.options += " -b " + str(int(self.dial.value())) + "K"
        config['bitrate'] = int(self.dial.value())
        self.progressBar.setValue(40)



        # self.myLine = startScrcpy(self.options)
        # self.connect(self.myLine, SIGNAL("update_terminal(QString)"), self.update_terminal)
        print("LOG: CONNECTION ESTABLISHED")
        self.progressBar.setValue(50)
        """
        for line in iter(backup.stdout.readline, b''): # TODO NOT IMPLEMENTED
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)
            output = '\n'.join(full)
            self.terminal.setText(str(output))
        """
        print("LOG: Flags passed to scrcpy engine : " + self.options)
        self.progressBar.setValue(75)
        
        # get additional flags from QLineEdit self.flaglineedit
        config['extra']= self.flaglineedit.text()
        
        # run scrcpy usng subprocess
        backup = po(
            increment + "scrcpy " + str(self.options) + " " +  str(config['extra']),
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=STDOUT,
        )
        # StartScrcpy(options=self.options
        timef = time.time()
        eta = timef - timei
        print("LOG: SCRCPY is launched in", eta, "seconds")
        self.progressBar.setValue(100)

        with open(cfgpath + jsonf, 'w') as f:
            json.dump(config, f)
        print("LOG: Configuration file at ", cfgpath + jsonf, ".")

        if self.notifChecker.isChecked():
            print("LOG: Launching notification auditor")
            # ------------
            # Begin notif auditor
            # --------
            import pystray
            from PIL import Image, ImageDraw

            def callback(icon):
                if platform.system() == "Windows":
                    print(
                        "WARNING: Notif Auditor is experimental on Windows. If you wish to help out on this issue. Open a PR on github"
                    )
                    notif = po(
                        increment +
                        "adb shell dumpsys notification | findstr ticker ",
                        stdout=PIPE,
                        shell=True,
                    )
                else:
                    "WARNING: Notif Auditor is experimental on Linux. If you wish to help out on this issue. Open a PR on github"
                    notif = po(
                        increment +
                        "adb shell dumpsys notification | grep ticker | cut -d= -f2",
                        stdout=PIPE,
                        shell=True,
                    )
                image = Image.new("RGBA", (128, 128), (255, 255, 255, 255))
                # loop this block --->
                var1 = notif.stdout.readlines()
                var2 = var1
                while True:
                    if platform.system() == "Windows":
                        print(
                            "WARNING: Notif Auditor is experimental on Windows. If you wish to help out on this issue. Open a PR on github"
                        )
                        notif = po(
                            increment +
                            "adb shell dumpsys notification | findstr ticker ",
                            stdout=PIPE,
                            shell=True,
                        )
                    else:
                        "WARNING: Notif Auditor is experimental on Linux. If you wish to help out on this issue. Open a PR on github"
                        notif = po(
                            increment +
                            "adb shell dumpsys notification | grep ticker | cut -d= -f2",
                            stdout=PIPE,
                            shell=True,
                        )
                    image = Image.new(
                        "RGBA", (128, 128), (255, 255, 255, 255))
                    # loop this block --->
                    var1 = notif.stdout.readlines()

                    # <----
                    print("LOG: var1: ", var1)
                    if len(var1) > len(var2):
                        d = ImageDraw.Draw(image)
                        d.rectangle([0, 255, 128, 128], fill="green")
                        icon.icon = img
                        time.sleep(600)
                        var2 = var1

            image = Image.new("RGBA", (128, 128), (255, 255, 255, 255))

            icon = pystray.Icon("Test Icon 1", image)

            icon.visible = True
            icon.run(setup=callback)
            # End notif auditor


def launch_main0():

    app = QtWidgets.QApplication(sys.argv)

    # file = QFile(":/dark.qss")
    # file.open(QFile.ReadOnly | QFile.Text)
    # stream = QTextStream(file)
    # app.setStyleSheet(stream.readAll())
    splash_pix = QPixmap(":/res/ui/guiscrcpy-branding.png")
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    # -------------------
    # chk ADB devices prehandle
    # -------------------
    adb_chk8 = po(increment + "adb devices", shell=True, stdout=PIPE)
    output8 = adb_chk8.stdout.readlines()
    try:
        needed_output8 = output8[1]
        deco8 = needed_output8.decode("utf-8")
        det8 = deco8.split("\t")
        print("ADB: ", deco8)

    except IndexError:
        print(
            bcolors.FAIL +
            " ADB is not installed on your system" +
            bcolors.ENDC)

    # ------------------

    time.sleep(0.5)
    app.processEvents()

    rw = SwipeUX()  # Load swipe UI
    rw.show()  # show Swipe UI

    window = QtWidgets.QMainWindow()  # Create windwo
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # windoww = QtWidgets.QMainWindow()
    # windowww = QtWidgets.QMainWindow()
    prog = MyApp(window)
    # panel = Panel(windoww)
    panel = Panel()
    progg = MyAppv()
    window.show()
    splash.hide()
    # windowww.show()
    # windoww.show()
    app.exec_()
    # appo.exec_()
    sys.exit()


if __name__ == "__main__":
    try:
        import guiscrcpy
        patz = list(guiscrcpy.__path__)[0]
        sys.path.append(patz)
        sys.path.append('')
    except ModuleNotFoundError:
        pass
    sys.path.append('')

    launch_main0()
    


def launch_main():
    import guiscrcpy
    patz1 = list(guiscrcpy.__path__)[0]
    sys.path.append(patz1)
    # print("SYS.path ==", sys.path)
    if(platform.system() == "Windows"):
        pythonexec = "python"
    else:
        pythonexec = "python3"
    ar = ""
    for i in sys.argv[1:]:
        ar += " " + i + " "
    #a= po(pythonexec + " ."+ar, shell=True, stdout=PIPE)
    launch_main0()
    print(a.stdout)


"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from guiscrcpy.lib.config import InterfaceConfig
from guiscrcpy.lib.check import adb
import argparse
from subprocess import PIPE, Popen
from pynput import keyboard
from PyQt5.QtGui import QPixmap, QPen, QPainter
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from subprocess import Popen as po
from subprocess import PIPE
import os
import platform
import sys
import json
import copy
import time

get1 = False
fixedpos = [0, 0]
finalpos = [0, 0]

cfgmgr = InterfaceConfig()
config = cfgmgr.get_config()
adb.path = config['adb']

jsong = 'guiscrcpy.mapper.json'

print("+++++++++++++++++++++++++++++++++++++++")
print("guiscrcpy ~ mapper by srevinsaju")
print("=======================================")
print("Make sure that your device is turned on, and connected to your PC")
print('With USB debugging turned on.')
print("+++++++++++++++++++++++++++++++++++++++")
print("Waiting for device")
adb.command(adb.path, 'wait-for-any-device')
print("Device : OK!")

cfgpath = cfgmgr.cfgpath

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--delay', default=10,
                    help="Set time to delay before screen is captured")
parser.add_argument('-r', '--reset', action="store_true",
                    help="Remove prefernces")
args = parser.parse_args()

dimensions = adb.get_dimensions(adb.path)


class MapperUI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.label = QtWidgets.QLabel(self)
        self.drawing = False
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(25, 16777215))
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label0 = QtWidgets.QLabel(self.widget)
        self.label0.setMinimumSize(QtCore.QSize(25, 25))
        self.label0.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "border-radius: 10px;\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(61, 255, 0, 255), stop:1 rgba(226, 255, 0, 255));\n"
                                  "")
        self.label0.setAlignment(QtCore.Qt.AlignCenter)
        self.label0.setObjectName("label")
        self.horizontalLayout.addWidget(self.label0)
        self.pushButton.pressed.connect(self.keyreg)
        # -- pullscreen shot
        a = Popen(
            "adb shell screencap -p /sdcard/scr.png",
            shell=True,
            stdout=PIPE,
        )
        time.sleep(2)
        b = Popen("adb pull /sdcard/scr.png "+cfgpath +
                  "scr.png", shell=True, stdout=PIPE)
        time.sleep(1)
        print(b.stdout.read().decode('utf-8'))
        print(a.stdout.read().decode('utf-8'))
        b = Popen("adb shell rm /sdcard/scr.png", shell=True, stdout=PIPE)
        self.label.setSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        self.label.resize(800, 600)
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setContentsMargins(0, 0, 0, 0)
        self.pixmap = QtGui.QPixmap(cfgpath+"scr.png")
        self.label.resize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
        self.resize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
        print("Lets Check")
        self.show()
        self.resize(self.label.size())
        self.label.setPixmap(self.pixmap)
        self.label.setMinimumSize(1, 1)
        self.label.setMaximumSize(
            0.5*self.pixmap.width(), 0.5*self.pixmap.height())
        self.setMaximumSize(0.5*self.pixmap.width(), 0.5*self.pixmap.height())
        self.label.installEventFilter(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        # print("NICE LOOK")
        # print("image.width == ", self.label.width())
        # print("image.height == ", self.label.height())
        # print("POSITION self.label.pos()", self.label.pos())
        # print("pix.width()", self.pixmap.width(), self.pixmap.height())
        self.pushButton.setText("OK")
        self.label0.setWordWrap(True)
        self.label0.setText(
            "Click the point, and enter char in textbox and press OK to continue.")

    def keyreg(self):
        with open(cfgpath + 'guiscrcpy.mapper.json', 'r') as f:
            key_a = json.load(f)
        #print("REL POS :: ", fixedpos)
        relx = fixedpos[0]/self.label.width()
        rely = fixedpos[1]/self.label.height()
        fixx = relx * int(dimensions[0])
        fixy = rely * int(dimensions[1])
        print("FINALIZED POS :: ", fixx, fixy)

        finalpos[0] = fixx
        finalpos[1] = fixy
        self.label0.setText(
            "SUCCESS! Add a new point and enter char; close the window to finish adding.")

        print("FINAL LIST == ", finalpos)
        keylisten = self.lineEdit.text()

        try:
            # keylisten = input("Enter key : ")

            print('YES THE KEY IS == ', keylisten)

            key_a[keylisten] = copy.copy(finalpos)

            print(key_a)
            with open(cfgpath + jsong, 'w') as f:
                json.dump(key_a, f)

            print("key_a", key_a)

        except:
            print("Special key entered, Use normal characters only")

    def eventFilter(self, source, event):
        if source is self.label and event.type() == QtCore.QEvent.Resize:
            self.label.setPixmap(
                self.pixmap.scaled(self.label.size(),
                                   QtCore.Qt.KeepAspectRatio)
            )
        return super(MapperUI, self).eventFilter(source, event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.lastPoint = event.pos()
            fixedpos[0] = int(event.pos().x())
            fixedpos[1] = int(event.pos().y())
            print(self.lastPoint, "LAST")
            self.lastPoint = self.label.mapFromParent(
                event .pos())  # this is working fine now
            # self.label.setPixmap(QPixmap.fromImage(self.image))

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton):

            #painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap,Qt.RoundJoin))
            # painter.drawLine(self.label.mapFromParent(event.pos()),self.lastPoint)
            self.lastPoint = self.label.mapFromParent(
                event.pos())  # this is working fine now
            print(self.lastPoint, "MOVE")
            fixedpos[0] = int(event.pos().x())
            fixedpos[1] = int(event.pos().y())
            # self.label.setPixmap(QPixmap.fromImage(self.image))

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            #self.drawing = False
            self.label.setPixmap(QPixmap.fromImage(self.image))


def listen_keypress(key_a):
    print("[SERVER] LISTENING VALUES: Your keys are being listened by server. ")
    print(key_a)

    def on_press0(key):
        finalpos = [0, 0]

        try:
            if key.char in key_a.keys():
                print(key.char)
                print("running cmd")
                finalpos0 = key_a[key.char]
                cm = "adb shell input tap " + \
                    str(finalpos0[0]) + " " + str(finalpos0[1])
                print(cm)
                c = po(cm, shell=True, stdout=PIPE)
                print(c.stdout.read().decode('utf-8'))
                print("COMPLETED")
        except AttributeError:
            print("E:")

    with keyboard.Listener(on_press=on_press0) as listener:
        listener.join()

        # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press0)
    listener.start()


def sth():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MapperUI()
    sys.exit(app.exec_())


def file_check():
    jsong = 'guiscrcpy.mapper.json'

    try:
        with open(cfgpath + 'guiscrcpy.mapper.json', 'r') as f:
            key_a = json.load(f)
        fileExist = True
        print("LOG: Key:Pos JSON Configuration file found in ",
              cfgpath, " directory")
    except FileNotFoundError:
        print("LOG: Initializing guiscrcpy.mapper() for first time use...")
        key_a = {"key": []}
        with open(cfgpath + jsong, 'w') as f:
            json.dump(key_a, f)
        print("LOG: Key:Pos JSON Configuration file created in ",
              cfgpath, " directory")
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

    if not fileExist:

        # Init json file for first time use
        key_a = {"key": [], "pos": []}
        with open(cfgpath + jsong, 'w') as f:
            json.dump(key_a, f)
        sth()

    elif fileExist:
        with open(cfgpath + jsong, 'r') as f:
            key_a = json.load(f)
        print('KEY:A', key_a)
        listen_keypress(key_a)


def file_checkm():
    try:
        with open(cfgpath + jsong, 'r') as f:
            key_a = json.load(f)
        fileExist = True
        print("LOG: Key:Pos JSON Configuration file found in ",
              cfgpath, " directory")
    except FileNotFoundError:
        print("LOG: Initializing guiscrcpy.mapper() for first time use...")
        with open(cfgpath + jsong, 'w') as f:
            json.dump(key_a, f)
        print("LOG: Key:Pos JSON Configuration file created in ",
              cfgpath, " directory")
        fileExist = False
        if (args.reset):
            os.remove(cfgpath+"guiscrcpy.mapper.json")
            print("FILE RESET")
            sys.exit()
        print("WAITING FOR ", args.delay, "s")
        time.sleep(args.delay)

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

    if not fileExist:
        # Init json file for first time use
        key_a = {"key": [], "pos": []}
        with open(os.path.join(cfgpath, jsong), 'w') as f:
            json.dump(key_a, f)

    elif fileExist:
        with open(os.path.join(cfgpath, jsong), 'r') as f:
            key_a = json.load(f)
        listen_keypress(key_a)


if __name__ == "__main__":
    file_check()

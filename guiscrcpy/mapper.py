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


fixedpos = [0,0]
finalpos = [0,0]
key_a = {"key":["0"], "pos":[[0,0]]}

jsonf = 'guiscrcpy.mapper.json'
# Declare key_a. path position
if (platform.system() == 'Windows'):
    cfgpath = os.path.expanduser("~/AppData/Local/")
else:
    if (os.getenv('XDG_CONFIG_HOME') is None):
        cfgpath = os.path.expanduser("~/.config/")
    else:
        cfgpath = os.getenv('XDG_CONFIG_HOME').split(":")[0]

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
                    print(b.stdout.read().decode('utf-8'))
                    

                    print(a.stdout)
            except (AttributeError, SyntaxError):
                print("special key {0} pressed".format(key))

        def on_release(key):
            print("{0} released".format(key))
            if key == keyboard.Key.esc:
                # Stop listener
                return False
            try:
                if key.char == "o":
                    # Stop listener
                    print("REL POS :: ", fixedpos)
                    relx = fixedpos[0]/self.label.width()
                    rely = fixedpos[1]/self.label.height()
                    fixx = relx * int(dimValues[0])
                    fixy = rely * int(dimValues[1])
                    print("FINALIZED POS :: ", fixx, fixy)
                    finalpos[0] = fixx
                    finalpos[1] = fixy
                    print("FINAL LIST == ", finalpos)
                    listener.stop()
                    self.hide()
                    mapcomplete()
            except AttributeError:
                pass

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


def mapcomplete():
    print("LAUNCHING KEY LISTENER ")
    print('Enter the key for mapping')
    print("use only normal characters. No special chars")
    try:
        keylisten = input("Enter key : ")
        print('YES THE KEY IS == ', keylisten)
        
        key_a['key'] = list(keylisten)
        key_a['pos'] = list(finalpos)
        print(key_a)
        with open(cfgpath + jsonf, 'w') as f:
            json.dump(key_a, f)
            
        print("key_a", key_a)
        checkn(keylisten, finalpos)
    except:
        print("Special key entered, Use normal characters only")
    
    

def checkn(keylisten, finalpos0):
    print("LISTENING VALUES. Your keys are being listened by server. ")
    def on_press0(key):
        try:
            if key.char == keylisten:
                print(key.char)
                print("running cmd")    
                print(finalpos0)
                cm = "adb shell input tap " + str(finalpos0[0]) + " " + str(finalpos0[1])
                print(cm)
                c = po(cm, shell=True, stdout=PIPE)
                print(c.stdout.read().decode('utf-8'))
                print("COMPLETED")
        except AttributeError:
            pass
        
    with keyboard.Listener(on_press=on_press0) as listener:
        listener.join()

        # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press0)
    listener.start()

def sth():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()



try:
    with open(cfgpath + jsonf, 'r') as f:
        key_a = json.load(f)
    fileExist = True
    print("LOG: key_auration file found in ", cfgpath, " directory")

except FileNotFoundError:

    print("LOG: Initializing guiscrcpy for first time use...")
    with open(cfgpath + jsonf, 'w') as f:
        json.dump(key_a, f)

    print("LOG: key_auration file created in ", cfgpath, " directory")
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
    key_a = {"key":[], "pos":[]}
    with open(cfgpath + jsonf, 'w') as f:
        json.dump(key_a, f)
    sth()


elif fileExist:
    with open(cfgpath + jsonf, 'r') as f:
        key_a = json.load(f)
    checkn(key_a['key'][0], key_a['pos'])
    

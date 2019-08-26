#
"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy
Licensed under GNU Public License

Build 1.9.7

CHANGELOG:

Build 1.9.7-release
16072019 1512
* Fixed many bugs
* Added configuration file
* Migrated from PyQt5 to PyQt5 due to KDE Plasma incompatibility
* Added config file save and read
* Edited ProgressBar thread locking to progressive type
* Separated  to linear and horizontal toolkit for easy use
* Added experimental autorotate orientage support change

Build 1.9.6
* Minor fixes

Build 1.9.5
25062019 2159
* MEGA CHANGE :: Migrated from `PyQt4` to `PyQt5` due to late realization that PyQt4 support
for Windows is unfortunately discontinued.
* `mainwindow.ui` >> xml parsed file loaded in uic loader has been compiled to `mainui.py` as UI
* toolkit.py is deprecated. toolkit class is restructured into mainwindow class with multiprocesing.
* After `PyQt5` update, GTK-LTK-KDE no longer raises pixmap errors


Build 1.9.4
23062018 1615 GMT+300
* Dumped terminal QTextEdit for multiprocessing to prevent QThread hang.
* Restructured StartScrcpy Class as two threads.

Build 1.9.3
22062019 1948 GMT+3
* Fixed GUI hang (issue reported by @rom1v)
(code has been restructured. the old code is placed in `/backup/` folder as `main 1.9.2.py`. But however, terminal ui QTextEdit
is not functional.


1.9.2
* Added GUIScrcpy icon
* Added pixmap icons
* Added check scrcpy process running or not
* Added GUIScrcpy Toolkit Experimental Support

1.9.1
* Initial Build :)


Syntax for the config file
ln1:: dial value
ln2:: dimensionCheckBox
ln3:: dimension value
ln4:: fullScreen
ln5:: showTouches


Icon made by Dave Gandy from www.flaticon.com used under Creative Commons 3.0 Unported. 
The original SVG black work by Dave Gandy has ben re-oriented, flipped or color-changed. 
The rest of Terms and Conditions put formward by CC-3.0:Unported has been feverently followed 
by the debeloper. Icons have been adapeted in all the three windows.

Icons pack obtained from www.flaticon.com
All rights reserved.

"""


# removed multiprocess modules


from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import qdarkstyle
import os
from subprocess import Popen as po, STDOUT
from subprocess import PIPE
import sys
import time
from PyQt5.QtWidgets import QMessageBox
from toolUI import Ui_Dialog
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow
from bottompanelUI import Ui_Panel
import breeze_resources
try:
    import psutil
except ModuleNotFoundError:
    print("psutil is not installed in the python3 directory. "
          "Install with \n $ pip3 install psutil")

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
from mainui import Ui_MainWindow

build = "1.9.7"
print("guiscrcpy v1.10.0-release")
print("by srevinsaju")
print("************************************")
print("released on 24082019 GMT+0300 2048 ")
print("************************************")
bitrate0 = 8000
try:
	cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "r")
	fileExist = True
	print("User configuration file found!")
except FileNotFoundError or FileExistsError:
    print("User configuration file not found!")
    cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "w+")
    fileExist = False

    cfg.close()

if not fileExist:
	cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "r+")
	cfg.writelines(("#" * 25 + "\n", "Created by Srevin Saju\n", "#" * 25 + "\n", str(time.time()) + "\n"))

	cfg.close()
elif fileExist:
	cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "r")
	"""
        the cfg file struct::
        :bitrate0 [4]
        :dimension0 [5]
        :swtouches0 [6]
        :fullscreen0 [7]
        :dispRO0 [8]
        
        
        
	"""
	a = cfg.readlines()
	cfg.close()
	# print("cfg:", cfg.readlines())
	print("cfg:", a)
	
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
		dispRO0= a[8].strip("\n")
		print("SUCCESS dispRO")
	except IndexError:
		dispRO0 = "False"
		print("FAILED dispRO")
	print("Bitrate : ", bitrate0, " + Dimensions", dimension0, "")
	print(bitrate0)
	print("dispRO:", dispRO0)



# ===================



# BEGIN TOOLKIT.UI

def clipd2pc():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "c")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+c")


def power():
    print("POWER")
    adb_power = po("adb shell input keyevent 26", shell=True, stdout=PIPE,
                                 stderr=PIPE)


def menu():
    print("MENU")
    adb_menu = po("adb shell input keyevent 82", shell=True, stdout=PIPE,
                                stderr=PIPE)


def Back():
    print("BACK")
    adb_back = po("adb shell input keyevent 4", shell=True, stdout=PIPE,
                                stderr=PIPE)


def volUP():
    print("BACK")
    adb_back = po("adb shell input keyevent 24", shell=True, stdout=PIPE,
                                stderr=PIPE)


def volDN():
    print("BACK")
    adb_back = po("adb shell input keyevent 25", shell=True, stdout=PIPE,
                                stderr=PIPE)


def homekey():
    print("HOME")
    adb_home = po("adb shell input keyevent 3", shell=True, stdout=PIPE,
                                stderr=PIPE)


def switch():
    print("APP_SWITCH")
    adb_home = po("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True,
                                stdout=PIPE,
                                stderr=PIPE)


def reorientP():
    print("REORIENT [POTRAIT]")
    adb_reo = po("adb shell settings put system accelerometer_rota"
                               "tion 0; adb shell settings put system"
                               " user_rotation 0", shell=True)


def reorientL():
    print("REORIENT [LANDSCAPE]")
    adb_reoo = po("adb shell settings put system accelerometer_rota"
                                "tion 0; adb shell settings put system"
                                " user_rotation 1", shell=True)


def notifExpand():
    print("NOTIF EXPAND")
    adb_dim = po("adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE)
    out = adb_dim.stdout.read()
    out_decoded = out.decode("utf-8")
    out_decoded = out_decoded[:-1]
    dimVal = out_decoded.split(": ")
    dimensions_ = dimVal[1]
    dimValues = dimensions_.split("x")
    adb_pull = po("adb shell input swipe 0 0 0 " + str(int(dimValues[1]) - 1),
                                shell=True, stdout=PIPE,
                                stderr=PIPE)


def notifCollapse():
    print("NOTIF COLLAPSE")
    adb_dim = po("adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE)
    out = adb_dim.stdout.read()
    out_decoded = out.decode("utf-8")
    out_decoded = out_decoded[:-1]
    dimVal = out_decoded.split(": ")
    dimensions_ = dimVal[1]
    dimValues = dimensions_.split("x")
    adb_pull = po("adb shell input swipe 0 " + str(int(dimValues[1]) - 1) + " 0 0",
                                shell=True, stdout=PIPE,
                                stderr=PIPE)


def clippc2d():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "shift", "c")
        print("NOT SUPPORTED ON WINDOWS")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+shift+c")


def fullscreen():
    try:
        scrcpywindow = getWindowsWithTitle("scrcpy")[0]
        scrcpywindow.focus()
        auto.hotkey("ctrl", "f")
    except NameError:
        os.system("wmctrl -x -a  scrcpy && xdotool key --clearmodifiers ctrl+f")


class MyAppv(Ui_Dialog):
    def __init__(self, Dialog):
        super(MyAppv, self).__init__()
        Ui_Dialog.__init__(self)
        Dialog.setFixedSize(30, 460)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setupUi(Dialog)
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
        
    

    def quitn(self):
        print("Quitting")
        sys.exit()

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

class Panel(Ui_Panel):
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
        

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)
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
        # backup = po("scrcpy" + str(options),
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
"""""


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
        

       
        bit_rate = bitrate0
        dimensions = dimension0
        swtouches = swtouches0
        dispRO = dispRO0
        fullscreen_opt = fullscreen0
        print("OPTS:", bit_rate, dimensions, swtouches, dispRO, fullscreen_opt)
        self.dial.setValue(int(bit_rate))
        if (swtouches.find("True")>-1):
            self.showTouches.setChecked(True)
        else:
            self.showTouches.setChecked(False)
        if (dispRO.find("True")>-1):
            self.displayForceOn.setChecked(True)
        else:
            self.displayForceOn.setChecked(False)
        if dimensions != None:
            self.dimensionDefaultCheckbox.setChecked(False)
            try:
            	self.dimensionSlider.setValue(dimensions)
            except TypeError:
            	self.dimensionDefaultCheckbox.setChecked(True)
        if (fullscreen_opt.find("True")>-1):
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
        self.dimensionDefaultCheckbox.stateChanged.connect(self.dimensionChange)
        self.build_label.setText("Build " + str(build))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.dial_text_refresh)
        self.dial.sliderReleased.connect(self.dial_text_refresh)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)

        self.quit.clicked.connect(self.quitAct)
        self.dimensionText.setText("DEFAULT")
        bit_rate = int(self.dial.value())
        self.bitrateText.setText(" " + str(bit_rate) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtme.clicked.connect(self.openme)
        self.abtgit.clicked.connect(self.opengit)

    def openme(self):
        webbrowser.open("https://srevinsaju.wixsite.com/srevinsaju")
    def opengit(self):
        webbrowser.open("https://github.com/srevinsaju/guiscrcpy")
    def about(self):
        abtBox = QMessageBox().window()
        abtBox.about(self.pushButton, "Info", "Please restart GUIscrcpy to reset the settings. GUIscrcpy will now exit")
        abtBox.addButton("OK", abtBox.hide())
        abtBox.show()

    def reset(self):
        cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "w+")
        cfg.write("RESET" + str(time.time()))
        cfg.close()
        msgBox = QMessageBox().window()
        msgBox.about(self.pushButton, "Info", "Please restart GUIscrcpy to reset the settings. GUIscrcpy will now exit")
        msgBox.addButton("OK", self.quitAct())
        msgBox.show()

    def quitAct(self):

        sys.exit()

    def menu_about(self):
        pass

    def dimensionChange(self):

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            dimension = None
            self.dimensionText.setText("DEFAULT")
            dimension0 = None

        else:
            self.dimensionSlider.setEnabled(True)
            dimension = int(self.dimensionSlider.value())
            dimension0 = int(self.dimensionSlider.value())
            self.dimensionText.setText(" "+str(dimension) + "px")
            self.dimensionSlider.sliderMoved.connect(self.slider_text_refresh)
            self.dimensionSlider.sliderReleased.connect(self.slider_text_refresh)

    def slider_text_refresh(self):
        dimension = int(self.dimensionSlider.value())
        dimension0 = int(self.dimensionSlider.value())
        self.dimensionText.setText(str(dimension) + "px")
        pass

    def dial_text_refresh(self):
        bit_rate = int(self.dial.value())
        bitrate0 = bit_rate
        print("xcx" + str(bitrate0))
        self.bitrateText.setText(str(bit_rate) + "KB/s")
        pass

    def start_act(self):
    	

        self.runningNot.setText("CHECKING DEVICE CONNECTION")
        timei = time.time()
        self.progressBar.setValue(5)
        adb_chk = po("adb devices", shell=True, stdout=PIPE)
        output = adb_chk.stdout.readlines()
        needed_output = output[1]

        deco = needed_output.decode("utf-8")
        det = deco.split("\t")
        if det[0] == "\n":
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0
        if det[1][:-1] == "device":
            self.runningNot.setText("DEVICE " + str(det[0]) + " IS CONNECTED")
            self.progressBar.setValue(10)

        elif det[1][:-1] == "unauthorized":
            self.runningNot.setText("DEVICE IS UNAUTHORIZED. PLEASE CLICK 'OK' ON DEVICE WHEN ASKED FOR")
            self.progressBar.setValue(0)
            return 0

        else:
            self.runningNot.setText("DEVICE CONNECTED BUT FAILED TO ESTABLISH CONNECTION")
            self.progressBar.setValue(0)
            return 0
        # check if the defaultDimension is checked or not for giving signal
        # ADB READ DIMENSIONS :: BEGIN
        adb_dim = po("adb shell wm size", shell=True, stdout=PIPE, stderr=PIPE)
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
            dimension = None
            dimension0 = None

        else:
            self.dimensionSlider.setEnabled(True)
            dimension = int(self.dimensionSlider.value())
            dimension0 = int(self.dimensionSlider.value())
            self.dimensionText.setText(str(dimension) + "px")

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
        if dimension is None:
            self.options = " "
            pass
        elif dimension is not None:
            self.options = " -m " + str(dimension)
        else:
            self.options = ""

        self.progressBar.setValue(25)
        # CHECK BOX GROUP CONNECT
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
            fullscreen0 = True
        else:
        	fullscreen0 = False
        """
        if self.keepdisplayRO.isChecked():
            self.options += " --no-control"
        """
        self.progressBar.setValue(30)
        if self.showTouches.isChecked():
            self.options += " --show-touches"
            swtouches0 = True

            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """

        else:
            swtouches0 = False
        if self.recScui.isChecked():
            self.options += " -r "+str(int(time.time()))+".mp4 "
            
            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """
        if self.displayForceOn.isChecked():
            self.options += " -S"
            dispRO0 = True
            """        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
            """

        else:
            dispRO0 = False


        self.options += " -b " + str(int(self.dial.value())) + "K"
        bitrate0 = str(int(self.dial.value()))
        self.progressBar.setValue(40)

        # implies program not idle

        """
        if(value == 91):
            print("DEVICE NOT DETECTED [ERROR]")
            self.runningNot.setText("DEVICE NOT DETECTED")
        else:
            print("DEVICE DETECTED")
            self.runningNot.setText("SCRCPY CONNECTED")
        """
        # TODO

        # self.myLine = startScrcpy(self.options)
        # self.connect(self.myLine, SIGNAL("update_terminal(QString)"), self.update_terminal)
        print("CONNECTION ESTABLISHED")
        self.progressBar.setValue(50)
        """
        for line in iter(backup.stdout.readline, b''): # TODO NOT IMPLEMENTED
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)
            output = '\n'.join(full)
            self.terminal.setText(str(output))
        """
        print("FLAGS PASSED : " + self.options)
        self.progressBar.setValue(75)
        backup = po("bash -c 'scrcpy" + str(self.options)+"'",
                                  shell=True,
                                  stdin=PIPE,
                                  stdout=PIPE,
                                  stderr=STDOUT)
        # StartScrcpy(options=self.options)
        
        timef = time.time()
        eta = timef-timei
        print("SCRCPY is launched in", eta, "seconds")
        self.progressBar.setValue(100)

        # self.terminal.setText(full)
        cfg = open(os.path.expanduser("~/guiscrcpy.cfg"), "w+")
        print("writing: #" * 25 + "\n", "Created by Srevin Saju\n", "#" * 25 + "\n", str(time.time()) + "\n",
                        str(bitrate0) + "\n", str(dimension0) + "\n", str(swtouches0) + "\n",
                        str(fullscreen0) + "\n" + str(dispRO0) + "\n")
        cfg.writelines(("#" * 25 + "\n", "Created by Srevin Saju\n", "#" * 25 + "\n", str(time.time()) + "\n",
                        str(bitrate0) + "\n", str(dimension0) + "\n", str(swtouches0) + "\n",
                        str(fullscreen0) + "\n" + str(dispRO0) + "\n"))

        cfg.close()
        """
        p5 = multiprocessing.Process(target=update_terminal)
        p5.start()
        p5.join()
        """










if __name__ == "__main__":
        	
        app = QtWidgets.QApplication(sys.argv)
	
        # file = QFile(":/dark.qss")
        #file.open(QFile.ReadOnly | QFile.Text)
        # stream = QTextStream(file)
        # app.setStyleSheet(stream.readAll())
        splash_pix = QPixmap(':/res/ui/guiscrcpy-branding.png')
        splash = QtWidgets.QSplashScreen(splash_pix)
        splash.setMask(splash_pix.mask())
        splash.show()
        app.processEvents()
        adb_chk0 = po("adb devices -l", shell=True, stdout=PIPE, stderr=PIPE)
        time.sleep(1)
        app.processEvents()
        print("output:", adb_chk0.stdout)
        """
	Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
	Ui_Dialog = uic.loadUiType(qtCreatorFile)
	"""

        window = QtWidgets.QMainWindow()
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        windoww = QtWidgets.QMainWindow()
        windowww = QtWidgets.QMainWindow()
        prog = MyApp(window)
        panel = Panel(windoww)
        progg = MyAppv(windowww)
        window.show()
        splash.hide()
        windowww.show()
        windoww.show()
        app.exec_()
        print("POS:", window.pos())
        # appo.exec_()
        sys.exit()

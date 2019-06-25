#
"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy
Licensed under GNU Public License

Build 1.9.2

CHANGELOG:
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
"""
import multiprocessing
import os
import subprocess
import sys
import time

from toolUI import Ui_Dialog

try:
    import psutil
except ModuleNotFoundError:
    print("psutil is not installed in the python3 directory. "
          "Install with $ pip3 install psutil")

try:
    from PyQt5 import QtCore, QtGui, uic, QtWidgets
    from PyQt5.QtCore import *
except ModuleNotFoundError:
    print("PyQt5 is not installed. Please install it with pip install PyQt5 pyside2."
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

from mainui import Ui_MainWindow

#

#

build = "1.9.5"
qtCreatorFile = "mainwindow.ui"  # Enter file here.
"""
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
Ui_Dialog = uic.loadUiType(qtCreatorFile)
"""
try:
    cfg = open("usercfgGUISCRCPY.cfg", "r")
    fileExist = False
except FileNotFoundError or FileExistsError:
    cfg = open("usercfgGUISCRCPY.cfg", "w+")
    fileExist = True
    cfg.close()


# BEGIN TOOLKIT.UI
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
        os.system("xdotool key --clearmodifiers ctrl+p")


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


class MyAppv(Ui_Dialog):
    def __init__(self, Dialog):
        super(MyAppv, self).__init__()
        Ui_Dialog.__init__(self)
        self.setupUi(Dialog)
        self.clipD2PC.released.connect(clipd2pc)
        self.clipPC2D.released.connect(clippc2d)
        self.back.released.connect(Back)
        self.appswi.released.connect(switch)
        self.menuUI.released.connect(menu)
        self.home.released.connect(homekey)
        self.notif_pull.released.connect(notifExpand)
        self.fullscreenUI.released.connect(fullscreen)


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


class StartScrcpy(QThread):
    print("Hello")

    def __init__(self, options):
        QThread.__init__(self)
        print("SCRCPY launch")

        backup = subprocess.Popen("scrcpy" + str(options),
                                  shell=True,
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

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

        tmp = ""
        dimension = None
        bit_rate = 8000  # default

        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        # self.setupUi(self)
        # self.menuAbout.itemPressed.connect(self.menu_about)

        # check if process Scrcpy is running right now in while loop

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
        self.bitrateText.setText(str(bit_rate) + "KB/s")

    def quitAct(self):
        sys.exit()

    def menu_about(self):
        pass

    def dimensionChange(self):

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            dimension = None
            self.dimensionText.setText("DEFAULT")

        else:
            self.dimensionSlider.setEnabled(True)
            dimension = int(self.dimensionSlider.value())
            self.dimensionText.setText(str(dimension) + "px")
            self.dimensionSlider.sliderMoved.connect(self.slider_text_refresh)
            self.dimensionSlider.sliderReleased.connect(self.slider_text_refresh)

    def slider_text_refresh(self):
        dimension = int(self.dimensionSlider.value())
        self.dimensionText.setText(str(dimension) + "px")
        pass

    def dial_text_refresh(self):
        bit_rate = int(self.dial.value())
        self.bitrateText.setText(str(bit_rate) + "KB/s")
        pass

    def start_act(self):

        # check if the defaultDimension is checked or not for giving signal
        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.dimensionText.setText("DEFAULT")
            dimension = None

        else:
            self.dimensionSlider.setEnabled(True)
            dimension = int(self.dimensionSlider.value())
            self.dimensionText.setText(str(dimension) + "px")
        # check if the defaultDimension is checked or not for giving signal

        """
        proc = subprocess.run(["scrcpy"], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
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

        # CHECK BOX GROUP CONNECT
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
        """
        if self.keepdisplayRO.isChecked():
            self.options += " --no-control"
        """
        if self.showTouches.isChecked():
            self.options += " --show-touches"
        if self.keepdisplayRO.isChecked():
            self.options += " --turn-screen-off"
        self.options += " -b " + str(int(self.dial.value())) + "K"

        # implies program not idle
        value = 0
        for i in range(0, 100):
            time.sleep(0.01)

            value += i * 1
            self.progressBar.setValue(value)
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
        print("RECEIVED")
        """
        for line in iter(backup.stdout.readline, b''): # TODO NOT IMPLEMENTED
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)
            output = '\n'.join(full)
            self.terminal.setText(str(output))
        """
        print(self.options)
        StartScrcpy(options=self.options)

        # self.terminal.setText(full)

    """
    p5 = multiprocessing.Process(target=update_terminal)
    p5.start()
    p5.join()
    """


if __name__ == "__main__":
    def proc8():
        app = QtWidgets.QApplication(sys.argv)
        # app.aboutToQuit().connect(app.deleteLater)
        window = QtWidgets.QMainWindow()
        prog = MyApp(window)
        window.show()
        app.exec_()


    def proc9():
        appo = QtWidgets.QApplication(sys.argv)
        # app.aboutToQuit().connect(app.deleteLater)
        windoww = QtWidgets.QMainWindow()
        progg = MyAppv(windoww)
        windoww.show()
        appo.exec_()


    p8 = multiprocessing.Process(target=proc8)
    p9 = multiprocessing.Process(target=proc9)
    p8.start()
    p9.start()
    p8.join()
    p9.join()

    sys.exit()

#
"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy
Licensed under GNU Public License

Build 1.9.2

CHANGELOG:
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
import platform
import subprocess
import sys
import time

import psutil
from PyQt4 import QtGui, uic
from PyQt4.QtCore import QThread

#

#

build = "1.9.4"
qtCreatorFile = "mainwindow.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

try:
    cfg = open("usercfgGUISCRCPY.cfg", "r")
    fileExist = False
except FileNotFoundError or FileExistsError:
    cfg = open("usercfgGUISCRCPY.cfg", "w+")
    fileExist = True
    cfg.close()


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


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        tmp = ""
        dimension = None
        bit_rate = 8000  # default

        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
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

    def quitAct(self):
        sys.exit()

    def menu_about(self):
        self.terminal.setText("GUISCRCPY :: Build " + str(build) +
                              "\nCREDITS :\nromv1 for scrcpy c++ "
                              "engine\nsrevinsaju for scrcpy GUI integration")

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
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()


    def launchmain():
        app.exec_()


    def launchtoolkit():
        if platform.system() == "Windows":
            p = subprocess.Popen("python " + str(os.getcwd()) + r"\toolkit.py", shell=True)
        if platform.system() == "Linux":
            p = subprocess.Popen("python3 " + str(os.getcwd()) + r"/toolkit.py", shell=True)
        if platform.system() == "MacOS":
            print("Hmm.. I don't know Mac stuff, please contribute on https://github.com/srevinsaju/guiscrcpy")


    ltk = multiprocessing.Process(target=launchtoolkit)
    main1 = multiprocessing.Process(target=launchmain)
    main1.start()
    time.sleep(1)
    ltk.start()
    main1.join()
    ltk.join(50)

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

import subprocess
import sys
import time

import psutil
from PyQt4 import QtGui, uic

#

#

build = "1.9.1"
qtCreatorFile = "mainwindow.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

try:
    cfg = open("usercfgGUISCRCPY.cfg", "r")
    fileExist = False
except FileNotFoundError or FileExistsError:
    cfg = open("usercfgGUISCRCPY.cfg", "w+")
    fileExist = True
    cfg.close()




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
            options = " "
            pass
        elif dimension is not None:
            options = " -m " + str(dimension)
        else:
            options = " "

        # CHECK BOX GROUP CONNECT
        if self.aotop.isChecked():
            options += " -T "
        if self.fullscreen.isChecked():
            options += " -f "
        if self.keepdisplayRO.isChecked():
            options += " -n "
        if self.showTouches.isChecked():
            options += " -t "
        if self.displayForceOn.isChecked():
            options += " -S "

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

        full = []

        toolkit.window.show()
        backup = subprocess.Popen("scrcpy" + str(options),
                                  shell=True,
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)

        # this block is for instantaneous reading the output
        for line in iter(backup.stdout.readline, b''):
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)

        output = '\n'.join(full)
        # block ends out
        if checkProcessRunning("scrcpy"):
            print("SCRCPY RUNNING")
            self.runningNot.setText("SCRCPY SERVER RUNNING")
        else:
            print("SCRCPY SERVER IS INACTIVE")
            self.runningNot.setText("SCRCPY SERVER NOT RUNNING")

        self.terminal.setText(str(output))  # set text to terminal


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

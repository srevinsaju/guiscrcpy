#
"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy

"""
import subprocess
import sys

from PyQt4 import QtGui, uic

build = 2.0
qtCreatorFile = "mainwindow.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        tmp = ""
        dimension = None
        bit_rate = 8000  # default

        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(self.dimensionChange)

        # CHECK BOX GROUP CONNECT
        self.

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.dial_text_refresh)
        self.dial.sliderReleased.connect(self.dial_text_refresh)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)

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
        backup = subprocess.Popen("scrcpy" + str(options),
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        full = []

        # this block is for instantaneous reading the output
        for line in iter(backup.stdout.readline, b''):
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)

        output = '\n'.join(full)
        # block ends out

        self.terminal.setText(str(output))  # set text to terminal


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

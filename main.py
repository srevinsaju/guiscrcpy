"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/sevinsaju/guiscrcpy

"""
import subprocess
import sys

from PyQt4 import QtGui, uic

qtCreatorFile = "mainwindow.ui"  # Enter file here.
tmp = []
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        tmp = ""
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.executeaction.clicked.connect(self.start_act)

    def start_act(self, ):
        bit_rate = int(self.dial.value())
        tax = (self.dimensionSlider.value())
        """
        proc = subprocess.run(["scrcpy"], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        out, err = proc.stdout, proc.stderr
        out_decoded = out.decode("utf-8")
        tmp.append(out_decoded)
        self.terminal.setText(str(tmp))
        """
        backup = subprocess.Popen("scrcpy", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        full = []
        for line in iter(backup.stdout.readline, b''):
            line = line.rstrip().decode('utf8')
            print(">>>", line)
            full.append(line)

        output = '\n'.join(full)
        self.terminal.setText(str(output))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

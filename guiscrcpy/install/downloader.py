
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import urllib.request
import sys
import threading


dlThread = 0
hWindow = 0
fProgressCounter = 0.0

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        global hWindow
        hWindow = self

        lblUrl = QLabel("File URL:")
        self.txtURL = QLineEdit()
        self.bttDL = QPushButton("&Download")
        self.pbar = QProgressBar()

        self.pbar.setMinimum(0)
        self.pbar.setMaximum(100)

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(lblUrl)
        buttonLayout1.addWidget(self.txtURL)
        buttonLayout1.addWidget(self.bttDL)
        buttonLayout1.addWidget(self.pbar)

        self.bttDL.clicked.connect(self.bttPush)

        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("pySFD")
    def bttPush(self):
        global dlThread

        hSignals = sigHandling()
        hSignals.dlProgress_update.connect(hSignals.pbar_incrementer)
        hSignals.dlProgress_done.connect(hSignals.dlDone)

        url = self.txtURL.text()
        if url == "":
            QMessageBox.information(self, "Empty URL",
                    "Please enter the URL of the file you want to download.")
            return
        else:
            filename = str(QFileDialog.getSaveFileName(self, 'Choose the download location and file name', '.')) ## DETECT A CANCEL
            filename = filename[:-6]
            filename = filename.split("('",maxsplit=1)[1]

        self.bttDL.setEnabled(False)
        dlThread = threading.Thread(target=hSignals.runDL,args=(url, filename))
        dlThread.start()
        return

    def pbarIncValue(self, val):
        global fProgressCounter
        #print("pbarIncValue({0})\nfProgressCounter={1}".format(val,fProgressCounter))

        if self.pbar.value() >= 100:
            self.dlProgress_done.emit()
            return
        if fProgressCounter > 1.0: # FIX
            self.pbar.setValue(self.pbar.value() + 1)
            fProgressCounter -= 1.0
            fProgressCounter += val
        else:
            fProgressCounter += val

class sigHandling(QObject):
    dlProgress_update = pyqtSignal(float)
    dlProgress_done = pyqtSignal()

    @pyqtSlot(float)
    def pbar_incrementer(self, val):
        hWindow.pbarIncValue(val)

    @pyqtSlot()
    def dlDone(self):
        print("in dlDone")
        hWindow.pbar.setValue(100)
        hWindow.bttDL.setEnabled(True)

    def runDL(self, dlLink, filename):
        #print("in run")
        global dlThread, hWindow
        def report(block_count, block_size, total_size):
            if block_count == 0:
                #print("block_count == 0")
                self.dlProgress_update.emit(0)
            if (block_count * block_size) == total_size:
                self.dlProgress_done.emit()
            incAmount = float((100*block_size) / total_size)
            #print("BS={0} TS={1} incAmount={2}".format(block_size,total_size,incAmount))
            self.dlProgress_update.emit(incAmount)

        urllib.request.urlretrieve(dlLink, filename, reporthook=report)
        #print("emit dlProgress_done")
        self.dlProgress_done.emit()
        #print("about to leave dlThread")
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
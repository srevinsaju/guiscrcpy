import os
import sys
from PyQt5.QtWidgets import QFileDialog


def openFileNameDialog(parent, appname):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = \
        QFileDialog.getOpenFileName(parent, "{} could not be found. Please locate it manually".format(appname),
                                    "", "Valid {} executable (*);;".format(appname), options=options)
    if fileName:
        print(fileName)
        return fileName

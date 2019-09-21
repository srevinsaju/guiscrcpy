import subprocess
import sys
from notifUI import Ui_Dialog
from PyQt5 import QtCore, QtGui, uic, QtWidgets


def chkRUN():
    adb_chk = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE)
    output = adb_chk.stdout.readlines()
    needed_output = output[1]

    deco = needed_output.decode("utf-8")
    det = deco.split("\t")
    if det[0] == "\n":
        return 0
    if det[1][:-1] == "device":
        return True
    elif det[1][:-1] == "unauthorized":
        return 0
    else:
        return 0


class MyApp(Ui_Dialog):
    def __init__(self, Dialog):
        super(MyApp, self).__init__()
        Ui_Dialog.__init__(self)
        self.setupUi(Dialog)

        self.readNotif()

    def readNotif(self):
        while chkRUN():
            notifReadOut = subprocess.Popen("adb shell dumpsys notification | grep ticker | cut -d= -f2",
                                            shell=True, stdout=subprocess.PIPE)
            output = notifReadOut.stdout.readlines()
            exist = 0
            for i in output:
                deco = i[:-1].decode("utf-8")
                print(deco)
                if deco=="null":
                    exist = 1
                    continue

                self.listWidget.addItems([deco])
            if exist:
                self.listWidget.addItems(["You may have more notifications."
                                          " guiscrcpy do not have enough permissions to view them."])
        else:
            self.listWidget.addItems(["You have no notifications here!"])


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    # app.aboutToQuit().connect(app.deleteLater)
    window = QtWidgets.QMainWindow()

    prog = MyApp(window)

    window.show()

    app.exec_()

    sys.exit()


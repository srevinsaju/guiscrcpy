"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog

from guiscrcpy.ux import Ui_SettingsWindow


class InterfaceSettings(QMainWindow, Ui_SettingsWindow):
    # there was a Dialog in the bracket
    def __init__(self, parent):
        QMainWindow.__init__(self)
        Ui_SettingsWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.commands = []
        self.checkboxes = {
            self.a1: [[None], "--always-on-top", 0],
            self.a2: [[self.a2c1, self.a2c2], "--crop {}:{}", 1],
            self.a3: [[self.a3e1], "--max-fps {}"],
            self.a4: [[None], "--prefer-text"],
            self.a5: [[self.a5c1], "--push-target {}"],
            self.a6: [[self.a6c1], "--record {}"],
            self.a8: [[self.a8c1], "--serial {}"],
            self.a9: [[None], "--window-borderless"],
            self.b0: [[self.b0c1], "--window-title {}"],
            self.b1: [[self.b1c1, self.b1c1], "--window-x {} --window-y {}"],
            self.b2: [[self.b2c1, self.b2c2], "--window-width {} --window-height {}"],
        }

    def init(self):
        self.updatebutton.clicked.connect(self.complete)
        self.a6d1.clicked.connect(self.file_chooser)
        self.show()

    def file_chooser(self):
        dialog = QFileDialog()
        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)
        dialog.setDefaultSuffix("mp4")
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setNameFilters(["H.264 (*.mp4)", "MKV (*.mkv)"])
        if dialog.exec_() == QDialog.Accepted:
            self.a6c1.setText(dialog.selectedFiles()[0])

    def checkboxes_act(self, args):
        pass

    def complete(self):
        x = []
        for i in self.checkboxes:
            if i.isChecked():
                box = self.checkboxes[i]
                cmd = box[1]
                cmd_args = []
                for j in box[0]:
                    if j is None:
                        break
                    else:
                        try:
                            arg = j.text()
                            print(arg)
                        except (AttributeError, NameError, ValueError):
                            arg = j.value()
                            print(arg)
                        cmd_args.append(arg)
                else:
                    cmd = cmd.format(*cmd_args)
                print(cmd)
                x.append(cmd)
        print(x)
        self.hide()
        self.parent.cmx = x

    def cancel(self):
        pass

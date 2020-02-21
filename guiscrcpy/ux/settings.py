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
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow

from guiscrcpy.ui.settings import Ui_MainWindow
from guiscrcpy.settings.settings import SettingsManager


class InterfaceSettings(QMainWindow, Ui_MainWindow):
    # there was a Dialog in the bracket
    def __init__(self, parent):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.commands = []
        self.checkboxes = {
            self.a1: [[None], '--always-on-top', 0],
            self.a2: [[self.a2c1, self.a2c2], '--crop {}:{}', 1],
            self.a3: [[self.a3e1], '--max-fps {}'],
            self.a4: [[None], '--prefer-text'],
            self.a5: [[self.a5c1], '--push-target {}'],
            self.a6: [[self.a6c1, self.a6c1], '--record {}'],
            self.a8: [[self.a8c1], '--serial {}'],
            self.a9: [[None], '--window-borderless'],
            self.b0: [[self.b0c1], '--window-title'],
            self.b1: [[self.b1c1, self.b1c1], '--window-x {} --window-y {}'],
            self.b2: [[self.b2c1, self.b2c2], '--window-width {} --window-height {}'],
        }

    def init(self):
        for i in self.checkboxes:
            self.checkboxes[i].clicked.connect(lambda k=i: self.updatelist(k))
        self.upda
        self.show()

    def checkboxes_act(self, args):
        pass

    def updatelist(self, args):
        # TODO Restore values
        # ' '.join(map(str, s))
        if self.checkboxes[args][0][0] is None:
            self.commands.append("{}".format(self.checkboxes[args][1]))
        else:
            text = "{}".format(self.checkboxes[args][1])
            x = []
            for i in self.checkboxes[args][0]:
                try:
                    x.append(i.text())
                except Exception as e:
                    x.append(i.value())
            self.commands.append(text.format(*x))
        pass

    def complete(self):
        pass

    def cancel(self):
        pass

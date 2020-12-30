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
import uuid

from qtpy import QtCore
from qtpy.QtCore import QPoint
from qtpy.QtWidgets import QMainWindow

from guiscrcpy.lib.toolkit import UXMapper
from guiscrcpy.ux import Ui_HorizontalPanel


class Panel(QMainWindow, Ui_HorizontalPanel):
    # there was a Dialog in the bracket
    def __init__(self, parent=None, ux_mapper=None, frame=False, always_on_top=True):
        """
        The bottom panel subwindow class for guiscrcpy
        :param parent: The caller of the function
        :param ux_mapper: The UX Mapper toolkit
        :param frame: Boolean (Frame window / Frameless Window)
        :param always_on_top: Boolean (always on top)
        """
        # noinspection PyArgumentList
        QMainWindow.__init__(self)
        Ui_HorizontalPanel.__init__(self)
        self.name = "panel"
        self.uid = uuid.uuid4()
        self.setupUi(self)
        self.parent = parent
        self.oldPos = self.pos()
        __flags = QtCore.Qt.Window
        if not frame:
            __flags |= QtCore.Qt.FramelessWindowHint
        if always_on_top:
            __flags |= QtCore.Qt.WindowStaysOnTopHint
        self.setWindowFlags(__flags)
        if ux_mapper:
            self.ux = ux_mapper
        else:
            self.ux = UXMapper()

    def init(self):
        self.bp_close.clicked.connect(self.quit_window)
        self.backk.clicked.connect(self.ux.key_back)
        self.menuUII.clicked.connect(self.ux.key_menu)
        self.homee.clicked.connect(self.ux.key_home)
        self.powerUII.clicked.connect(self.ux.key_power)
        self.vupp.clicked.connect(self.ux.key_volume_up)
        self.vdownn.clicked.connect(self.ux.key_volume_down)
        self.colorize()
        self.show()

    def colorize(self):
        hexdigest = self.ux.get_sha()[:6]
        self.bp_device_id.setStyleSheet(f"background-color: #{hexdigest};")

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)

            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except (TypeError, AttributeError):
            pass

    def quit_window(self):
        for instance in self.parent.child_windows:  # noqa
            # We are checking for any more windows running before killing
            # the main window. self.child_windows has the list of all
            # objects spawned by the main window ui
            # This method checks if we are the last member of the windows
            # spawned and we ourselves are not a member of ourself by
            # checking the uuid generated on creation
            if (
                not instance.isHidden()
                and instance.name != "swipe"
                and instance.uid != self.uid
            ):
                self.hide()
                break
        else:
            for instance in self.parent.child_windows:  # noqa
                if (
                    instance.name == "swipe"
                    and instance.ux.get_sha() == self.ux.get_sha()
                ):
                    instance.hide()
            self.hide()

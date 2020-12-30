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
from qtpy.QtWidgets import QMessageBox
from qtpy import QtGui, QtCore, QtWidgets
from qtpy.QtCore import Qt
from qtpy.QtGui import QPixmap


class MapperUI(QtWidgets.QWidget):
    """
    Guiscrcpy Mapper User Interface
    configuration an button
    mapping
    """

    def __init__(
        self,
        core,
        screenshot_path,
        dimensions,
        fixed_pos=[0.0, 0.0],
        final_pos=[0.0, 0.0],
    ):
        self.fixed_pos = fixed_pos
        self.final_pos = final_pos
        self.core = core
        self.last_found_point = None
        self.image = None
        QtWidgets.QWidget.__init__(self)
        self.build_user_interface()
        self.screenshot_path = screenshot_path
        self.dimensions = dimensions
        self.set_screenshot_to_label(self.screenshot_path)

    def build_user_interface(self):
        self.label = QtWidgets.QLabel(self)
        self.drawing = False
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 351, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(size_policy)
        self.lineEdit.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(25, 16777215))
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label0 = QtWidgets.QLabel(self.widget)
        self.label0.setMinimumSize(QtCore.QSize(25, 25))
        self.label0.setStyleSheet(
            "color: rgb(0, 0, 0);\n"
            "border-radius: 10px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, "
            "y2:1, stop:0 rgba(61, 255, 0, 255), stop:1 rgba(226, 255, 0, "
            "255));\n "
        )
        self.label0.setAlignment(QtCore.Qt.AlignCenter)
        self.label0.setObjectName("label")
        self.horizontalLayout.addWidget(self.label0)
        self.pushButton.pressed.connect(self.register_key)
        self.label.setSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        self.label.resize(800, 600)
        self.setContentsMargins(0, 0, 0, 0)
        self.label.setContentsMargins(0, 0, 0, 0)

    def set_screenshot_to_label(self, screenshot_path):
        """
        Sets the pixmap of a QLabel to the path provided by the screenshot path
        :param screenshot_path: the full path to the screenshot file (*.png)
        :type screenshot_path: str
        :return: None
        :rtype: None
        """
        self.pixmap = QtGui.QPixmap(screenshot_path)
        self.label.resize(
            int(0.5 * self.pixmap.width()), int(0.5 * self.pixmap.height())
        )
        self.resize(int(0.5 * self.pixmap.width()), int(0.5 * self.pixmap.height()))

        self.show()
        self.resize(self.label.size())
        self.label.setPixmap(self.pixmap)
        self.label.setMinimumSize(1, 1)
        self.label.setMaximumSize(
            int(0.5 * self.pixmap.width()), int(0.5 * self.pixmap.height())
        )
        self.setMaximumSize(
            int(0.5 * self.pixmap.width()), int(0.5 * self.pixmap.height())
        )
        self.label.installEventFilter(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        self.pushButton.setText("OK")
        self.label0.setWordWrap(True)
        self.label0.setText(
            "Click the point, and enter char in textbox and " "press OK to continue."
        )

    def register_key(self):
        relx = self.fixed_pos[0] / self.label.width()
        rely = self.fixed_pos[1] / self.label.height()
        fixx = relx * int(self.dimensions[0])
        fixy = rely * int(self.dimensions[1])
        char = self.lineEdit.text()[:1]
        print(
            "Successfully registered {ch} "
            "with position  ({x}, {y})".format(ch=char, x=fixx, y=fixy)
        )
        self.core.add_position(char, (fixx, fixy))
        self.label0.setText(
            "SUCCESS! "
            "Add a new point and enter char; "
            "close the window to finish adding."
        )

    def eventFilter(self, source, event):
        if source is self.label and event.type() == QtCore.QEvent.Resize:
            self.label.setPixmap(
                self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            )
        return super(MapperUI, self).eventFilter(source, event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_found_point = event.pos()
            self.fixed_pos[0] = int(event.pos().x())
            self.fixed_pos[1] = int(event.pos().y())
            print(self.last_found_point, "LAST")
            self.last_found_point = self.label.mapFromParent(
                event.pos()
            )  # this is working fine now
            # self.label.setPixmap(QPixmap.fromImage(self.image))

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            # painter.setPen(QPen(self.brushColor,
            # self.brushSize, Qt.SolidLine, Qt.RoundCap,Qt.RoundJoin))
            # painter.drawLine(
            # self.label.mapFromParent(event.pos()),self.last_found_point)
            self.last_found_point = self.label.mapFromParent(
                event.pos()
            )  # this is working fine now
            print(self.last_found_point, "MOVE")
            self.fixed_pos[0] = int(event.pos().x())
            self.fixed_pos[1] = int(event.pos().y())
            # self.label.setPixmap(QPixmap.fromImage(self.image))

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            # self.drawing = False
            self.label.setPixmap(QPixmap.fromImage(self.image))

    def closeEvent(self, event):
        # do stuff
        message_box = QMessageBox()
        message_box.setText("Save changes and exit?")
        vals = ["{} → {}".format(x, self.core.config[x]) for x in self.core.config]
        message_box.setInformativeText(
            "Mapper has unsaved mappings: {val}. Do you want to save the "
            "current mappings?".format(val=", ".join(vals))
        )
        message_box.setStandardButtons(
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        )
        user_message_box_response = message_box.exec()
        if user_message_box_response == QMessageBox.Yes:
            print("Registration process completed.")
            print("Registered mappings are : ", self.core.config)
            print("Writing configuration file...")
            self.core.create_configuration()
            print("Mapper completed successfully!")
            event.accept()
        elif user_message_box_response == QMessageBox.No:
            print("Not saving mapper configuration to json file")
            event.accept()
        else:
            event.ignore()

from subprocess import PIPE, Popen
from pynput import keyboard

from PyQt5 import QtGui, QtCore, QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.label = QtWidgets.QLabel(self)

        def on_press(key):
            try:

                if key.char == ",":
                    a = Popen(
                        "adb shell screencap -p /sdcard/scr.png",
                        shell=True,
                        stdout=PIPE,
                    )
                    b = Popen("adb pull /sdcard/scr.png", shell=True, stdout=PIPE)
                    c = Popen("gwenview scr.png", shell=True, stdout=PIPE)

                    print(a.stdout)
            except AttributeError:
                print("special key {0} pressed".format(key))

        def on_release(key):
            print("{0} released".format(key))
            if key == keyboard.Key.esc:
                # Stop listener
                return False

        # Collect events until released
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()

        self.label.setSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        self.label.resize(800, 600)
        self.label.setContentsMargins(0, 0, 0, 0)
        self.pixmap = QtGui.QPixmap("scr.png")
        self.label.setPixmap(self.pixmap)
        self.label.setMinimumSize(1, 1)
        self.label.installEventFilter(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)

    def eventFilter(self, source, event):
        if source is self.label and event.type() == QtCore.QEvent.Resize:
            self.label.setPixmap(
                self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio)
            )
        return super(Window, self).eventFilter(source, event)


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    window.resize(800, 600)
    sys.exit(app.exec_())

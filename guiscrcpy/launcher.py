#!/usr/bin/env python3

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


Icon made by Dave Gandy from www.flaticon.com used under
Creative Commons 3.0 Unported. The original SVG black work
by Dave Gandy has been re-oriented, flipped or color-changed.
The rest of Terms and Conditions put forward by
CC-3.0:Unported has been feverently followed by the developer.
Icons have been adapted in all the three windows.

Icons pack obtained from www.flaticon.com
All rights reserved.

"""

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
import sys
import argparse
import logging
import webbrowser
import time
from datetime import datetime
from subprocess import Popen as po
import os
import os.path
from subprocess import PIPE
from guiscrcpy.lib.config import InterfaceConfig
from guiscrcpy.lib.process import is_running
from guiscrcpy.lib.ver import version
from guiscrcpy.platform import platform
from guiscrcpy.theme.decorate import header
from guiscrcpy.lib.check import adb
from guiscrcpy.lib.check import scrcpy
from guiscrcpy.theme.style import darkstylesheet
from guiscrcpy.ui.main import Ui_MainWindow
from guiscrcpy.lib.toolkit import UXMapper
from guiscrcpy.ux.panel import Panel
from guiscrcpy.ux.swipe import SwipeUX
from guiscrcpy.ux.toolkit import InterfaceToolkit

try:
    os.chdir(os.path.dirname(__file__))
except FileNotFoundError:
    pass  # Its a PyInstaller compiled package

# create app


# initialize config manager
cfgmgr = InterfaceConfig()
config = cfgmgr.get_config()
environment = platform.System()
adb.path = config['adb']
scrcpy.path = config['scrcpy']
scrcpy.server_path = config['scrcpy-server']
v = version()

# Initialize argument parser
parser = argparse.ArgumentParser('guiscrcpy v{}'.format(v.get_commit()))
parser.add_argument('-i', '--install', action='store_true',
                    help="Install guiscrcpy system wide on Linux")
parser.add_argument('-s', '--start', action='store_true',
                    help="Start scrcpy first before loading the GUI")
parser.add_argument('-o', '--output', action='store_true',
                    help="Show logging output in stdout as well as in .log file")
parser.add_argument('-d', '--debug', default=3,
                    help="Set a logging level from 0,1,2,3,4,5")
parser.add_argument('-v', '--version', action='store_true',
                    help="Display guiscrcpy version")
args = parser.parse_args()

# set argument debug level
if args.debug:
    logging_priority = int(args.debug) * 10
else:
    logging_priority = 30

# configure logging settings
logging.basicConfig(
    filename=os.path.join(cfgmgr.get_cfgpath(),
                          'guiscrcpy_log_{}.log'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))),
    filemode='w',
    level=logging_priority,
    format='%(levelname)s :: %(message)s'
)

# show terminal output
if args.output:
    logging.getLogger().addHandler(logging.StreamHandler())

# try using pynput, if exception handling not done here, it might fail in CI
try:
    from pynput import keyboard
except Exception as e:
    logging.warning("Running from tty, pass. E:{}".format(e))
    keyboard = None


# FIXME move to version.py
pass

logging.debug("Received flag {}".format(args.start))

header(v.get_commit())

if args.version:
    sys.exit(0)

logging.debug("Current Working Directory {}".format(os.getcwd()))

if args.start:
    logging.debug("RUNNING SCRCPY DIRECTLY")
    args = ""
    args += " -b " + str(config['bitrate'])
    if config['fullscreen']:
        args += " -f "
    if config['swtouches']:
        args += " -t "
    if config['dispRO']:
        args += " --turn-screen-off "
    scrcpy.start(scrcpy.path, args)

logging.debug("Importing modules...")


class InterfaceGuiscrcpy(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.cmx = None
        logging.debug(
            "Options received by class are : {} {} {} {} {} ".format(
                config['bitrate'],
                config['dimension'],
                config['swtouches'],
                config['dispRO'],
                config['fullscreen'],
            ))
        self.dial.setValue(int(config['bitrate']))
        if config['swtouches']:
            self.showTouches.setChecked(True)
        else:
            self.showTouches.setChecked(False)
        if config['dispRO']:
            self.displayForceOn.setChecked(True)
        else:
            self.displayForceOn.setChecked(False)
        if config['dimension'] is not None:
            self.dimensionDefaultCheckbox.setChecked(False)
            try:
                self.dimensionSlider.setValue(config['dimension'])
            except TypeError:
                self.dimensionDefaultCheckbox.setChecked(True)
        if config['fullscreen']:
            self.fullscreen.setChecked(True)
        else:
            self.fullscreen.setChecked(False)
        if is_running("scrcpy"):
            logging.debug("SCRCPY RUNNING")
            self.runningNot.setText("SCRCPY SERVER RUNNING")
        else:
            logging.debug("SCRCPY SERVER IS INACTIVE")
            self.runningNot.setText("SCRCPY SERVER NOT RUNNING")

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(
            self.dimensionChange)
        self.build_label.setText("Build " + str(v.build))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.dial_text_refresh)
        self.dial.sliderReleased.connect(self.dial_text_refresh)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)
        try:
            if config['extra']:
                self.flaglineedit.setText(config['extra'])
            else:
                pass
        except:
            pass

        # show subwindows
        self.swipe_instance = SwipeUX()  # Load swipe UI
        self.panel_instance = Panel()
        self.side_instance = InterfaceToolkit()
        self.quit.clicked.connect(self.quitAct)
        self.dimensionText.setText("DEFAULT")
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(" " + str(config['bitrate']) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtme.clicked.connect(self.openme)
        self.abtgit.clicked.connect(self.opengit)
        self.usbaud.clicked.connect(self.usbaudi)
        self.mapnow.clicked.connect(self.mapp)
        self.network_button.clicked.connect(self.network_mgr)
        self.settings_button.clicked.connect(self.settings_mgr)

    def settings_mgr(self):
        from guiscrcpy.ux.settings import InterfaceSettings
        self.sm = InterfaceSettings(self)
        self.sm.init()
        self.sm.show()

    def network_mgr(self):
        from guiscrcpy.ux.network import InterfaceNetwork
        self.nm = InterfaceNetwork(adb.path)
        self.nm.init()
        self.nm.show()

    def mapp(self):
        if (os.path.exists(
                os.path.join(cfgmgr.get_cfgpath() + "guiscrcpy.mapper.json"))):
            from guiscrcpy.lib import mapper
            mapper.file_check()
        else:
            logging.warning(
                "guiscrcpy ~ mapper is not initialized. Initialize by running" +
                "$ guiscrcpy-mapper" + "reset points by" + "$ guiscrcpy-mapper -r")

    def fin(self):
        result = []
        try:
            from guiscrcpy import __path__ as xz
            str1 = xz
        except:
            str1 = []
        for path in os.getenv('PATH').split(":") + str1:
            logging.debug("PATH: {}".format(path))
            for files in os.listdir(path):
                logging.debug("FILE: {}".format(files))
                if "mapper.py" in files:
                    result.append(os.path.join(path, "mapper.py"))
                    break
            else:
                logging.debug("Mapper.py not found")

        return result

    def usbaudi(self):
        logging.debug("Called usbaudio")
        runnow = po("usbaudio", shell=True, stdout=PIPE, stderr=PIPE)

    def openme(self):
        webbrowser.open("https://srevinsaju.github.io")

    def opengit(self):
        webbrowser.open("https://github.com/srevinsaju/guiscrcpy")

    def about(self):
        abtBox = QMessageBox().window()
        abtBox.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. guiscrcpy will now exit",
        )
        abtBox.addButton("OK", abtBox.hide())
        abtBox.show()

    def reset(self):

        cfgmgr.reset_config()
        logging.debug("CONFIGURATION FILE REMOVED SUCCESSFULLY")
        logging.debug("RESTART")
        msgBox = QMessageBox().window()
        msgBox.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. guiscrcpy will now exit",
        )
        msgBox.addButton("OK", self.quitAct())
        msgBox.show()

    def quitAct(self):
        sys.exit()

    def menu_about(self):
        pass

    def dimensionChange(self):
        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            config['dimension'] = None
            self.dimensionText.setText("DEFAULT")

        else:
            self.dimensionSlider.setEnabled(True)
            config['dimension'] = int(self.dimensionSlider.value())

            self.dimensionText.setText(
                " " + str(config['dimension']) + "px")
            self.dimensionSlider.sliderMoved.connect(
                self.slider_text_refresh)
            self.dimensionSlider.sliderReleased.connect(
                self.slider_text_refresh)

    def slider_text_refresh(self):
        config['dimension'] = int(self.dimensionSlider.value())
        self.dimensionText.setText(str(config['dimension']) + "px")
        pass

    def dial_text_refresh(self):
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(str(config['bitrate']) + "KB/s")
        pass

    def start_act(self):

        self.runningNot.setText("CHECKING DEVICE CONNECTION")
        timei = time.time()
        self.progressBar.setValue(5)

        devices_list = adb.devices(adb.path)

        if devices_list[0] == "\n":
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0
        try:
            exc = devices_list[1].find("device")
        except IndexError:
            self.runningNot.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0

        if exc > -1:
            self.runningNot.setText(
                "DEVICE " + str(devices_list[0]) + " IS CONNECTED")
            self.progressBar.setValue(10)

        elif devices_list[1][:-1] == "unauthorized":
            self.runningNot.setText(
                "DEVICE IS UNAUTHORIZED. PLEASE CLICK 'OK' ON DEVICE WHEN ASKED FOR"
            )
            self.progressBar.setValue(0)
            return 0

        else:
            self.runningNot.setText(
                "DEVICE CONNECTED BUT FAILED TO ESTABLISH CONNECTION"
            )
            self.progressBar.setValue(0)
            return 0
        # check if the defaultDimension is checked or not for giving signal

        ux = UXMapper()
        dimValues = adb.get_dimensions(adb.path)

        self.progressBar.setValue(15)

        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.dimensionText.setText("DEFAULT")
            config['dimension'] = None

        else:
            self.dimensionSlider.setEnabled(True)
            config['dimension'] = int(self.dimensionSlider.value())
            self.dimensionSlider.setValue(config['dimension'])
            self.dimensionText.setText(str(config['dimension']) + "px")

        # check if the defaultDimension is checked or not for giving signal
        self.progressBar.setValue(20)

        # process dimension
        if config['dimension'] is None:
            self.options = " "
            pass
        elif config['dimension'] is not None:
            self.options = " -m " + str(config['dimension'])
        else:
            self.options = ""

        self.progressBar.setValue(25)
        # CHECK BOX GROUP CONNECT
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
            config['fullscreen'] = True
        else:
            config['fullscreen'] = False

        self.progressBar.setValue(30)
        if self.showTouches.isChecked():
            self.options += " --show-touches"
            config['swtouches'] = True

        else:
            config['swtouches'] = False
        if self.recScui.isChecked():
            self.options += " -r " + str(int(time.time())) + ".mp4 "

        if self.displayForceOn.isChecked():
            self.options += " -S"
            config['dispRO'] = True

        else:
            config['dispRO'] = False

        self.options += " -b " + str(int(self.dial.value())) + "K"
        config['bitrate'] = int(self.dial.value())
        self.progressBar.setValue(40)
        logging.debug("CONNECTION ESTABLISHED")
        self.progressBar.setValue(50)
        logging.debug("Flags passed to scrcpy engine : " + self.options)
        self.progressBar.setValue(75)
        config['extra'] = self.flaglineedit.text()
        self.swipe_instance.init()  # show Swipe UI
        self.panel_instance.init()
        self.side_instance.init()
        if self.cmx is not None:
            config['cmx'] = ' '.join(map(str, self.cmx))

        # run scrcpy usng subprocess
        args = "{} {} {}".format(self.options, config['extra'], config['cmx'])
        scrcpy.start(scrcpy.path, args)

        timef = time.time()
        eta = timef - timei
        print("SCRCPY is launched in", eta, "seconds")
        self.progressBar.setValue(100)

        # handle config files

        cfgmgr.update_config(config)
        cfgmgr.write_file()

        if self.notifChecker.isChecked():
            from guiscrcpy.lib.notify import NotifyAuditor
            NotifyAuditor()

        return True


def bootstrap0():
    # enable highdpi scaling
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(
        QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle('Breeze')
    app.setStyleSheet(darkstylesheet())

    splash_pix = QPixmap(":/res/ui/guiscrcpy-branding.png")
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    cfedited = False

    from guiscrcpy.install.finder import openFileNameDialog
    if adb.path is None:
        adb.path = openFileNameDialog(None, 'adb')
        cfedited = True
        config['adb'] = adb.path

    if scrcpy.path is None:
        scrcpy.path = openFileNameDialog(None, 'scrcpy')
        cfedited = True
        config['scrcpy'] = scrcpy.path

    if (scrcpy.server_path is None) and (platform.System() == 'Windows'):
        scrcpy.server_path = openFileNameDialog(None, 'scrcpy-server')
        cfedited = True
        config['scrcpy-server'] = scrcpy.server_path

    if cfedited:
        cfgmgr.update_config(config)
        cfgmgr.write_file()

    adb.devices(adb.path)
    prog = InterfaceGuiscrcpy()
    prog.show()
    app.processEvents()
    splash.hide()
    app.exec_()
    sys.exit()


if __name__ == "__main__":
    try:
        from guiscrcpy import __path__

        patz = list(__path__)[0]
        sys.path.append(patz)
        sys.path.append('')
    except ModuleNotFoundError:
        pass
    sys.path.append('')

    bootstrap0()


def bootstrap():
    from guiscrcpy import __path__
    patz1 = list(__path__)[0]
    sys.path.append(patz1)
    bootstrap0()

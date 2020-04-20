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

import argparse
import logging
import os
import os.path
import sys
import time
import webbrowser
from datetime import datetime
from subprocess import PIPE
from subprocess import Popen as po

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox

from guiscrcpy.lib.check import adb
from guiscrcpy.lib.check import scrcpy
from guiscrcpy.lib.config import InterfaceConfig
from guiscrcpy.lib.process import is_running
from guiscrcpy.lib.toolkit import UXMapper
from guiscrcpy.platform import platform
from guiscrcpy.theme.decorate import header
from guiscrcpy.theme.style import darkstylesheet
from guiscrcpy.ui.main import Ui_MainWindow
from guiscrcpy.ux.panel import Panel
from guiscrcpy.ux.swipe import SwipeUX
from guiscrcpy.ux.toolkit import InterfaceToolkit
from guiscrcpy.version import VERSION
from guiscrcpy.install.finder import openFileNameDialog

try:
    os.chdir(os.path.dirname(__file__))
except FileNotFoundError:
    pass  # Its a PyInstaller compiled package

# initialize config manager
cfgmgr = InterfaceConfig()
config = cfgmgr.get_config()
environment = platform.System()

# Add precedence for guiscrcpy to check environment variables
# for the paths of `adb` and `scrcpy` over the configuration files.
if os.getenv('GUISCRCPY_ADB', None) is None:
    adb.path = config['adb']
else:
    adb.path = os.getenv('GUISCRCPY_ADB')

if os.getenv('GUISCRCPY_SCRCPY', None) is None:
    scrcpy.path = config['scrcpy']
else:
    scrcpy.path = os.getenv('GUISCRCPY_SCRCPY')

scrcpy.server_path = config['scrcpy-server']

# Initialize argument parser
parser = argparse.ArgumentParser('guiscrcpy v{}'.format(VERSION))
parser.add_argument('-i', '--install', action='store_true',
                    help="Install guiscrcpy system wide on Linux")
parser.add_argument('-s', '--start', action='store_true',
                    help="Start scrcpy first before loading the GUI")
parser.add_argument('-o', '--output', action='store_true',
                    help="Show logging output in stdout and in .log filename")
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
    filename=os.path.join(
        cfgmgr.get_cfgpath(),
        'guiscrcpy_log_{}.log'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    ),
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

logging.debug("Received flag {}".format(args.start))

header(VERSION)

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
    """
    Main class for guiscrcpy object.
    All the processes to spawn to scrcpy are handled here
    """

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.cmx = None
        self.sm = None
        self.nm = None
        self.swipe_instance = None
        self.panel_instance = None
        self.side_instance = None
        self.child_windows = list()
        self.options = ""
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
            self.private_message_box_adb.setText("SCRCPY SERVER RUNNING")
        else:
            logging.debug("SCRCPY SERVER IS INACTIVE")
            self.private_message_box_adb.setText("SCRCPY SERVER NOT RUNNING")

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(
            self.__dimension_change_cb)
        self.build_label.setText("Build " + str(VERSION))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.__dial_change_cb)
        self.dial.sliderReleased.connect(self.__dial_change_cb)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)
        try:
            if config['extra']:
                self.flaglineedit.setText(config['extra'])
            else:
                pass
        except Exception as err:
            logging.debug(f"Exception: flaglineedit.text(config[extra]) {err}")
            pass

        # set bottom instance and side instance as enabled by default
        self.check_bottom_panel.setChecked(True)
        self.check_side_panel.setChecked(True)

        self.quit.clicked.connect(self.quit_window)
        self.dimensionText.setText("DEFAULT")
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(" " + str(config['bitrate']) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtme.clicked.connect(self.launch_web_srevinsaju)
        self.abtgit.clicked.connect(self.launch_web_github)
        self.usbaud.clicked.connect(self.launch_usb_audio)
        self.mapnow.clicked.connect(self.mapp)
        self.network_button.clicked.connect(self.network_mgr)
        self.settings_button.clicked.connect(self.settings_mgr)
        self.refreshdevices.clicked.connect(
            self.__refresh_devices_combo_box_cb)

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
                "guiscrcpy ~ mapper is not initialized. "
                "Initialize by running" +
                "$ guiscrcpy-mapper" + "reset points by" +
                "$ guiscrcpy-mapper -r"
            )

    @staticmethod
    def launch_usb_audio():
        logging.debug("Called usbaudio")
        po("usbaudio", shell=True, stdout=PIPE, stderr=PIPE)

    @staticmethod
    def launch_web_srevinsaju():
        webbrowser.open("https://srevinsaju.github.io")

    @staticmethod
    def launch_web_github():
        webbrowser.open("https://github.com/srevinsaju/guiscrcpy")

    def about(self):
        about_message_box = QMessageBox().window()
        about_message_box.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. "
            "guiscrcpy will now exit",
        )
        about_message_box.addButton("OK", about_message_box.hide())
        about_message_box.show()

    def reset(self):

        cfgmgr.reset_config()
        logging.debug("CONFIGURATION FILE REMOVED SUCCESSFULLY")
        logging.debug("RESTART")
        message_box = QMessageBox().window()
        message_box.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. "
            "guiscrcpy will now exit",
        )
        message_box.addButton("OK", self.quit_window())
        message_box.show()

    @staticmethod
    def quit_window():
        sys.exit()

    def __dimension_change_cb(self):
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
                self.__slider_change_cb)
            self.dimensionSlider.sliderReleased.connect(
                self.__slider_change_cb)

    def __slider_change_cb(self):
        config['dimension'] = int(self.dimensionSlider.value())
        self.dimensionText.setText(str(config['dimension']) + "px")
        pass

    def __dial_change_cb(self):
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(str(config['bitrate']) + "KB/s")
        pass

    def __refresh_devices_combo_box_cb(self):
        devices_list = adb.devices(adb.path)

        if len(devices_list) == 0:
            self.private_message_box_adb.setText("DEVICE IS NOT CONNECTED")
            self.progressBar.setValue(0)
            return 0,
        else:
            valid_devices = []
            invalid_devices = []
            for dev, stat in devices_list:
                if stat == "unauthorized":
                    invalid_devices.append(
                        f"{dev} IS UNAUTHORIZED. CLICK 'ok' when asked.")
                elif stat == "device":
                    valid_devices.append(dev)
                else:
                    invalid_devices.append(
                        f"{dev} is connected. Failed to establish connection")
            self.private_message_box_adb.setText(
                "Connected: {};".format(', '.join(valid_devices))
            )
        if len(valid_devices) > 1:
            if self.devices_combox.currentText(
            ) == '' or self.devices_combox.currentText().isspace():
                logging.info(
                    "Found more than one device. "
                    "Please select device in drop down box")
                self.private_message_box_adb.setText(
                    "Found more than one device. "
                    "Please select device in drop down box")
                self.devices_combox.clear()
                self.devices_combox.addItems(
                    [f"{x[0]} : {x[1]}" for x in devices_list])
                return 0,

            else:
                more_devices = True
                device_id = self.devices_combox.currentText().split(":")[
                    0].strip()
        else:
            more_devices = False
            device_id = None

        return more_devices, device_id

    def start_act(self):
        stylesheet = "background-color: qlineargradient(" \
                     "spread:pad, x1:0, y1:0, x2:1, y2:1, " \
                     "stop:0 rgba(0, 255, 255, 255), " \
                     "stop:1 rgba(0, 255, 152, 255)); " \
                     "border-radius: 10px;"
        self.private_message_box_adb.setStyleSheet(stylesheet)

        self.private_message_box_adb.setText("CHECKING DEVICE CONNECTION")
        initial_time = time.time()
        self.progressBar.setValue(5)

        values_devices_list = self.__refresh_devices_combo_box_cb()
        if len(values_devices_list) != 2:
            return 0
        else:
            more_devices, device_id = values_devices_list

        # check if the defaultDimension is checked or not for giving signal

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
        self.progressBar.setValue(60)
        config['extra'] = self.flaglineedit.text()

        # show subwindows
        ux = UXMapper(device_id=device_id)
        swipe_instance = SwipeUX(ux_wrapper=ux)  # Load swipe UI

        self.progressBar.setValue(70)
        if self.check_side_panel.isChecked():
            side_instance = InterfaceToolkit(parent=self, ux_mapper=ux)
            side_instance.init()
            self.child_windows.append(side_instance)

        if self.check_bottom_panel.isChecked():
            panel_instance = Panel(parent=self, ux_mapper=ux)
            panel_instance.init()
            self.child_windows.append(panel_instance)

        swipe_instance.init()
        self.child_windows.append(swipe_instance)

        hexdigest = ux.get_sha()[:6]
        stylesheet = f"background-color: #{hexdigest}; border-radius: 10px; "
        self.private_message_box_adb.setStyleSheet(stylesheet)

        if self.cmx is not None:
            config['cmx'] = ' '.join(map(str, self.cmx))

        arguments_scrcpy = "{} {} {}".format(
            self.options,
            config['extra'],
            config['cmx']
        )

        if more_devices:
            # guiscrcpy found more devices
            # scrcpy will fail if more than one device is found
            # its important to pass the device serial id, if more than one
            # device is found
            arguments_scrcpy = f"-s {device_id} " + arguments_scrcpy
            # tell end users that the color of the device is this
            self.private_message_box_adb.setText(f"Device {device_id} is "
                                                 f"connected; (color id "
                                                 f"matches toolkit color)")

        scrcpy.start(scrcpy.path, arguments_scrcpy)
        final_time = time.time()
        eta = final_time - initial_time
        print("scrcpy launched in {:.2f}s".format(eta))
        self.progressBar.setValue(100)

        # handle config files

        cfgmgr.update_config(config)
        cfgmgr.write_file()

        if self.notifChecker.isChecked():
            # call notification auditor if notification_auditor is checked only
            from guiscrcpy.lib.notify import NotifyAuditor
            NotifyAuditor()

        return True


def bootstrap0():
    """
    Launch the guiscrcpy window
    :return:
    """
    # enable High DPI scaling
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(
        QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use HIGH DPI icons
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle('Breeze')
    app.setStyleSheet(darkstylesheet())

    splash_pix = QPixmap(":/res/ui/guiscrcpy-branding.png")
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    cfedited = False

    if (adb.path is None) or (not os.path.exists(adb.path)):
        adb.path = openFileNameDialog(None, 'adb')
        cfedited = True
        config['adb'] = adb.path

    if (scrcpy.path is None) or (not os.path.exists(scrcpy.path)):
        scrcpy.path = openFileNameDialog(None, 'scrcpy')
        cfedited = True
        config['scrcpy'] = scrcpy.path

    # on windows, users are likely not to add the scrcpy-server to the
    # SCRCPY_SERVER_PATH
    scrcpy_server_path_env = os.getenv('SCRCPY_SERVER_PATH', None)
    if scrcpy_server_path_env:
        if os.path.exists(scrcpy_server_path_env):
            config['scrcpy-server'] = scrcpy.server_path
        else:
            scrcpy.server_path = openFileNameDialog(None, 'scrcpy-server')
            cfedited = True
            config['scrcpy-server'] = scrcpy.server_path
            os.environ['SCRCPY_SERVER_PATH'] = scrcpy.server_path
    elif ((scrcpy.server_path is None) or
          (not os.path.exists(scrcpy.server_path))) and (
            platform.System().system() == 'Windows'
    ):
        scrcpy.server_path = openFileNameDialog(None, 'scrcpy-server')
        cfedited = True
        config['scrcpy-server'] = scrcpy.server_path
        os.environ['SCRCPY_SERVER_PATH'] = scrcpy.server_path
    elif platform.System().system() == "Windows":
        os.environ['SCRCPY_SERVER_PATH'] = scrcpy.server_path

    if cfedited:
        cfgmgr.update_config(config)
        cfgmgr.write_file()

    adb.devices(adb.path)
    guiscrcpy = InterfaceGuiscrcpy()
    guiscrcpy.show()
    app.processEvents()
    splash.hide()
    app.exec_()
    sys.exit()


if __name__ == "__main__":
    try:
        # workaround the inability to locate pixmaps
        from guiscrcpy import __path__
        paths = list(__path__)[0]
        sys.path.append(paths)
        sys.path.append('')
    except Exception as e:
        logging.debug(f"E:{e}. Continuing to run guiscrcpy.")

    # add current path to PATH
    sys.path.append('')

    # bootstrap guiscrcpy
    bootstrap0()


def bootstrap():
    from guiscrcpy import __path__
    patz1 = list(__path__)[0]
    sys.path.append(patz1)
    bootstrap0()

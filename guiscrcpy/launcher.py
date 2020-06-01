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
import hashlib
import logging
import os
import sys
import time
import webbrowser
from subprocess import PIPE
from subprocess import Popen

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QModelIndex, QPoint
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QMenu
from PyQt5.QtWidgets import QMessageBox

from guiscrcpy.install.finder import open_exe_name_dialog
from guiscrcpy.lib.check import adb
from guiscrcpy.lib.check import scrcpy
from guiscrcpy.lib.config import InterfaceConfig
from guiscrcpy.lib.process import is_running
from guiscrcpy.lib.toolkit import UXMapper
from guiscrcpy.lib.utils import log, shellify
from guiscrcpy.platform import platform
from guiscrcpy.theme.decorate import Header
from guiscrcpy.theme.desktop_shortcut import desktop_device_shortcut_svg
from guiscrcpy.theme.linux_desktop_shortcut_template import GUISCRCPY_DEVICE
from guiscrcpy.theme.style import dark_stylesheet
from guiscrcpy.ui.main import Ui_MainWindow
from guiscrcpy.ux.panel import Panel
from guiscrcpy.ux.swipe import SwipeUX
from guiscrcpy.ux.toolkit import InterfaceToolkit
from guiscrcpy.version import VERSION

# ============================================================================
# Change directory so that the pixmaps are available to PyQt windows
try:
    os.chdir(os.path.dirname(__file__))
except FileNotFoundError:
    pass  # Its a PyInstaller compiled package

# ============================================================================
# initialize config manager
cfgmgr = InterfaceConfig()
config = cfgmgr.get_config()
environment = platform.System()

# ============================================================================
# Load cairo-svg conditionally
if environment.system() == "Linux":
    from cairosvg import svg2png  # noqa:

# ============================================================================
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

# ============================================================================
# ARGUMENT PARSER

sys_argv = []
for arg in range(len(sys.argv)-1, -1, -1):
    log("Scanning {}".format(sys.argv[arg]))
    if '.py' in sys.argv[arg] or 'guiscrcpy' in sys.argv[arg]:
        sys_argv = sys.argv[arg+1:]
        break

# interface adb if asked for
if 'adb-interface' in sys.argv:
    if (adb.path is None) or (not os.path.exists(adb.path)):
        raise FileNotFoundError(
            "adb is not yet configured to interface it. "
            "Please run guiscrcpy normally once, and then you can run the "
            "command. adb is configured on the first successful run of "
            "guiscrcpy"
        )
    try:
        adb_commands = sys.argv.index('adb-interface') + 1
    except ValueError:
        raise OSError("adb-interface command is to be given as an arg and "
                      "not a param")
    adb_process_output = Popen(shellify(
        f"{adb.path} {' '.join(sys.argv[adb_commands:])}"
    ), stdout=PIPE, stderr=PIPE)
    print(adb_process_output.stdout.read().decode())
    print(adb_process_output.stderr.read().decode())
    sys.exit(0)

# interface scrcpy if asked for
if 'scrcpy-interface' in sys.argv:
    if (scrcpy.path is None) or (not os.path.exists(scrcpy.path)):
        raise FileNotFoundError(
            "scrcpy is not yet configured to interface it. "
            "Please run guiscrcpy normally once, and then you can run the "
            "command. scrcpy is configured on the first successful run of "
            "guiscrcpy"
        )
    try:
        scrcpy_commands = sys.argv.index('scrcpy-interface') + 1
    except ValueError:
        raise OSError("scrcpy-interface command is to be given as an arg and "
                      "not a param")
    scrcpy_process_output = Popen(shellify(
        f"{scrcpy.path} {' '.join(sys.argv[scrcpy_commands:])}"
    ), stdout=PIPE, stderr=PIPE)
    print(scrcpy_process_output.stdout.read().decode())
    print(scrcpy_process_output.stderr.read().decode())
    sys.exit(0)

# Initialize argument parser
parser = argparse.ArgumentParser(
    'guiscrcpy v{}'.format(VERSION)
)
parser.add_argument(
    '-i',
    '--install',
    action='store_true',
    help="Install guiscrcpy system wide on Linux"
)
parser.add_argument(
    '-s',
    '--start',
    action='store_true',
    help="Start scrcpy first before loading the GUI"
)
parser.add_argument(
    '--start-scrcpy-device-id',
    default='',
    help="Provide the device id in the case of multiple devices."
         " (applicable only when '-s' or '--start' is passed)"
)
parser.add_argument(
    '-r',
    '--reset',
    action='store_true',
    help="Reset the guiscrcpy configuration files to default"
)
parser.add_argument(
    '--mapper',
    action='store_true',
    help="Interface guiscrcpy's mapper to guiscrcpy main executable"
)
parser.add_argument(
    '--mapper-reset',
    action='store_true',
    help="Reset guiscrcpy's mapper configuration file"
)
parser.add_argument(
    '--mapper-delay',
    action='store_true',
    help="Sets the delay before connecting and configuring mapper files"
)
parser.add_argument(
    '--mapper-device-id',
    default='',
    help="Sets the device-id for mapper to configure (optional, "
         "needed for multiple devices)"
)
parser.add_argument(
    '-w',
    '--disable-swipe',
    action='store_true',
    help="Disable the swipe panel"
)
parser.add_argument(
    '--connect',
    default='',
    help="Disable the swipe panel"
)
parser.add_argument(
    '-q',
    '--noscrcpy',
    action='store_true',
    help="Disable scrcpy processes (For debugging only)"
)
parser.add_argument(
    '--panels-not-always-on-top',
    action='store_true',
    help="Remove the always on top default while running guiscrcpy"
)
parser.add_argument(
    '--theme',
    default='Breeze',
    help="Set the default theme (based on PyQt5 themes - Fusion, Breeze, "
         "Windows) (stored in configuration, override by --theme-no-cfg)"
)
parser.add_argument(
    '-f',
    '--force-window-frame',
    action='store_true',
    help="Force display desktop window manager for toolkit without frames"
)
parser.add_argument(
    '-o',
    '--output',
    action='store_true',
    help="Show logging output in stdout and in .log filename"
)
parser.add_argument(
    '-k',
    '--killserver',
    action='store_true',
    help="Kills adb server if exists any and restarts server. (Disconnects "
         "any connected device over LAN)"
)
parser.add_argument(
    '-d',
    '--debug',
    default=3,
    help="Set a logging level from 0,1,2,3,4,5"
)
parser.add_argument(
    '-v',
    '--version',
    action='store_true',
    help="Display guiscrcpy version"
)
log(f"Complete args {sys.argv}")
log(f"Received {sys_argv}")
args = parser.parse_args(sys_argv)
log(f"Parsed {args}")
# set argument debug level
if args.debug:
    logging_priority = int(args.debug) * 10
else:
    logging_priority = 30
logger = logging.Logger('guiscrcpy', logging_priority)

logger.debug("Received flag {}".format(args.start))

Header(VERSION)

if args.version:
    # Show version and exit lol
    import inspect
    from PyQt5 import Qt
    _pyqt5_version = [
        '%s = %s' % (k, v) for k, v in
        vars(Qt).items() if
        k.lower().find('version') >= 0 and not inspect.isbuiltin(v)
    ]
    print()
    print("== PyQt5 Version ==")
    print('\n'.join(sorted(_pyqt5_version)))
    print()
    if environment.system() == "Linux":
        print("== CairoSVG version ==")
        from cairosvg import VERSION as CAIRO_VERSION # noqa:
        print("CairoSVG == {}".format(CAIRO_VERSION))
        print()

    sys.exit(0)

if args.reset:
    # Resets the guiscrcpy.json configuration file
    cfgmgr.reset_config()
    print("Configuration files resetted successfully.")

logger.debug("Current Working Directory {}".format(os.getcwd()))

if args.connect:
    # Connects to a device with a valid IP:PORT address
    adb_cnx_output = adb.command(adb.path, 'connect {}'.format(args.connect))
    print(
        adb_cnx_output.stdout.read().decode(),
        adb_cnx_output.stderr.read().decode()
    )

if args.start:
    # Starts scrcpy before calling guiscrcpy UI with limited configuration
    devices = adb.devices_detailed(adb.path)
    logger.debug("RUNNING SCRCPY DIRECTLY")
    scrcpy_args = ""

    if len(devices) > 1 and args.start_scrcpy_device_id:
        scrcpy_args += " -s {}".format(args.start_scrcpy_device_id)

    scrcpy_args += " -b " + str(config['bitrate'])
    if config['fullscreen']:
        scrcpy_args += " -f "
    if config['swtouches']:
        scrcpy_args += " -t "
    if config['dispRO']:
        scrcpy_args += " --turn-screen-off "
    scrcpy.start(scrcpy.path, scrcpy_args)

if args.mapper_reset:
    # Reset the mapper configuration if mapper is called.
    mapper_cfg_path = os.path.join(
        cfgmgr.get_cfgpath(), 'guiscrcpy.mapper.json'
    )
    # A ternary version of removing a file if it exists
    # https://stackoverflow.com/questions/10840533/
    # most-pythonic-way-to-delete-a-file-which-may-not-exist
    mapper_configuration_file_exists = os.remove(mapper_cfg_path) if \
        os.path.exists(
        mapper_cfg_path) else None
    if mapper_configuration_file_exists:
        print("guiscrcpy mapper configuration file has been removed.")
        print("Removed {}".format(mapper_configuration_file_exists))
        sys.exit(0)
    else:
        print("guiscrcpy mapper configuration is not created yet.")
        sys.exit(1)

if args.mapper:
    from guiscrcpy.lib import mapper
    # Initialize the mapper if it is called.
    print('Initializing guiscrcpy mapper v3.5-')
    mapper.file_check()
    sys.exit(0)

logger.debug("Importing modules...")


class InterfaceGuiscrcpy(QMainWindow, Ui_MainWindow):
    """
    Main class for guiscrcpy object.
    All the processes to spawn to scrcpy are handled here
    """

    # noinspection PyArgumentList
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
        logger.debug(
            "Options received by class are : {} {} {} {} {} ".format(
                config['bitrate'],
                config['dimension'],
                config['swtouches'],
                config['dispRO'],
                config['fullscreen'],
            ))
        # ====================================================================
        # Rotation; read config, update UI
        self.device_rotation.setCurrentIndex(config.get("rotation", 0))
        self.dial.setValue(int(config['bitrate']))
        if config['swtouches']:
            self.showTouches.setChecked(True)
        else:
            self.showTouches.setChecked(False)
        if config['dispRO']:
            self.displayForceOn.setChecked(True)
        else:
            self.displayForceOn.setChecked(False)

        # panels
        if config['panels'].get('swipe'):
            self.check_swipe_panel.setChecked(True)
        else:
            self.check_swipe_panel.setChecked(False)
        if config['panels'].get('tookit'):
            self.check_side_panel.setChecked(True)
        else:
            self.check_side_panel.setChecked(False)
        if config['panels'].get('bottom'):
            self.check_bottom_panel.setChecked(True)
        else:
            self.check_bottom_panel.setChecked(False)

        # dimension
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
            logger.debug("SCRCPY RUNNING")
            self.display_public_message("SCRCPY SERVER RUNNING")
        else:
            logger.debug("SCRCPY SERVER IS INACTIVE")
            self.display_public_message("SCRCPY SERVER NOT RUNNING")

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(
            self.__dimension_change_cb)
        self.build_label.setText("Build {} by srevinsaju".format(VERSION))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.__dial_change_cb)
        self.dial.sliderReleased.connect(self.__dial_change_cb)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)
        try:
            if config['extra']:
                self.flaglineedit.setText(config['extra'])
        except Exception as err:
            logger.debug(f"Exception: flaglineedit.text(config[extra]) {err}")

        # set swipe instance, bottom instance and
        # side instance as enabled by default
        self.check_swipe_panel.setChecked(True)
        self.check_bottom_panel.setChecked(True)
        self.check_side_panel.setChecked(True)

        self.quit.clicked.connect(self.quit_window)
        self.dimensionText.setText("DEFAULT")
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(" " + str(config['bitrate']) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtgit.clicked.connect(self.launch_web_github)
        self.usbaud.clicked.connect(self.launch_usb_audio)
        self.mapnow.clicked.connect(self.bootstrap_mapper)
        self.network_button.clicked.connect(self.network_mgr)
        self.settings_button.clicked.connect(self.settings_mgr)
        # self.devices_view.itemChanged.connect(self.update_rotation_combo_cb)
        self.devices_view.itemClicked.connect(self.update_rotation_combo_cb)
        self.refreshdevices.clicked.connect(
            self.scan_devices_update_list_view
        )
        self.restart_adb_server.clicked.connect(
            self.restart_adb_server_guiscrcpy)
        self.devices_view.itemClicked.connect(self.more_options_device_view)
        self.devices_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.scan_config_devices_update_list_view()
        self.refresh_devices()

    @staticmethod
    def restart_adb_server_guiscrcpy():
        adb.kill_adb_server(adb.path)

    def refresh_devices(self):
        """
        A slot for refreshing the QListView
        :return:
        """
        self.scan_devices_update_list_view()

    def update_rotation_combo_cb(self):
        """
        A proposed method for refreshing the rotation combobox on item
        change in the QListBox
        :return:
        """
        if self.devices_view.currentItem():
            _, device_id = self.current_device_identifier()
            _rotation = config['device']\
                .get(device_id, dict()).get(
                    'rotation',
                    self.device_rotation.currentIndex()
            )
        else:
            _rotation = config.get(
                "rotation", self.device_rotation.currentIndex()
            )
        self.device_rotation.setCurrentIndex(_rotation)

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

    @staticmethod
    def bootstrap_mapper():
        if (os.path.exists(
                os.path.join(cfgmgr.get_cfgpath() + "guiscrcpy.mapper.json"))):
            from guiscrcpy.lib import mapper
            mapper.file_check()
        else:
            logger.warning(
                "guiscrcpy ~ mapper is not initialized. \n"
                "Initialize by running \n\n"
                "$ guiscrcpy --mapper \n\n"
                "reset points by \n\n" +
                "$ guiscrcpy --mapper --mapper-reset\n"
            )

    @staticmethod
    def launch_usb_audio():
        logger.debug("Called usbaudio")
        for path in environment.paths():
            if os.path.exists(os.path.join(path, 'usbaudio')):
                path_to_usbaudio = os.path.join(path, 'usbaudio')
                break
        else:
            return
        Popen(path_to_usbaudio, stdout=PIPE, stderr=PIPE)

    @staticmethod
    def launch_web_github():
        webbrowser.open("https://github.com/srevinsaju/guiscrcpy")

    def about(self):
        """
        Reset message box is based on aboutWindow object
        For some reason, I did not get time to fix that
        :return:
        """
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
        """
        Remove configuration files; Reset the mapper and guiscrcpy.json
        :return:
        """
        cfgmgr.reset_config()
        logger.debug("CONFIGURATION FILE REMOVED SUCCESSFULLY")
        logger.debug("RESTART")
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
        """
        A method to quit the main window
        :return:
        """
        sys.exit()

    def forget_paired_device(self):
        """
        Forgets / Removes the configuration for saved
        :return: popped item / False
        """
        try:
            _, identifier = self.current_device_identifier()
            popped_device = config['device'].pop(identifier)
            self.refresh_devices()
            cfgmgr.update_config(config)
            cfgmgr.write_file()
            return popped_device
        except KeyError:
            return False

    def more_options_device_view(self, button):
        if 'Disconnect' in button.text():
            menu = QMenu("Menu", self)
            menu.addAction("Pair / Ping", self.ping_paired_device)
            menu.addAction("Attempt TCPIP on device", self.tcpip_paired_device)
            menu.addAction("Forget device", self.forget_paired_device)
        else:
            menu = QMenu("Menu", self)
            menu.addAction("Attempt TCPIP on device", self.tcpip_paired_device)
            menu.addAction("Attempt reconnection", self.ping_paired_device)
            menu.addAction("Refresh", self.refresh_devices)
        _, identifier = self.current_device_identifier()
        if platform.System.system() == "Linux" and identifier.count('.') >= 3:
            menu.addAction(
                "Add Desktop Shortcut to this device",
                self.create_desktop_shortcut_linux_os
            )
        menu.exec_(
            self.devices_view.mapToGlobal(
                QPoint(
                    self.devices_view.visualItemRect(button).x() + 22,
                    self.devices_view.visualItemRect(button).y() + 22
                )
            )
        )

    def create_desktop_shortcut_linux_os(self):
        """
        Creates a desktop shortcut for Linux OS
        :return:
        """
        # just a check before anything further happens because of an
        # unrelated OS
        if environment.system() != "Linux":
            log("Tried to run create_desktop_shortcut_linux_os on an "
                "unsupported OS.")
            return False

        # get device specific configuration
        model, identifier = self.current_device_identifier()
        picture_file_path = cfgmgr.get_cfgpath()
        __sha_shift = config.get('sha_shift', 5)
        sha = hashlib.sha256(
            str(identifier).encode()
        ).hexdigest()[__sha_shift:__sha_shift + 6]
        log(f"Creating desktop shortcut sha: {sha}")
        path_to_image = os.path.join(picture_file_path, identifier+'.png')
        svg2png(
            bytestring=desktop_device_shortcut_svg().format(f"#{sha}"),
            write_to=path_to_image
        )

        # go through all args; break when we find guiscrcpy
        for args_i in range(len(sys.argv)):
            if 'guiscrcpy' in sys.argv[args_i]:
                aend = args_i + 1
                break
        else:
            aend = None

        sys_args_desktop = sys.argv[:aend]

        # check if its a python file
        # experimental support for AppImages / snaps
        # I am not sure; if it would work indeed
        for i in sys_args_desktop:
            if i.endswith('.py'):
                needs_python = True
                break
        else:
            needs_python = False
        if needs_python:
            sys_args_desktop = ['python3'] + sys_args_desktop

        # convert the list into a string
        sys_args_desktop = ' '.join(sys_args_desktop)
        auto_connect_run_command = \
            "{executable} --connect={ip} " \
            "--start --start-scrcpy-device-id={ip}".format(
                executable=sys_args_desktop,
                ip=identifier
            )

        # create the desktop file using linux's desktop file gen method
        path_to_desktop_file = platform.System().create_desktop(
            desktop_file=GUISCRCPY_DEVICE.format(
                identifier=model,
                command=auto_connect_run_command,
                icon_path=path_to_image
            ),
            desktop_file_name=f'{model}.guiscrcpy.desktop'
        )

        # announce it to developers / users
        log(f"Path to desktop file : {path_to_desktop_file}")
        print("Desktop file generated successfully")
        self.display_public_message("Desktop file has been created")

    def is_connection_success_handler(self, output: Popen, ip=None):
        out, err = output.communicate()
        if 'failed' in out.decode() or 'failed' in err.decode():
            self.display_public_message(
                "Failed to connect to {}. See the logs for more "
                "information".format(ip)
            )
            print("adb:", out.decode(), err.decode())
        else:
            self.display_public_message(
                "Connection command completed successfully"
            )

    def ping_paired_device(self, device_id=None):
        # update the configuration file first
        if not device_id:
            _, identifier = self.current_device_identifier()
            if identifier.count('.') == 3:
                wifi_device = True
            else:
                wifi_device = False
            try:
                config['device'][identifier]['wifi'] = wifi_device
            except KeyError:
                log(f"Failed writing the configuration "
                    f"'wifi' key to {identifier}")

            if wifi_device:
                ip = self.current_device_identifier()[1]
                output = adb.command(adb.path, 'connect {}'.format(ip))
                self.is_connection_success_handler(output, ip=ip)
            else:
                adb.command(adb.path, 'reconnect offline')
            # As we have attempted to connect; refresh the panel
            self.refresh_devices()
        else:
            output = adb.command(adb.path, 'connect {}'.format(device_id))
            self.is_connection_success_handler(output, ip=device_id)

    def tcpip_paired_device(self):
        if self.devices_view.currentItem():
            _, identifier = self.current_device_identifier()
        else:
            identifier = ""
        __exit_code = adb.tcpip(adb.path, identifier=identifier)
        if __exit_code != 0:
            self.display_public_message(
                "TCP/IP failed on device. "
                "Please reconnect USB and try again"
            )
        else:
            self.display_public_message(
                "TCP/IP completed successfully."
            )
            time.sleep(0.1)  # wait for everything to get settled
            if identifier.count('.') >= 3:
                self.ping_paired_device(device_id=identifier)
            else:
                self.ping_paired_device()

    def current_device_identifier(self, need_status=False):
        if self.devices_view.currentItem():
            if need_status:
                return \
                    self.devices_view.currentItem().text().split()[0], \
                    self.devices_view.currentItem().text().split()[1], \
                    self.devices_view.currentItem().text().split()[2]
            else:
                return \
                    self.devices_view.currentItem().text().split()[0], \
                    self.devices_view.currentItem().text().split()[1]
        else:
            raise ValueError("No item is selected in QListView")

    def scan_config_devices_update_list_view(self):
        """
        Scans for saved devices
        :return:
        """
        self.devices_view.clear()
        paired_devices = config['device']
        for i in paired_devices:
            if paired_devices[i].get('wifi'):
                icon = ':/icons/icons/portrait_mobile_disconnect.svg'
                devices_view_list_item = QListWidgetItem(
                        QIcon(icon),
                        "{device}\n{mode}\n{status}".format(
                            device=paired_devices[i].get('model'),
                            mode=i,
                            status='Disconnected'
                        )
                    )
                __sha_shift = config.get('sha_shift', 5)
                __sha = hashlib.sha256(
                    str(i).encode()).hexdigest()[__sha_shift:__sha_shift+6]
                devices_view_list_item.setToolTip(
                    "<span style='color: #{color}'>Device</snap>: <b>{d}</b>\n"
                    "Status: {s}".format(
                        d=i,
                        s="Disconnected. Right click 'ping' to attempt "
                          "reconnect",
                        color=__sha
                    )
                )
                devices_view_list_item.setFont(QFont('Noto Sans', pointSize=8))
                self.devices_view.addItem(devices_view_list_item)
        return paired_devices

    def scan_devices_update_list_view(self):
        """
        Scan for new devices; and update the list view
        :return:
        """
        # self.devices_view.clear()
        device_exists_in_view = False
        paired_devices = []
        for index in range(self.devices_view.count()):
            paired_devices.append(self.devices_view.item(index))

        __devices = adb.devices_detailed(adb.path)
        log(__devices)
        for i in __devices:
            device_is_wifi = \
                i['identifier'].count('.') >= 3 and (':' in i['identifier'])

            if i['identifier'] not in config['device'].keys():
                device_paired_and_exists = False
                config['device'][i['identifier']] = {
                    'rotation': 0
                }
            else:
                device_paired_and_exists = True

            if device_is_wifi:
                _icon_suffix = '_wifi'
            else:
                _icon_suffix = '_usb'

            icon = ':/icons/icons/portrait_mobile_white{}.svg'.format(
                _icon_suffix
            )

            if i['status'] == 'offline':
                icon = ':/icons/icons/portrait_mobile_error.svg'
            elif i['status'] == 'unauthorized':
                icon = ':/icons/icons/portrait_mobile_warning.svg'

            if i['status'] == 'no_permission':
                log("pairfilter: 5")
                # https://stackoverflow.com/questions/
                # 53887322/adb-devices-no-permissions-user-in-
                # plugdev-group-are-your-udev-rules-wrong
                udev_error = "Error connecting to device. Your udev rules are"\
                    " incorrect. See https://stackoverflow.com/questions"\
                    "/53887322/adb-devices-no-permissions-user-in-plugdev-"\
                    "group-are-your-udev-rules-wrong"
                self.display_public_message(udev_error)
                print(udev_error)
                return []
            # Check if device is unauthorized
            elif i['status'] == "unauthorized":
                log("unauthorized device detected: Click Allow on your device")
                log("pairfilter: 4")
                # The device is connected; and might/might't paired in the past
                # And is connected to the same IP address
                # It is possibly a bug with the connection;
                # Temporarily create a new QListItem to display the
                # device with the error
                paired = False
                device_paired_and_exists = False
                self.display_public_message(
                    f"{i['identifier']} is unauthorized. Please click allow "
                    f"on your device."
                )
                # Remove other devices with the same id and offline and
                # unauthorized
                self.remove_device_device_view(
                    i['identifier'],
                    statuses=['offline', 'unauthorized']
                )
                # Unauthorized device cannot be considered as a paired device
                devices_view_list_item = QListWidgetItem()
            else:
                # check if device is paired
                # if yes, just update the list item
                if not device_paired_and_exists:
                    paired = False
                    devices_view_list_item = QListWidgetItem()
                else:
                    for paired_device in paired_devices:
                        if paired_device.text().split()[0] == i['model']:
                            log("pairfilter: 1")
                            paired = True
                            devices_view_list_item = paired_device
                            # as we have found a paired device
                            # we know by assumption; there cannot be two
                            # devices with the same local IP address;
                            # lets scan the devices_view once more in a loop
                            # to check for any device with the same
                            # identifier and remove them; based on this same
                            # assumption
                            self.remove_device_device_view(
                                i['identifier'],
                                statuses=['offline', 'unauthorized']
                            )
                            break
                        elif paired_device.text().split()[1] ==\
                                i['identifier']:
                            log("pairfilter: 2")
                            self.remove_device_device_view(
                                i['identifier'],
                                statuses=['offline', 'unauthorized']
                            )
                            devices_view_list_item = QListWidgetItem()
                            paired = False
                            break
                    else:
                        log("pairfilter: 3")
                        paired = False
                        devices_view_list_item = QListWidgetItem()

            devices_view_list_item.setIcon(QIcon(icon))

            devices_view_list_item.setText(
                "{device}\n{mode}\n{status}".format(
                    device=i['model'],
                    mode=i['identifier'],
                    status=i['status']
                )
            )
            __sha_shift = config.get('sha_shift', 5)
            __sha = hashlib.sha256(
                str(i['identifier']).encode()
            ).hexdigest()[__sha_shift:__sha_shift + 6]
            devices_view_list_item.setToolTip(
                "Device: "
                "<span style='color: #{inv_color};background-color: #{color}'>"
                "<b>{d}</b></span>\n"
                "<br>"
                "Model: {m}\n<br>"
                "Alias: {a}\n<br>"
                "Status: {s}\n<br>"
                "Transport ID: {t}\n<br>"
                "Paired: {p}".format(
                    d=i['identifier'],
                    m=i['model'],
                    a=i['product'],
                    s=i['status'],
                    t=i['transport_id'],
                    p=paired,
                    color=__sha,
                    inv_color=str(hex(0xFFFFFF - int(__sha, 16))[2:])
                )
            )

            devices_view_list_item.setFont(QFont('Noto Sans', pointSize=8))
            log(f"Pairing status: {device_paired_and_exists}")
            if device_paired_and_exists and device_is_wifi:
                # we need to only neglect wifi devices
                # paired usb device need to still show in the display
                continue
            elif device_exists_in_view:
                # devices exists in the list with the same status and
                # we should not add the new detected list item
                continue
            # If and only if the device doesn't exist; add it
            self.devices_view.addItem(devices_view_list_item)
        return __devices

    def remove_device_device_view(self, identifier: str = '', statuses=()):
        """
        Removes all QListWidgetItems from the device_view for all matching
        identifier
        :param identifier: str
        :param statuses: Iterable
        :return:
        """
        for index in range(self.devices_view.count() - 1, -1, -1):
            for status in statuses:
                if self.devices_view.item(index):
                    if str(identifier) in self.devices_view.item(index).text()\
                            and \
                            str(status) in \
                            self.devices_view.item(index).text():
                        self.devices_view.takeItem(index)
        return

    def __dimension_change_cb(self):
        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            config['dimension'] = None
            self.dimensionText.setInputMask("")
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

    def __dial_change_cb(self):
        config['bitrate'] = int(self.dial.value())
        self.bitrateText.setText(str(config['bitrate']) + "KB/s")

    def progress(self, val):
        self.progressBar.setValue(val)
        if (val + 4) >= 100:
            return 100
        else:
            return val + 100 / 20

    @staticmethod
    def is_device_unusable(status):
        if any(('unauth' in status, 'offline' in status)):
            return True
        else:
            return False

    def show_device_status_failure(self, status):
        self.display_public_message(
            f"Device is {status}. Please reconnect / press allow."
        )

    def __reset_message_box_stylesheet(self):
        stylesheet = \
            "background-color: qlineargradient(" \
            "spread:pad, x1:0, y1:0, x2:1, y2:1, " \
            "stop:0 rgba(0, 255, 255, 255), " \
            "stop:1 rgba(0, 255, 152, 255)); " \
            "border-radius: 10px;"
        self.private_message_box_adb.setStyleSheet(stylesheet)

    def __select_first_device(self):
        self.devices_view.setCurrentIndex(
            QModelIndex(self.devices_view.model().index(0, 0))
        )

    def display_public_message(self, message):
        """
        sets the message box information (GUI) with the string message
        :param message: str
        :return: None
        """
        self.private_message_box_adb.setText(message)

    def start_act(self):
        """
        Main brain of guiscrcpy; handles what to do when
        :return:
        """
        # prepare launch of scrcpy,
        # reset colors
        # reset vars

        # 1: reset
        self.options = ""
        progress = self.progress(0)
        self.__reset_message_box_stylesheet()

        # ====================================================================
        # 2: Update UI to start checking
        self.display_public_message("CHECKING DEVICE CONNECTION")
        initial_time = time.time()
        progress = self.progress(progress)

        # ====================================================================
        # 3: Check devices
        values_devices_list = self.scan_devices_update_list_view()
        if len(values_devices_list) == 0:
            # Could not detect any device
            self.display_public_message("Could not find any devices")
            return 0
        elif self.devices_view.currentIndex() is None and \
                len(values_devices_list) != 1:
            # No device is selected and more than one device found
            self.display_public_message("Please select a device below.")
            return 0
        else:
            # Device selected
            log("DEVICE LIST", len(values_devices_list), values_devices_list)
            if len(values_devices_list) == 1:
                # found only one device
                # ======================================================
                # Store the current rotation temporarily
                __selected_rotation = self.device_rotation.currentIndex()
                self.__select_first_device()
                # Restore the selected rotation
                self.device_rotation.setCurrentIndex(__selected_rotation)
                # =======================================================
                # get the status and identifier of the device;
                # return if device is not in a connectable state
                try:
                    _, device_id, _stat = \
                        self.current_device_identifier(need_status=True)
                    if self.is_device_unusable(_stat):
                        self.show_device_status_failure(_stat)
                        return 0
                except ValueError:
                    self.display_public_message(
                        "Please select a device from the list view"
                    )
                    return 0
                more_devices = False
            elif self.devices_view.currentItem() is None:
                # no item is selected
                self.display_public_message("Please select a device below.")
                return 0
            else:
                _, device_id, _stat = self.current_device_identifier(
                    need_status=True)
                if self.is_device_unusable(_stat):
                    self.show_device_status_failure(_stat)
                    return 0
                log("Device_id = {}".format(device_id))
                more_devices = True
        progress = self.progress(progress)

        # ====================================================================
        # 4: Parse dimension slider
        # check if the defaultDimension is checked or not for giving signal
        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.dimensionText.setText("DEFAULT")
            config['dimension'] = None
        else:
            self.dimensionSlider.setEnabled(True)
            config['dimension'] = int(self.dimensionSlider.value())
            self.dimensionSlider.setValue(config['dimension'])
            self.dimensionText.setText(str(config['dimension']) + "px")
        # edit configuration files to update dimension key
        if config['dimension'] is None:
            self.options = " "
        elif config['dimension'] is not None:
            self.options = " -m " + str(config['dimension'])
        else:
            self.options = ""
        progress = self.progress(progress)

        # ====================================================================
        # 5: Check if always_on and fullscreen switches are on
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
            config['fullscreen'] = True
        else:
            config['fullscreen'] = False
        progress = self.progress(progress)

        # ====================================================================
        # 6: Check if show touches / recording are on
        if self.showTouches.isChecked():
            self.options += " --show-touches"
            config['swtouches'] = True
        else:
            config['swtouches'] = False
        progress = self.progress(progress)

        # ====================================================================
        # 7: Check if the record option is selected
        if self.recScui.isChecked():
            self.options += " -r " + str(int(time.time())) + ".mp4 "
        progress = self.progress(progress)

        # ====================================================================
        # 8: Check if the display is forced to be on
        if self.displayForceOn.isChecked():
            self.options += " -S"
            config['dispRO'] = True
        else:
            config['dispRO'] = False
        progress = self.progress(progress)

        # ====================================================================
        # 9: Parse bitrate
        # Bitrate is parsed, by editing the bitrate mask
        if self.bitrateText.text().split()[1][0] in ['K', 'M', 'T']:
            bitrate_multiplier = str(self.bitrateText.text().split()[1][0])
        elif self.bitrateText.text().split()[1][0] == "B":
            bitrate_multiplier = "B"
        else:
            # do not proceed. Invalid file size multiplier
            multiplier_error = f"Invalid file size multiplier \
            '{str(self.bitrateText.text().split()[1][0])}'. " \
                                               f"Please use only K, M, T only"
            print(multiplier_error)
            self.display_public_message(multiplier_error)
            return False
        if self.bitrateText.text().split()[0].isdigit():
            bitrate_integer = int(self.bitrateText.text().split()[0])
        else:
            bitrate_integer = 8000
        self.options += " -b {}{}".format(bitrate_integer, bitrate_multiplier)
        config['bitrate'] = bitrate_integer
        progress = self.progress(progress)

        # ====================================================================
        # 10: Make user aware that there were no problems in connection
        # or in the data provided by the user
        logger.debug("CONNECTION ESTABLISHED")
        self.progressBar.setValue(50)
        logger.debug("Flags passed to scrcpy engine : " + self.options)
        self.progressBar.setValue(60)
        config['extra'] = self.flaglineedit.text()
        progress = self.progress(progress)

        # ====================================================================
        # 11: Initialize User Experience Mapper
        ux = UXMapper(
            device_id=device_id,
            sha_shift=config.get('sha_shift', 5)
        )
        progress = self.progress(progress)
        always_on_top = \
            config.get('panels_always_on_top', False) or \
            not args.panels_not_always_on_top
        # ====================================================================
        # 12: Init side_panel if necessary
        if self.check_side_panel.isChecked():
            config['panels']['toolkit'] = True
            side_instance = InterfaceToolkit(
                parent=self,
                ux_mapper=ux,
                frame=args.force_window_frame,
                always_on_top=always_on_top
            )
            for instance in self.child_windows:
                if instance.ux.get_sha() == side_instance.ux.get_sha() and \
                        instance.name == side_instance.name and \
                        not instance.isHidden():
                    break
            else:
                side_instance.init()
                self.child_windows.append(side_instance)
        else:
            config['panels']['toolkit'] = False
        progress = self.progress(progress)

        # ====================================================================
        # 13: Init bottom_panel if necessary
        if self.check_bottom_panel.isChecked():
            config['panels']['bottom'] = True
            panel_instance = Panel(
                parent=self,
                ux_mapper=ux,
                frame=args.force_window_frame,
                always_on_top=always_on_top
            )
            for instance in self.child_windows:
                if instance.ux.get_sha() == panel_instance.ux.get_sha() and \
                        instance.name == panel_instance.name and \
                        not instance.isHidden():
                    break
            else:
                panel_instance.init()
                self.child_windows.append(panel_instance)
        else:
            config['panels']['bottom'] = False
        progress = self.progress(progress)

        # ====================================================================
        # 14: Init swipe panel if necessary
        if self.check_swipe_panel.isChecked():
            config['panels']['swipe'] = True
            swipe_instance = SwipeUX(
                ux_wrapper=ux,
                frame=args.force_window_frame,
                always_on_top=always_on_top
            )  # Load swipe UI
            for instance in self.child_windows:
                if instance.ux.get_sha() == swipe_instance.ux.get_sha() and \
                        instance.name == swipe_instance.name and \
                        not instance.isHidden():
                    break
            else:
                swipe_instance.init()
                self.child_windows.append(swipe_instance)
        else:
            config['panels']['swipe'] = False
        progress = self.progress(progress)

        # ====================================================================
        # 15: Generate uuid for device and set uuid color for PMBA
        hexdigest = ux.get_sha()[:6]
        stylesheet = f"background-color: #{hexdigest}; border-radius: 10px; "
        self.private_message_box_adb.setStyleSheet(stylesheet)
        progress = self.progress(progress)

        # ====================================================================
        # 16: Update device specific configuration
        model, identifier = self.current_device_identifier()
        # ====================================================================
        # 17: Parse rotation (scrcpy v1.13+)
        rotation_index = self.device_rotation.currentIndex() - 1
        if self.lock_rotation.isChecked():
            rotation_parameter = "--lock-video-orientation"
        else:
            rotation_parameter = "--rotation"
        if rotation_index != -1:
            self.options += " {} {}".format(rotation_parameter, rotation_index)
            config['device'][identifier]['rotation'] = \
                rotation_index + 1
        else:
            config['device'][identifier]['rotation'] = 0

        # ====================================================================
        # 18: Update device specific configuration
        if identifier.count('.') >= 3 and identifier[-1].isdigit():
            config['device'][identifier]['wifi'] = True
            config['device'][identifier]['model'] = model

        # ====================================================================
        # 16: Parse scrcpy arguments
        if self.cmx is not None:
            config['cmx'] = ' '.join(map(str, self.cmx))

        arguments_scrcpy = "{} {} {}".format(
            self.options,
            config['extra'],
            config['cmx']
        )
        progress = self.progress(progress)

        # ====================================================================
        # 18: Handle more devices
        if more_devices:
            # guiscrcpy found more devices
            # scrcpy will fail if more than one device is found
            # its important to pass the device serial id, if more than one
            # device is found
            arguments_scrcpy = f"-s {device_id} {arguments_scrcpy}"

        # tell end users that the color of the device is this
        self.display_public_message(
            f"Device {device_id} is connected; (color id matches "
            f"toolkit color)"
        )
        log("Device connection completed successfully.")
        log("Private message box updated successfully")
        progress = self.progress(progress)

        # ====================================================================
        # 19: spawn scrcpy
        if not args.noscrcpy:
            # for debugging purposes, its important to not start scrcpy
            # every time
            scrcpy.start(scrcpy.path, arguments_scrcpy)
        progress = self.progress(progress)

        # ====================================================================
        # 20: Calculate time
        final_time = time.time()
        eta = final_time - initial_time
        print("scrcpy launched in {:.2f}s".format(eta))
        progress = self.progress(progress)

        # ====================================================================
        # 22: Update configuration
        cfgmgr.update_config(config)
        cfgmgr.write_file()
        progress = self.progress(progress)

        return self.progress(progress)


def bootstrap0():
    """
    Launch the guiscrcpy window
    :return:
    """
    # enable High DPI scaling
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(
        QtCore.Qt.AA_UseHighDpiPixmaps, True
    )  # use HIGH DPI icons
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle(args.theme)

    if args.theme == 'Breeze':
        # The Qdarkstylesheet is based on Breeze, lets load them on default
        app.setStyleSheet(dark_stylesheet())

    splash_pix = QPixmap(":/res/ui/guiscrcpy-branding.png")
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    cfg_edited = False

    if (adb.path is None) or (not os.path.exists(adb.path)):
        adb.path = open_exe_name_dialog(None, 'adb')
        cfg_edited = True
        config['adb'] = adb.path

    if (scrcpy.path is None) or (not os.path.exists(scrcpy.path)):
        scrcpy.path = open_exe_name_dialog(None, 'scrcpy')
        cfg_edited = True
        config['scrcpy'] = scrcpy.path

    # on windows, users are likely not to add the scrcpy-server to the
    # SCRCPY_SERVER_PATH
    scrcpy_server_path_env = os.getenv('SCRCPY_SERVER_PATH', None)
    if scrcpy_server_path_env:
        if os.path.exists(scrcpy_server_path_env):
            config['scrcpy-server'] = scrcpy.server_path
        else:
            scrcpy.server_path = open_exe_name_dialog(None, 'scrcpy-server')
            cfg_edited = True
            config['scrcpy-server'] = scrcpy.server_path
            os.environ['SCRCPY_SERVER_PATH'] = scrcpy.server_path
    elif (
        (scrcpy.server_path is None) or
        (not os.path.exists(scrcpy.server_path))
    ) and (
        platform.System().system() == 'Windows'
    ):
        scrcpy.server_path = open_exe_name_dialog(None, 'scrcpy-server')
        cfg_edited = True
        config['scrcpy-server'] = scrcpy.server_path
        os.environ['SCRCPY_SERVER_PATH'] = scrcpy.server_path
    elif platform.System().system() == "Windows":
        os.environ['SCRCPY_SERVER_PATH'] = scrcpy.server_path

    if cfg_edited:
        cfgmgr.update_config(config)
        cfgmgr.write_file()

    if args.killserver:
        adb.command(adb.path, 'kill-server')
        adb.command(adb.path, 'start-server')
    else:
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
        logger.debug(f"E:{e}. Continuing to run guiscrcpy.")

    # add current path to path
    sys.path.append('')

    # bootstrap guiscrcpy
    bootstrap0()


def bootstrap():
    from guiscrcpy import __path__
    patz1 = list(__path__)[0]
    sys.path.append(patz1)
    bootstrap0()

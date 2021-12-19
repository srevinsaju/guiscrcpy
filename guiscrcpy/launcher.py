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

import hashlib
import os
import subprocess
import sys
import time
import webbrowser
from subprocess import PIPE
from subprocess import Popen

from qtpy import QtCore, QtWidgets
from qtpy.QtCore import QModelIndex, QPoint
from qtpy.QtGui import QPixmap, QIcon, QFont, QFontDatabase
from qtpy.QtWidgets import QMainWindow, QListWidgetItem, QMenu
from qtpy.QtWidgets import QMessageBox

from .lib.bridge.audio.sndcpy import SndcpyBridge
from .lib.bridge.audio.usbaudio import USBAudioBridge
from .lib.config import InterfaceConfig
from .lib.utils import format_colors as fc
from .constants import FONTS
from .install.finder import open_exe_name_dialog
from .lib.process import is_running
from .lib.toolkit import UXMapper
from .lib.utils import log, get_self
from .platform import platform
from .theme.desktop_shortcut import desktop_device_shortcut_svg
from .theme.linux_desktop_shortcut_template import GUISCRCPY_DEVICE
from .theme.style import dark_stylesheet
from .ux import Ui_MainWindow
from .ux.panel import Panel
from .ux.swipe import SwipeUX
from .ux.toolkit import InterfaceToolkit
from .version import VERSION
from .lib.bridge import AndroidDebugBridge, ScrcpyBridge
from .lib.bridge.exceptions import ScrcpyServerNotFoundError


environment = platform.System()

# ============================================================================
# Load cairo-svg conditionally
if environment.system() == "Linux":
    try:
        from cairosvg import svg2png  # noqa:

        has_cairo = True
    except Exception as e:
        print("Failed to load cairo:", e)
        print("Some features are likely to be disabled")
        has_cairo = False


class InterfaceGuiscrcpy(QMainWindow, Ui_MainWindow):
    """
    Main class for guiscrcpy object.
    All the processes to spawn to scrcpy are handled here
    """

    # noinspection PyArgumentList
    def __init__(
        self,
        config_manager: InterfaceConfig,
        adb: AndroidDebugBridge,
        scrcpy: ScrcpyBridge,
        force_window_frame: bool = False,
        panels_not_always_on_top: bool = False,
        debug_no_scrcpy: bool = False,
    ):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._adb = adb
        self._scrcpy = scrcpy
        self.config_manager = config_manager
        config = self.config_manager.get_config()
        self._config = config
        self.panels_not_always_on_top = panels_not_always_on_top
        self.force_window_frame = force_window_frame
        self.debug__no_scrcpy = debug_no_scrcpy
        self.cmx = None
        self.sm = None
        self.mp = None
        self.nm = None
        self.swipe_instance = None
        self.panel_instance = None
        self.side_instance = None
        self.child_windows = list()
        self.options = ""
        log(
            "Options received by class are : {} {} {} {} {} ".format(
                config["bitrate"],
                config["dimension"],
                config["swtouches"],
                config["dispRO"],
                config["fullscreen"],
            )
        )
        # ====================================================================
        # Rotation; read config, update UI
        self.device_rotation.setCurrentIndex(config.get("rotation", 0))
        self.dial.setValue(int(config["bitrate"]))
        if config["swtouches"]:
            self.showTouches.setChecked(True)
        else:
            self.showTouches.setChecked(False)
        if config["dispRO"]:
            self.displayForceOn.setChecked(True)
        else:
            self.displayForceOn.setChecked(False)

        # panels
        if config["panels"].get("swipe"):
            self.check_swipe_panel.setChecked(True)
        else:
            self.check_swipe_panel.setChecked(False)
        if config["panels"].get("tookit"):
            self.check_side_panel.setChecked(True)
        else:
            self.check_side_panel.setChecked(False)
        if config["panels"].get("bottom"):
            self.check_bottom_panel.setChecked(True)
        else:
            self.check_bottom_panel.setChecked(False)

        # dimension
        if config["dimension"] is not None:
            self.dimensionDefaultCheckbox.setChecked(False)
            try:
                self.dimensionSlider.setValue(config["dimension"])
            except TypeError:
                self.dimensionDefaultCheckbox.setChecked(True)
        if config["fullscreen"]:
            self.fullscreen.setChecked(True)
        else:
            self.fullscreen.setChecked(False)
        if is_running("scrcpy"):
            log("SCRCPY RUNNING")
            self.display_public_message("SCRCPY SERVER RUNNING")
        else:
            log("SCRCPY SERVER IS INACTIVE")
            self.display_public_message("SCRCPY SERVER NOT RUNNING")

        # CONNECT DIMENSION CHECK BOX TO STATE CHANGE
        self.dimensionDefaultCheckbox.stateChanged.connect(self.__dimension_change_cb)
        self.build_label.setText("Build {} by srevinsaju".format(VERSION))

        # DIAL CTRL GRP
        self.dial.sliderMoved.connect(self.__dial_change_cb)
        self.dial.sliderReleased.connect(self.__dial_change_cb)
        # DIAL CTRL GRP

        # MAIN EXECUTE ACTION
        self.executeaction.clicked.connect(self.start_act)
        try:
            if config["extra"]:
                self.flaglineedit.setText(config["extra"])
        except Exception as err:
            log(f"Exception: flaglineedit.text(config[extra]) {err}")

        self.quit.clicked.connect(self.quit_window)
        self.dimensionText.setText("DEFAULT")
        config["bitrate"] = int(self.dial.value())
        self.bitrateText.setText(str(config["bitrate"]) + "KB/s")
        self.pushButton.setText("RESET")
        self.pushButton.clicked.connect(self.reset)
        self.abtgit.clicked.connect(self.launch_web_github)
        self.usbaud.clicked.connect(self.launch_usb_audio)
        self.initmapnow.clicked.connect(self.bootstrap_mapper)
        self.network_button.clicked.connect(self.network_mgr)
        self.settings_button.clicked.connect(self.settings_mgr)
        # self.devices_view.itemChanged.connect(self.update_rotation_combo_cb)
        self.devices_view.itemClicked.connect(self.update_rotation_combo_cb)
        self.refreshdevices.clicked.connect(self.scan_devices_update_list_view)
        self.restart_adb_server.clicked.connect(self.restart_adb_server_guiscrcpy)
        self.devices_view.itemClicked.connect(self.more_options_device_view)
        self.devices_view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.scan_config_devices_update_list_view()
        self.refresh_devices()

    @property
    def adb(self) -> AndroidDebugBridge:
        return self._adb

    @property
    def scrcpy(self) -> ScrcpyBridge:
        return self._scrcpy

    @property
    def config(self) -> dict:
        return self._config

    def restart_adb_server_guiscrcpy(self):
        self.adb.kill_adb_server()

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
            _rotation = (
                self.config.get("device")
                .get(device_id, dict())
                .get("rotation", self.device_rotation.currentIndex())
            )
        else:
            _rotation = self.config.get("rotation", self.device_rotation.currentIndex())
        self.device_rotation.setCurrentIndex(_rotation)

    def settings_mgr(self):
        from guiscrcpy.ux.settings import InterfaceSettings

        self.sm = InterfaceSettings(self)
        self.sm.init()
        self.sm.show()

    def network_mgr(self):
        from guiscrcpy.ux.network import InterfaceNetwork

        self.nm = InterfaceNetwork(self.adb)
        self.nm.init()
        self.nm.show()

    def bootstrap_mapper(self):
        mapper_config_path = os.path.join(
            self.config_manager.get_cfgpath(), "guiscrcpy.mapper.json"
        )
        if os.path.exists(mapper_config_path):
            from guiscrcpy.lib.mapper.mapper import MapperAsync

            _, identifier = self.current_device_identifier()
            self.mp = MapperAsync(
                self,
                device_id=identifier,
                config_path=mapper_config_path,
                adb=self.adb,
                initialize=False,
            )
            self.mp.start()
            self.private_message_box_adb.setText("guiscrcpy-mapper has started")
        else:
            message_box = QMessageBox()
            message_box.setText(
                "guiscrcpy mapper is not initialized yet. Do you want to "
                "initialize it now?"
            )
            message_box.setInformativeText(
                "Before you initialize, make sure your phone is connected and "
                "the display is switched on to map the points."
            )
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            user_message_box_response = message_box.exec()
            values_devices_list = self.scan_devices_update_list_view()
            self.check_devices_status_and_select_first_if_only_one(
                values_devices_list=values_devices_list
            )
            # TODO: allow enabling mapper from inside
            if user_message_box_response == QMessageBox.Yes:
                self.private_message_box_adb.setText("Initializing mapper...")
                print("Make sure your phone is connected and display is " "switched on")
                print(
                    "Reset mapper if you missed any "
                    "steps by 'guiscrcpy --mapper-reset'"
                )
                print()
                print(
                    "If at first you don't succeed... "
                    "reset, reset and reset again! :D"
                )
                print()
                _, identifier = self.current_device_identifier()
                executable = get_self()
                from .lib.utils import shellify as sx, open_process

                open_process(
                    sx("{} mapper".format(executable)),
                    stdout=sys.stdout,
                    stdin=sys.stdin,
                    stderr=sys.stderr,
                    cwd=os.getcwd(),
                )
                print("Mapper started")
                self.private_message_box_adb.setText("Mapper initialized")

    def launch_usb_audio(self):
        android_api_level = self.adb.get_target_android_version()

        if android_api_level == -1:
            return

        print("Detected device API level: " + str(android_api_level))

        if android_api_level >= 29:
            print("Using Sndcpy as audio bridge")
            audio_bridge = SndcpyBridge()
        else:
            print("Using USBAudio as audio bridge")
            audio_bridge = USBAudioBridge()

        # FIXME: provide the right device id
        audio_bridge.run(device_id=None)

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
        about_message_box.addButton("OK", about_message_box.hide)  # noqa:
        about_message_box.show()

    def reset(self):
        """
        Remove configuration files; Reset the mapper and guiscrcpy.json
        :return:
        """
        self.config_manager.reset_config()
        log("CONFIGURATION FILE REMOVED SUCCESSFULLY")
        log("RESTART")
        message_box = QMessageBox().window()
        message_box.about(
            self.pushButton,
            "Info",
            "Please restart guiscrcpy to reset the settings. "
            "guiscrcpy will now exit",
        )
        QMessageBox.ButtonRole()
        message_box.addButton("OK", self.quit_window)  # noqa:
        message_box.show()

    def quit_window(self):
        """
        A method to quit the main window
        :return:
        """
        try:
            self.mp.exit()
        except (AttributeError, KeyboardInterrupt):
            pass
        sys.exit()

    def forget_paired_device(self):
        """
        Forgets / Removes the configuration for saved
        :return: popped item / False
        """
        try:
            _, identifier = self.current_device_identifier()
            popped_device = self.config["device"].pop(identifier)
            self.refresh_devices()
            self.config_manager.update_config(self.config)
            self.config_manager.write_file()
            return popped_device
        except KeyError:
            return False

    def more_options_device_view(self, button):
        if "Disconnect" in button.text():
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
        if platform.System.system() == "Linux" and identifier.count(".") >= 3:
            menu.addAction(
                "Add Desktop Shortcut to this device",
                self.create_desktop_shortcut_linux_os,
            )
        menu.exec_(
            self.devices_view.mapToGlobal(
                QPoint(
                    self.devices_view.visualItemRect(button).x() + 22,
                    self.devices_view.visualItemRect(button).y() + 22,
                )
            )
        )

    def create_desktop_shortcut_linux_os(self) -> bool:
        """
        Creates a desktop shortcut for Linux OS
        :return: bool
        """
        # just a check before anything further happens because of an
        # unrelated OS
        if environment.system() != "Linux":
            log(
                "Tried to run create_desktop_shortcut_linux_os on an " "unsupported OS."
            )
            return False

        # get device specific configuration
        model, identifier = self.current_device_identifier()
        picture_file_path = self.config_manager.get_cfgpath()
        __sha_shift = self.config.get("sha_shift", 5)
        sha = hashlib.sha256(str(identifier).encode()).hexdigest()[
            __sha_shift : __sha_shift + 6
        ]
        log(f"Creating desktop shortcut sha: {sha}")
        path_to_image = os.path.join(picture_file_path, identifier + ".png")
        if has_cairo:
            svg2png(
                bytestring=desktop_device_shortcut_svg().format(f"#{sha}"),
                write_to=path_to_image,
            )
        else:
            print("Trying to use Plain SVG as renderer" " instead of cairo")
            with open(path_to_image, "w") as fp:
                svg_str = desktop_device_shortcut_svg().format(f"#{sha}")
                fp.write(svg_str)

        # go through all args; break when we find guiscrcpy
        for args_i in range(len(sys.argv)):
            if "guiscrcpy" in sys.argv[args_i]:
                aend = args_i + 1
                break
        else:
            aend = None

        sys_args_desktop = sys.argv[:aend]

        # check if its a python file
        # experimental support for AppImages / snaps
        # I am not sure; if it would work indeed
        for i in sys_args_desktop:
            if i.endswith(".py"):
                needs_python = True
                break
        else:
            needs_python = False
        if needs_python:
            sys_args_desktop = ["python3"] + sys_args_desktop

        # convert the list into a string
        sys_args_desktop = " ".join(sys_args_desktop)
        auto_connect_run_command = (
            "{executable} --connect={ip} "
            "--start --start-scrcpy-device-id={ip}".format(
                executable=sys_args_desktop, ip=identifier
            )
        )

        # create the desktop file using linux's desktop file gen method
        path_to_desktop_file = platform.System().create_desktop(
            desktop_file=GUISCRCPY_DEVICE.format(
                identifier=model,
                command=auto_connect_run_command,
                icon_path=path_to_image,
            ),
            desktop_file_name=f"{model}.guiscrcpy.desktop",
        )

        # announce it to developers / users
        log(f"Path to desktop file : {path_to_desktop_file}")
        print("Desktop file generated successfully")
        self.display_public_message("Desktop file has been created")
        return True

    def is_connection_success_handler(self, output: Popen, ip=None):
        out, err = output.communicate()
        if "failed" in out.decode() or "failed" in err.decode():
            self.display_public_message(
                "Failed to connect to {}. See the logs for more "
                "information".format(ip)
            )
            print("adb:", out.decode(), err.decode())
        else:
            self.display_public_message("Connection command completed successfully")

    def ping_paired_device(self, device_id=None):
        # update the configuration file first
        if not device_id:
            _, identifier = self.current_device_identifier()
            if identifier.count(".") == 3:
                wifi_device = True
            else:
                wifi_device = False
            try:
                self.config["device"][identifier]["wifi"] = wifi_device
            except KeyError:
                log(f"Failed writing the configuration " f"'wifi' key to {identifier}")

            if wifi_device:
                ip = self.current_device_identifier()[1]
                output = self.adb.command("connect {}".format(ip))
                self.is_connection_success_handler(output, ip=ip)
            else:
                self.adb.command("reconnect offline")
            # As we have attempted to connect; refresh the panel
            self.refresh_devices()
        else:
            output = self.adb.command("connect {}".format(device_id))
            self.is_connection_success_handler(output, ip=device_id)

    def tcpip_paired_device(self):
        if self.devices_view.currentItem():
            _, identifier = self.current_device_identifier()
        else:
            identifier = ""
        __exit_code = self.adb.tcpip(identifier=identifier)
        if __exit_code != 0:
            self.display_public_message(
                "TCP/IP failed on device. " "Please reconnect USB and try again"
            )
        else:
            self.display_public_message("TCP/IP completed successfully.")
            time.sleep(0.1)  # wait for everything to get settled
            if identifier.count(".") >= 3:
                self.ping_paired_device(device_id=identifier)
            else:
                self.ping_paired_device()

    def current_device_identifier(self, need_status=False):
        if self.devices_view.currentItem():
            if need_status:
                return (
                    self.devices_view.currentItem().text().split()[0],
                    self.devices_view.currentItem().text().split()[1],
                    self.devices_view.currentItem().text().split()[2],
                )
            else:
                return (
                    self.devices_view.currentItem().text().split()[0],
                    self.devices_view.currentItem().text().split()[1],
                )
        else:
            raise ValueError("No item is selected in QListView")

    def scan_config_devices_update_list_view(self):
        """
        Scans for saved devices
        :return:
        """
        self.devices_view.clear()
        paired_devices = self.config["device"]
        for i in paired_devices:
            if paired_devices[i].get("wifi"):
                icon = ":/icons/icons/portrait_mobile_disconnect.svg"
                devices_view_list_item = QListWidgetItem(
                    QIcon(icon),
                    "{device}\n{mode}\n{status}".format(
                        device=paired_devices[i].get("model"),
                        mode=i,
                        status="Disconnected",
                    ),
                )
                __sha_shift = self.config.get("sha_shift", 5)
                __sha = hashlib.sha256(str(i).encode()).hexdigest()[
                    __sha_shift : __sha_shift + 6
                ]
                devices_view_list_item.setToolTip(
                    "<span style='color: #{color}'>Device</snap>: <b>{d}</b>\n"
                    "Status: {s}".format(
                        d=i,
                        s="Disconnected. Right click 'ping' to attempt " "reconnect",
                        color=__sha,
                    )
                )
                devices_view_list_item.setFont(QFont("Noto Sans", 8))
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

        __devices = self.adb.devices_detailed()
        log(__devices)
        for i in __devices:
            device_is_wifi = i["identifier"].count(".") >= 3 and (
                ":" in i["identifier"]
            )

            if i["identifier"] not in self.config["device"].keys():
                device_paired_and_exists = False
                self.config["device"][i["identifier"]] = {"rotation": 0}
            else:
                device_paired_and_exists = True

            if device_is_wifi:
                _icon_suffix = "_wifi"
            else:
                _icon_suffix = "_usb"

            icon = ":/icons/icons/portrait_mobile_white{}.svg".format(_icon_suffix)

            if i["status"] == "offline":
                icon = ":/icons/icons/portrait_mobile_error.svg"
            elif i["status"] == "unauthorized":
                icon = ":/icons/icons/portrait_mobile_warning.svg"

            if i["status"] == "no_permission":
                log("pairfilter: 5")
                # https://stackoverflow.com/questions/
                # 53887322/adb-devices-no-permissions-user-in-
                # plugdev-group-are-your-udev-rules-wrong
                udev_error = (
                    "Error connecting to device. Your udev rules are"
                    " incorrect. See https://stackoverflow.com/questions"
                    "/53887322/adb-devices-no-permissions-user-in-plugdev-"
                    "group-are-your-udev-rules-wrong"
                )
                self.display_public_message(udev_error)
                print(udev_error)
                return []
            # Check if device is unauthorized
            elif i["status"] == "unauthorized":
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
                    i["identifier"], statuses=["offline", "unauthorized"]
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
                        if paired_device.text().split()[0] == i["model"]:
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
                                i["identifier"], statuses=["offline", "unauthorized"]
                            )
                            break
                        elif paired_device.text().split()[1] == i["identifier"]:
                            log("pairfilter: 2")
                            self.remove_device_device_view(
                                i["identifier"], statuses=["offline", "unauthorized"]
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
                    device=i["model"], mode=i["identifier"], status=i["status"]
                )
            )
            __sha_shift = self.config.get("sha_shift", 5)
            __sha = hashlib.sha256(str(i["identifier"]).encode()).hexdigest()[
                __sha_shift : __sha_shift + 6
            ]
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
                    d=i["identifier"],
                    m=i["model"],
                    a=i["product"],
                    s=i["status"],
                    t=i["transport_id"],
                    p=paired,
                    color=__sha,
                    inv_color=str(hex(0xFFFFFF - int(__sha, 16))[2:]),
                )
            )

            devices_view_list_item.setFont(QFont("Noto Sans", 8))
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

    def remove_device_device_view(self, identifier: str = "", statuses=()):
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
                    if (
                        str(identifier) in self.devices_view.item(index).text()
                        and str(status) in self.devices_view.item(index).text()
                    ):
                        self.devices_view.takeItem(index)
        return

    def __dimension_change_cb(self):
        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.config["dimension"] = None
            self.dimensionText.setInputMask("")
            self.dimensionText.setText("DEFAULT")
        else:
            self.dimensionSlider.setEnabled(True)
            self.config["dimension"] = int(self.dimensionSlider.value())
            self.dimensionText.setText(" " + str(self.config["dimension"]) + "px")
            self.dimensionSlider.sliderMoved.connect(self.__slider_change_cb)
            self.dimensionSlider.sliderReleased.connect(self.__slider_change_cb)

    def __slider_change_cb(self):
        self.config["dimension"] = int(self.dimensionSlider.value())
        self.dimensionText.setText(str(self.config["dimension"]) + "px")

    def __dial_change_cb(self):
        self.config["bitrate"] = int(self.dial.value())
        self.bitrateText.setText(str(self.config["bitrate"]) + "KB/s")

    def progress(self, val):
        self.progressBar.setValue(int(val))
        if (val + 4) >= 100:
            return 100
        else:
            return val + 100 / 20

    @staticmethod
    def is_device_unusable(status):
        if any(("unauth" in status, "offline" in status)):
            return True
        else:
            return False

    def show_device_status_failure(self, status):
        self.display_public_message(
            f"Device is {status}. Please reconnect / press allow."
        )

    def __reset_message_box_stylesheet(self):
        stylesheet = (
            "background-color: qlineargradient("
            "spread:pad, x1:0, y1:0, x2:1, y2:1, "
            "stop:0 rgba(0, 255, 255, 255), "
            "stop:1 rgba(0, 255, 152, 255)); "
            "border-radius: 10px;"
        )
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

    def check_devices_status_and_select_first_if_only_one(self, values_devices_list):
        """
        Checks the devices in the Grid View, and then checks if any device
        is available or offline accordingly display the error message. If
        only one device was detected, automatically select the first device
        and check its status of connectivity. Return the selected device if
        multiple devices were detected by adb. Return device_id, status and
        a bool more_devices if more than one device was found
        :param values_devices_list:
        :type values_devices_list:
        :return:
        :rtype:
        """
        if len(values_devices_list) == 0:
            # Could not detect any device
            self.display_public_message("Could not find any devices")
            return 0
        elif self.devices_view.currentIndex() is None and len(values_devices_list) != 1:
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
                    _, device_id, _stat = self.current_device_identifier(
                        need_status=True
                    )
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
                _, device_id, _stat = self.current_device_identifier(need_status=True)
                if self.is_device_unusable(_stat):
                    self.show_device_status_failure(_stat)
                    return 0
                log("Device_id = {}".format(device_id))
                more_devices = True
        return device_id, more_devices, _stat

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
        _e = self.check_devices_status_and_select_first_if_only_one(values_devices_list)
        if _e is None or isinstance(_e, int):
            return _e
        device_id, more_devices, _stat = _e
        progress = self.progress(progress)

        # ====================================================================
        # 4: Parse dimension slider
        # check if the defaultDimension is checked or not for giving signal
        if self.dimensionDefaultCheckbox.isChecked():
            self.dimensionSlider.setEnabled(False)
            self.dimensionText.setText("DEFAULT")
            self.config["dimension"] = None
        else:
            self.dimensionSlider.setEnabled(True)
            self.config["dimension"] = int(self.dimensionSlider.value())
            self.dimensionSlider.setValue(self.config["dimension"])
            self.dimensionText.setText(str(self.config["dimension"]) + "px")
        # edit configuration files to update dimension key
        if self.config["dimension"] is None:
            self.options = " "
        elif self.config["dimension"] is not None:
            self.options = " -m " + str(self.config["dimension"])
        else:
            self.options = ""
        progress = self.progress(progress)

        # ====================================================================
        # 5: Check if always_on and fullscreen switches are on
        if self.aotop.isChecked():
            self.options += " --always-on-top"
        if self.fullscreen.isChecked():
            self.options += " -f"
            self.config["fullscreen"] = True
        else:
            self.config["fullscreen"] = False
        progress = self.progress(progress)

        # ====================================================================
        # 6: Check if show touches / recording are on
        if self.showTouches.isChecked():
            self.options += " --show-touches"
            self.config["swtouches"] = True
        else:
            self.config["swtouches"] = False
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
            self.config["dispRO"] = True
        else:
            self.config["dispRO"] = False
        progress = self.progress(progress)

        # ====================================================================
        # 9: Parse bitrate
        # Bitrate is parsed, by editing the bitrate mask
        if self.bitrateText.text().split()[1][0] in ["K", "M", "T"]:
            bitrate_multiplier = str(self.bitrateText.text().split()[1][0])
        elif self.bitrateText.text().split()[1][0] == "B":
            bitrate_multiplier = "B"
        else:
            # do not proceed. Invalid file size multiplier
            multiplier_error = (
                f"Invalid file size multiplier \
            '{str(self.bitrateText.text().split()[1][0])}'. "
                f"Please use only K, M, T only"
            )
            print(multiplier_error)
            self.display_public_message(multiplier_error)
            return False
        if self.bitrateText.text().split()[0].isdigit():
            bitrate_integer = int(self.bitrateText.text().split()[0])
        else:
            bitrate_integer = 8000
        self.options += " -b {}{}".format(bitrate_integer, bitrate_multiplier)
        self.config["bitrate"] = bitrate_integer
        progress = self.progress(progress)

        # ====================================================================
        # 10: Make user aware that there were no problems in connection
        # or in the data provided by the user
        log("CONNECTION ESTABLISHED")
        self.progressBar.setValue(50)
        log("Flags passed to scrcpy engine : " + self.options)
        self.progressBar.setValue(60)
        self.config["extra"] = self.flaglineedit.text()
        progress = self.progress(progress)

        # ====================================================================
        # 11: Initialize User Experience Mapper
        ux = UXMapper(
            adb=self.adb, device_id=device_id, sha_shift=self.config.get("sha_shift", 5)
        )
        progress = self.progress(progress)
        always_on_top = (
            self.config.get("panels_always_on_top", False)
            or not self.panels_not_always_on_top
        )
        # ====================================================================
        # 12: Init side_panel if necessary
        if self.check_side_panel.isChecked():
            self.config["panels"]["toolkit"] = True
            side_instance = InterfaceToolkit(
                parent=self,
                ux_mapper=ux,
                frame=self.force_window_frame,
                always_on_top=always_on_top,
            )
            for instance in self.child_windows:
                if (
                    instance.ux.get_sha() == side_instance.ux.get_sha()
                    and instance.name == side_instance.name
                    and not instance.isHidden()
                ):
                    break
            else:
                side_instance.init()
                self.child_windows.append(side_instance)
        else:
            self.config["panels"]["toolkit"] = False
        progress = self.progress(progress)

        # ====================================================================
        # 13: Init bottom_panel if necessary
        if self.check_bottom_panel.isChecked():
            self.config["panels"]["bottom"] = True
            panel_instance = Panel(
                parent=self,
                ux_mapper=ux,
                frame=self.force_window_frame,
                always_on_top=always_on_top,
            )
            for instance in self.child_windows:
                if (
                    instance.ux.get_sha() == panel_instance.ux.get_sha()
                    and instance.name == panel_instance.name
                    and not instance.isHidden()
                ):
                    break
            else:
                panel_instance.init()
                self.child_windows.append(panel_instance)
        else:
            self.config["panels"]["bottom"] = False
        progress = self.progress(progress)

        # ====================================================================
        # 14: Init swipe panel if necessary
        if self.check_swipe_panel.isChecked():
            self.config["panels"]["swipe"] = True
            swipe_instance = SwipeUX(
                ux_wrapper=ux,
                frame=self.force_window_frame,
                always_on_top=always_on_top,
            )  # Load swipe UI
            for instance in self.child_windows:
                if (
                    instance.ux.get_sha() == swipe_instance.ux.get_sha()
                    and instance.name == swipe_instance.name
                    and not instance.isHidden()
                ):
                    break
            else:
                swipe_instance.init()
                self.child_windows.append(swipe_instance)
        else:
            self.config["panels"]["swipe"] = False
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
            self.config["device"][identifier]["rotation"] = rotation_index + 1
        else:
            self.config["device"][identifier]["rotation"] = 0

        # ====================================================================
        # 18: Update device specific configuration
        if identifier.count(".") >= 3 and identifier[-1].isdigit():
            self.config["device"][identifier]["wifi"] = True
            self.config["device"][identifier]["model"] = model

        # ====================================================================
        # 16: Parse scrcpy arguments
        if self.cmx is not None:
            self.config["cmx"] = " ".join(map(str, self.cmx))

        arguments_scrcpy = "{} {} {}".format(
            self.options, self.config["extra"], self.config["cmx"]
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
            f"Device {device_id} is connected; (color id matches " f"toolkit color)"
        )
        log("Device connection completed successfully.")
        log("Private message box updated successfully")
        progress = self.progress(progress)

        # ====================================================================
        # 19: spawn scrcpy
        if not self.debug__no_scrcpy:
            # for debugging purposes, its important to not start scrcpy
            # every time
            self.scrcpy.start(arguments_scrcpy, stdout=sys.stdout, stderr=sys.stderr)
        progress = self.progress(progress)

        # ====================================================================
        # 20: Calculate time
        final_time = time.time()
        eta = final_time - initial_time
        print("scrcpy launched in {:.2f}s".format(eta))
        progress = self.progress(progress)

        # ====================================================================
        # 22: Update configuration
        self.config_manager.update_config(self.config)
        self.config_manager.write_file()
        progress = self.progress(progress)

        return self.progress(progress)


def set_scrcpy_server_path(config):
    scrcpy_server_path_env = os.getenv("SCRCPY_SERVER_PATH", None)
    if scrcpy_server_path_env:
        if not os.path.exists(scrcpy_server_path_env):
            server_path = open_exe_name_dialog(None, "scrcpy-server")
            if server_path is None:
                raise ScrcpyServerNotFoundError("User did not select scrcpy server")
            config["scrcpy-server"] = server_path
            os.environ["SCRCPY_SERVER_PATH"] = server_path
    elif (
        (scrcpy_server_path_env is None)
        and (
            (
                isinstance(config.get("scrcpy-server"), str)
                and not os.path.exists(config.get("scrcpy-server"))
            )
            or config.get("scrcpy-server") is None
        )
    ) and (platform.System().system() == "Windows"):
        server_path = open_exe_name_dialog(None, "scrcpy-server")
        if server_path is None:
            raise ScrcpyServerNotFoundError("User did not select scrcpy server")
        config["scrcpy-server"] = server_path
        os.environ["SCRCPY_SERVER_PATH"] = server_path
    elif platform.System().system() == "Windows":
        os.environ["SCRCPY_SERVER_PATH"] = config["scrcpy-server"]
    return config


def bootstrap(
    app: QtWidgets.QApplication,
    config_manager: InterfaceConfig,
    theme: str = "Breeze",
    aot: bool = True,
    debug_no_scrcpy: bool = False,
    hide_wm_frame: bool = True,
):
    """
    Launch the guiscrcpy window
    :return:
    """
    config = config_manager.get_config()

    # load fonts
    font_database = QFontDatabase()
    for font in FONTS:
        s = font_database.addApplicationFont(":/font/fonts/{ttf}".format(ttf=font))
        if s == -1:  # loading the font failed
            # https://doc.qt.io/qt-5/qfontdatabase.html
            print(fc("{y}Failed to load {ttf} font.{rst}", ttf=font))

    # set theme
    app.setStyle(theme)
    # apply stylesheet
    if theme == "Breeze":
        # The Qdarkstylesheet is based on Breeze, lets load them on default
        app.setStyleSheet(dark_stylesheet())

    # load splash
    splash_pix = QPixmap(":/res/ui/guiscrcpy-branding.png")
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # on windows, users are likely not to add the scrcpy-server to the
    # SCRCPY_SERVER_PATH
    config_manager.update_config(set_scrcpy_server_path(config))
    config_manager.write_file()
    adb = AndroidDebugBridge(config_manager.get_config().get("adb"))
    scrcpy = ScrcpyBridge(config_manager.get_config().get("scrcpy"))
    config_manager["adb"] = adb.get_path()
    config_manager["scrcpy"] = scrcpy.get_path()
    guiscrcpy = InterfaceGuiscrcpy(
        config_manager=config_manager,
        adb=adb,
        scrcpy=scrcpy,
        force_window_frame=not hide_wm_frame,
        panels_not_always_on_top=not aot,
        debug_no_scrcpy=debug_no_scrcpy,
    )
    guiscrcpy.show()
    app.processEvents()
    splash.hide()
    app.exec_()

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

import logging
import os

from guiscrcpy.platform.windows_tools.tools import make_shortcut


class Windows:
    def __init__(self):
        self.make_config()

    @staticmethod
    def make_config():
        path = os.path.expanduser(os.path.join(
            "~", "AppData", "Local", "guiscrcpy"))
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                logging.error(
                    "Error creating configuration filename in dir {path}. "
                    "Error code:{e}".format(path=path, e=e)
                )
        return path

    @staticmethod
    def system():
        return 'Windows'

    def cfgpath(self):
        return self.make_config()

    def increment(self):
        pass

    @staticmethod
    def paths():
        return ['bin']

    @staticmethod
    def install_fonts():
        """
        Install fonts to system directory.
        The fonts being installed is Titillium Web ~
        https://fonts.google.com/specimen/Titillium+Web
        Open Source Approved fonts.
        # TODO support for SystemWide Installation
        :return: True if installation successful, else False
        """
        # TODO: Test it properly
        # Likely to fail
        cmd = r"""copy "{fontdir}" "%WINDIR%\Fonts
        reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /
        v "FontName (TrueType)" / t REG_SZ / d {font} / f """

        font_dir = os.path.join(
            os.path.abspath(
                os.path.dirname(os.path.dirname(__file__))
            ),
            'ui',
            'fonts'
        )
        try:
            fonts = os.listdir(font_dir)
            for i in fonts:
                # install the fonts by executing cmd and update the Windows
                # Registry
                print(cmd.format(font=i, fontdir=os.path.join(font_dir, i)))
                os.system(
                    cmd.format(font=i, fontdir=os.path.join(font_dir, i)))
            return True
        except Exception as e:
            print("Installing fonts failed")
            logging.error(
                "Error Installing the fonts. "
                "You might have to manually install the fonts"
                "Titillium Web : "
                "https://fonts.google.com/specimen/Titillium+Web"
                "Error: {}".format(e)
            )
            return False

    @staticmethod
    def create_desktop():
        try:
            make_shortcut()
        except Exception as e:
            # do not stop users from using guiscrcpy
            # in case this small exception happens
            print("Desktop shortcut generation failed: {}".format(e))

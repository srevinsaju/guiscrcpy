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

from guiscrcpy.version import VERSION

desktop = \
    """
[Desktop Entry]
Version={v}
Name=guiscrcpy
GenericName=guiscrcpy
Comment=Open Source Android Screen Mirroring System
Exec=guiscrcpy
Icon={icon_path}
Type=Application
Categories=Utility;Development;
StartupWMClass=UGENE
"""


class Linux:
    def __init__(self):
        pass

    def cfgpath(self):
        return self.make_config()

    @staticmethod
    def make_config():
        if os.getenv('XDG_CONFIG_HOME') is None:
            path = os.path.expanduser("~/.config/guiscrcpy/")
        else:
            path = os.getenv('XDG_CONFIG_HOME').split(":")[0] + "/guiscrcpy"
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as e:
                logging.error(
                    "Error creating configuration filename in dir {path}. "
                    "Error code:{e}"
                    .format(
                        path=path,
                        e=e
                    ))
        return path

    @staticmethod
    def create_desktop(desktop_file=None,
                       desktop_file_name='guiscrcpy.desktop'):
        """
        Create Desktop filename for Linux in ~/.local level
        :return:
        """
        if desktop_file:
            desk = desktop_file
        else:
            desk = desktop.format(
                v=VERSION,
                icon_path=os.path.join(
                    os.path.abspath(
                        os.path.dirname(
                            os.path.dirname(__file__)
                        )
                    ),
                    'ui', 'ui', 'guiscrcpy_logo.png'
                )
            )
        if os.getenv('XDG_DESKTOP_DIR'):
            desktop_dir = os.getenv('XDG_DESKTOP_DIR')
        else:
            if os.path.exists(os.path.expanduser('~/Desktop')):
                desktop_dir = os.path.expanduser('~/Desktop')
            elif os.path.exists(os.path.expanduser('~/desktop')):
                desktop_dir = os.path.expanduser('~/desktop')
            else:
                desktop_dir = False
        if desktop_dir:
            with open(os.path.join(desktop_dir, desktop_file_name),
                      'w') as w:
                w.write(desk)
            return desktop_dir
        else:
            return False

    @staticmethod
    def install_fonts():
        """
        Install fonts to ~/.fonts.
        The fonts being installed is Titillium Web ~
        https://fonts.google.com/specimen/Titillium+Web
        Open Source Approved fonts.
        # TODO support for SystemWide Installation
        :return: True if installation successful, else False
        """
        sys_font_dir = os.path.join(os.path.expanduser('~'), '.fonts')
        if not os.path.exists(sys_font_dir):
            os.makedirs(sys_font_dir)

        try:
            from fontTools.ttLib import TTFont
        except ModuleNotFoundError as e:
            logging.error(
                "Error Installing the fonts. "
                "You might have to manually install the fonts"
                "Titillium Web : "
                "https://fonts.google.com/specimen/Titillium+Web "
                "Error: {}".format(e)
            )
            return False

        font_dir = os.path.join(os.path.abspath(
            os.path.dirname(os.path.dirname(__file__))), 'ui', 'fonts')
        try:
            fonts = os.listdir(font_dir)
            for i in fonts:
                font = TTFont(os.path.join(font_dir, i))
                font.save(os.path.join(sys_font_dir, i))
            return True
        except Exception as e:
            logging.error(
                "Error Installing the fonts. "
                "You might have to manually install the fonts"
                "Titillium Web : "
                "https://fonts.google.com/specimen/Titillium+Web "
                "Error: {}".format(e)
            )
            return False

    @staticmethod
    def system():
        return 'Linux'

    def increment(self):
        pass

    @staticmethod
    def paths():
        return ['bin', '/usr/bin', '~/.local/bin', '~/bin', '/usr/local/bin']

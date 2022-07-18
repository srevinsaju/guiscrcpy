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

import os

# flake8: noqa
has_pyside2 = False
has_pyqt5 = False

try:
    import PySide2

    has_pyside2 = True
except ModuleNotFoundError:
    try:
        import PyQt5

        has_pyqt5 = True
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "Did not find either 'PyQt5' or 'PySide2' installations"
        )

if has_pyside2:
    from guiscrcpy.ui.pyside2.main import Ui_MainWindow  # noqa: F401
    from guiscrcpy.ui.pyside2.network import Ui_NetworkUI  # noqa: F401
    from guiscrcpy.ui.pyside2.panel import Ui_HorizontalPanel  # noqa: F401
    from guiscrcpy.ui.pyside2.settings import Ui_MainWindow as Ui_SettingsWindow
    from guiscrcpy.ui.pyside2.downloader import Ui_Initializer  # noqa: F401
    from guiscrcpy.ui.pyside2.toolkit import Ui_ToolbarPanel  # noqa: F401
elif has_pyqt5:
    from guiscrcpy.ui.pyqt5.main import Ui_MainWindow  # noqa: F401
    from guiscrcpy.ui.pyqt5.network import Ui_NetworkUI  # noqa: F401
    from guiscrcpy.ui.pyqt5.panel import Ui_HorizontalPanel  # noqa: F401
    from guiscrcpy.ui.pyqt5.settings import Ui_MainWindow as Ui_SettingsWindow
    from guiscrcpy.ui.pyqt5.downloader import Ui_Initializer  # noqa: F401
    from guiscrcpy.ui.pyqt5.toolkit import Ui_ToolbarPanel  # noqa: F401

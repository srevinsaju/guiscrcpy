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

__QT_INSTANCE = os.getenv("QT_API", False)

if __QT_INSTANCE and __QT_INSTANCE in ("pyside2", "pyqt5"):
    if __QT_INSTANCE == "pyside2":
        use_pyqt5 = False
    else:
        use_pyqt5 = True
else:
    # either QT_API is not defined or defined for an older version of PyQt5
    # just use PyQt5 as default
    use_pyqt5 = True

if use_pyqt5:
    from guiscrcpy.ui.pyqt5.main import Ui_MainWindow  # noqa: F401
    from guiscrcpy.ui.pyqt5.network import Ui_NetworkUI  # noqa: F401
    from guiscrcpy.ui.pyqt5.panel import Ui_HorizontalPanel  # noqa: F401
    from guiscrcpy.ui.pyqt5.settings import Ui_MainWindow as Ui_SettingsWindow
    from guiscrcpy.ui.pyqt5.downloader import Ui_Initializer  # noqa: F401
    from guiscrcpy.ui.pyqt5.toolkit import Ui_ToolbarPanel  # noqa: F401
else:
    from guiscrcpy.ui.pyside2.main import Ui_MainWindow  # noqa: F401
    from guiscrcpy.ui.pyside2.network import Ui_NetworkUI  # noqa: F401
    from guiscrcpy.ui.pyside2.panel import Ui_HorizontalPanel  # noqa: F401
    from guiscrcpy.ui.pyside2.settings import Ui_MainWindow as Ui_SettingsWindow
    from guiscrcpy.ui.pyside2.downloader import Ui_Initializer  # noqa: F401
    from guiscrcpy.ui.pyside2.toolkit import Ui_ToolbarPanel  # noqa: F401

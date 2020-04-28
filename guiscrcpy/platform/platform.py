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
import platform

if platform.system() == 'Windows':
    # Windows OS > 7
    from guiscrcpy.platform.windows import Windows as System
elif platform.system() == "Linux":
    # GNU/Linux OS
    from guiscrcpy.platform.linux import Linux as System
elif platform.system() == "Darwin":
    # MacOS
    from guiscrcpy.platform.darwin import Darwin as System
else:
    logging.warning("Attempting to run guiscrcpy on utested OS")
    from guiscrcpy.platform.linux import Linux as System
# Other OSes should benefit from Linux config

System()

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

from subprocess import PIPE

from ..lib.utils import shellify as _, open_process


def get(ls, idx, default=""):
    try:
        return ls[idx]
    except IndexError:
        return default


def _get_dimension_raw_noexcept(path, device_id=None):
    if device_id:
        shell_adb = open_process(
            _("{} -s {} shell wm size".format(path, device_id)),
            stdout=PIPE,
            stderr=PIPE,
        )
    else:
        shell_adb = open_process(
            _("{} shell wm size".format(path)), stdout=PIPE, stderr=PIPE
        )
    return shell_adb

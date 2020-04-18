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

from guiscrcpy.theme.termcolor import termcolors


class header:
    def __init__(self, commit):
        print(
            termcolors.UNDERLINE +
            "                                  " +
            termcolors.ENDC)
        print()
        print("guiscrcpy")
        print("by srevinsaju")
        print(termcolors.OKBLUE + commit + termcolors.ENDC)
        print(
            termcolors.OKBLUE +
            "Licensed under GNU GPL v3 (c) 2020  " +
            termcolors.ENDC)
        print(
            termcolors.UNDERLINE +
            "                                  " +
            termcolors.ENDC)
        print(termcolors.OKBLUE + "" + termcolors.ENDC)

        print()
        print(
            "MSG: Please ensure you have enabled",
            termcolors.OKGREEN + "USB Debugging" + termcolors.ENDC,
            "on your device. See README.md for more details",
        )

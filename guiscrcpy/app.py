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

#!/usr/bin/env python3

import os
import sys
import subprocess
import platform


def check_snap():
    if platform.platform() == "Linux":

        """Check if inside a snap"""

        if 'SNAP_COMMON' in os.environ:
            print('running in a snap')
            return True
        return False
    else:
        return False


def add_path():
    """Add home dir to path for accessing tools from a snap"""

    toolspath = os.environ['SNAP_COMMON']
    #toolspath = os.path.join(home, 'tools')
    binpath = os.path.join(toolspath, 'bin')
    # if not os.path.exists(toolspath):
    print('you should install external tools in %s' % toolspath)
    os.environ["PATH"] += os.pathsep + binpath
    print(os.environ["PATH"])
    return


def run_test():
    print(__file__)
    if(platform.platform() == "Windows"):
        print("DETECTED OS :: WINDOWS")
        pythonexec = "python"
    else:
        print("DETECTED OS :: *NIX")
        pythonexec = "python3"

    filename = str(__file__)[:-(len("app.py"))]
    os.chdir(str(os.path.abspath(__file__)[:-len("app.py")]))
    cmd = pythonexec + ' __main__.py'
    tmp = subprocess.Popen(cmd, shell=True)

    return


def main():
    "Run the application"

    if check_snap() is True:
        add_path()
    print('Hello!')
    run_test()


if __name__ == '__main__':
    main()

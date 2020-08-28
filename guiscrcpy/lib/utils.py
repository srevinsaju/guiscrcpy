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
import shlex
import shutil
import sys

from colorama import Fore

from guiscrcpy.platform.platform import System

environment = System()

COLORS = {
    'g': Fore.GREEN,
    'rst': Fore.RESET,
    'y': Fore.YELLOW,
    'r': Fore.RED,
    'b': Fore.BLUE,
    'B': Fore.LIGHTBLUE_EX,
    'x': Fore.LIGHTBLACK_EX
}


def log(*args, **kwargs):
    if os.getenv('GUISCRCPY_DEBUG', False):
        print(*args, **kwargs)
    else:
        logging.debug(str(args))


def shellify(args):
    if environment.system() == 'Windows':
        return args
    else:
        return shlex.split(args)


_ = shellify


def decode_process(process):
    try:
        output = process.stdout.readlines()
        for i in range(len(output)):
            output[i] = output[i].decode('utf-8')
    except NameError:
        logging.error("No stdout in process.")
        output = ""
    return output


def check_existence(paths, filename="", directory=True, path=False):
    for i in paths:
        j = os.path.expanduser(i)
        if os.path.exists(j):  # directory exists
            if directory and os.path.isdir(j):
                return [j]
            else:
                if environment.system() == 'Windows':
                    append = '.exe'
                else:
                    append = ''

                if (isinstance(filename, list)) or \
                        (isinstance(filename, tuple)):
                    for exe in filename:
                        if os.path.exists(os.path.join(j, exe + append)):
                            return [os.path.join(j, exe + append)]
                else:

                    if os.path.exists(os.path.join(j, filename + append)):
                        return [os.path.join(j, filename + append)]
        else:
            logging.debug("{} doesn't exist".format(i))

    if path:
        new_paths = os.getenv('PATH').split(os.pathsep)
        found_path = check_existence(
            new_paths, filename=filename, directory=directory, path=False)
        if found_path:
            return found_path + ['path']
        else:
            return False
    else:
        return False


def get_self():
    """
    Returns the path to the running executable depending on the conditions
    :return:
    :rtype:
    """
    if os.getenv('APPIMAGE'):
        # Running from AppImage
        return os.getenv('APPIMAGE')
    elif getattr(sys, 'frozen', False):
        # running in precompiled bundle
        return sys.executable
    elif shutil.which('guiscrcpy'):
        # guiscrcpy is added to PATH
        return shutil.which('guiscrcpy')
    elif any([os.path.exists(os.path.join(x, 'guiscrcpy'))
              for x in sys.path]) and \
            any([sys.executable.endswith(py) for py in
                 ['python', 'python3']]):
        # guiscrcpy is installed as a pip package, but not added to PATH
        return '{py} -m guiscrcpy'.format(py=sys.executable)
    elif os.getenv('SNAP'):
        # running from SNAP
        return '/snap/bin/guiscrcpy'
    raise RuntimeError("Could not detect if guiscrcpy was run from "
                       "snap, appimage or python wheel")


def format_colors(string, **kwargs):
    return string.format(**kwargs, **COLORS)

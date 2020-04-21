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

"""

import os
import sys
from setuptools import setup
import platform

requirements = ['PyQt5==5.14.2', 'pynput']
if platform.system() == 'Windows':
    requirements.extend(['pywin32', 'psutil'])
elif platform.system() == 'Linux':
    requirements.extend(['fonttools', 'psutil'])

data_files = [
        ('share/applications', ['guiscrcpy.desktop'] )
    ]



setup(
    name='guiscrcpy',
    version='3.4.post78.dev',
    description='An Open Source - Fast - Android Screen Mirroring system.',
    long_description="""<img src=https://github.com/srevinsaju/guiscrcpy/blob/master/guiscrcpy/ui/ui/guiscrcpy_logo.png width=25%>

# guiscrcpy

![Linux](https://github.com/srevinsaju/guiscrcpy/workflows/Linux/badge.svg)
![Windows](https://github.com/srevinsaju/guiscrcpy/workflows/Windows/badge.svg)
![Mac OS](https://github.com/srevinsaju/guiscrcpy/workflows/Mac%20OS/badge.svg)
[![Updates](https://pyup.io/repos/github/srevinsaju/guiscrcpy/shield.svg)](https://pyup.io/repos/github/srevinsaju/guiscrcpy/)
[![Python 3](https://pyup.io/repos/github/srevinsaju/guiscrcpy/python-3-shield.svg)](https://pyup.io/repos/github/srevinsaju/guiscrcpy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/guiscrcpy?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/guiscrcpy?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/guiscrcpy?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/guiscrcpy?color=dark%20green&logo=PYPI&logoColor=Green&style=flat-square)](https://pypi.org/project/guiscrcpy)
[![AUR version](https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square)](https://aur.archlinux.org/packages/guiscrcpy)
[![Snap Status](https://build.snapcraft.io/badge/srevinsaju/guiscrcpy.svg)](https://build.snapcraft.io/user/srevinsaju/guiscrcpy)
[![GitHub All Releases](https://img.shields.io/github/downloads/srevinsaju/guiscrcpy/total?style=flat-square)](https://github.com/srevinsaju/guiscrcpy/releases)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Twitter Follow](https://img.shields.io/twitter/follow/srevinsaju?style=social)](https://twitter.com/srevinsaju)
[![GitHub followers](https://img.shields.io/github/followers/srevinsaju?label=srevin%20Saju&style=social)](https://github.com/srevinsaju)

> **IMPORTANT** : `guiscrcpy` is a free and open source android screen mirroring system. The work on guiscrcpy is driven by 
the interest of users into it. Please feel free to let you know your thanks if this software helped you a lot, or if you like 
some more features to be included, and paticularly ...

[![Become a Patron](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/srevinsaju?fan_landing=true)

For beta Windows compiled executables, click 
[![Windows Executable](https://github.com/srevinsaju/guiscrcpy/workflows/Windows%20Executable/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions?query=+event%3Apush++is%3Asuccess+branch%3Amaster+workflow%3A%22Windows+Executable%22). Select the latest commit 
and download the artifact.

For beta Linux compiled AppImages, click
[![AppImage](https://github.com/srevinsaju/guiscrcpy/workflows/AppImage/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions?query=event%3Apush+branch%3Amaster+is%3Asuccess+workflow%3AAppImage+)
and download the artifact. :tada: Thanks to @niess, guiscrcpy appimages are distributed for public use!!

![image of guiscrcpy](https://raw.githubusercontent.com/srevinsaju/guiscrcpy-docs/master/docs/screen3.png)

guiscrcpy is a multiplatform, ready-to-use GUI layer for Android to PC screen mirroring written in the advancing programming language python3 for the most award winning open-source android screen mirroring system -- `scrcpy` located on `https://github.com/genymobile/scrcpy/` by [@rom1v](https://github.com/rom1v)

## Installation
To install `guiscrcpy`, just type:
```bash
python3 -m pip install guiscrcpy
```
in your terminal

Alternatively, download the compiled EXE from the releases for Windows Operating Systems and 
AppImages for Linux OSes

For more details on Installation instructions, head over to the Wiki

## Documentation
All detailed information are clearly laid out in the Wiki. you might need to check that out
""",
    long_description_content_type='text/markdown',
    license='GPL v3',
    author='srevinsaju',
    author_email="srevin03@gmail.com",
    packages=['guiscrcpy'],
    data_files = data_files,
    url="https://srevinsaju.github.io/guiscrcpy",
    download_url="https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    package_data={'guiscrcpy': ['*', '*.*', 'resources/*', 'ui/*', 'lib/*', 'platform/*', 'theme/*', 'ux/*', 'network/*', 'settings/*', 'install/*', 'platform/windows_tools/*', 'ui/icons/*', 'ui/fonts/*', 'ui/rsrc/*', 'ui/ui/*']},
    include_package_data=True,
    install_requires=requirements,
    scripts=["scripts/guiscrcpy", "scripts/guiscrcpy-mapper"],
    entry_points={'console_scripts': ['guiscrcpy = guiscrcpy.launcher:bootstrap']},
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.8',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)


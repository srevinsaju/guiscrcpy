<img src=https://github.com/srevinsaju/guiscrcpy/blob/master/guiscrcpy/ui/ui/guiscrcpy_logo.png width=25%>

# guiscrcpy

![Linux](https://github.com/srevinsaju/guiscrcpy/workflows/Linux/badge.svg)
![Windows](https://github.com/srevinsaju/guiscrcpy/workflows/Windows/badge.svg)
![Mac OS](https://github.com/srevinsaju/guiscrcpy/workflows/Mac%20OS/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/59c0214b5f2140e0be7af62f14ebdc42)](https://www.codacy.com/manual/srevinsaju/guiscrcpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=srevinsaju/guiscrcpy&amp;utm_campaign=Badge_Grade)
[![Updates](https://pyup.io/repos/github/srevinsaju/guiscrcpy/shield.svg)](https://pyup.io/repos/github/srevinsaju/guiscrcpy/)
[![Python 3](https://pyup.io/repos/github/srevinsaju/guiscrcpy/python-3-shield.svg)](https://pyup.io/repos/github/srevinsaju/guiscrcpy/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/guiscrcpy?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/guiscrcpy?style=flat-square)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/guiscrcpy?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/guiscrcpy?color=dark%20green&logo=PYPI&logoColor=Green&style=flat-square)](https://pypi.org/project/guiscrcpy)
[![AUR version](https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square)](https://aur.archlinux.org/packages/guiscrcpy)
[![guiscrcpy](https://snapcraft.io//guiscrcpy/badge.svg)](https://snapcraft.io/guiscrcpy)
[![GitHub All Releases](https://img.shields.io/github/downloads/srevinsaju/guiscrcpy/total?style=flat-square)](https://github.com/srevinsaju/guiscrcpy/releases)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Twitter Follow](https://img.shields.io/twitter/follow/srevinsaju?style=social)](https://twitter.com/srevinsaju)
[![GitHub followers](https://img.shields.io/github/followers/srevinsaju?label=srevin%20Saju&style=social)](https://github.com/srevinsaju)

> **IMPORTANT** : `guiscrcpy` is a free and open source android screen mirroring system. The work on guiscrcpy is driven by 
the interest of users into it. Please feel free to let you know your thanks if this software helped you a lot, or if you like 
some more features to be included, and paticularly ...

[![Become a Patron](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/srevinsaju?fan_landing=true)



![image of guiscrcpy](https://raw.githubusercontent.com/srevinsaju/guiscrcpy-docs/master/docs/screen3.png)

guiscrcpy is a multiplatform, ready-to-use GUI layer for Android to PC screen mirroring written in the advancing programming language python3 for the most award winning open-source android screen mirroring system -- `scrcpy` located on `https://github.com/genymobile/scrcpy/` by [@rom1v](https://github.com/rom1v)

<br>

## Installation

These are the common methods of installation. To see more interesting ways, checkout [Installation wiki](docs/INSTALL.md) page for more information, and to find a compatible installtion method for your device and device architecture

| Package Type  | Platforms                                                    | Status                                                       | Command / Link                |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------- |
| PyPI (`pip`)  | <img src="https://guiscrcpy.github.io/img/linux.png" height=15px><img src="https://guiscrcpy.github.io/img/windows.png" height=15px><img src="https://guiscrcpy.github.io/img/darwin.jpeg" height=15px style="border-radius: 50%"> | ![Linux](https://github.com/srevinsaju/guiscrcpy/workflows/Linux/badge.svg) | `pip3 install -U guiscrcpy`   |
| Snap Store    | <img src="https://guiscrcpy.github.io/img/linux.png" height=15px><img src="https://guiscrcpy.github.io/img/darwin.jpeg" height=15px style="border-radius: 50%"> | [![guiscrcpy](https://snapcraft.io//guiscrcpy/badge.svg)](https://snapcraft.io/guiscrcpy) | `sudo snap install guiscrcpy` |
| AUR*          | <img src="https://raw.githubusercontent.com/guiscrcpy/guiscrcpy.github.io/master/img/archlinux.png" height=15px> | [![AUR version](https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square)](https://aur.archlinux.org/packages/guiscrcpy) | `yay -S guiscrcpy`            |
| Windows (exe) | <img src="https://guiscrcpy.github.io/img/windows.png" height=15px> | [![Windows Executable](https://github.com/srevinsaju/guiscrcpy/workflows/Windows%20Executable/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions?query=+event%3Apush++is%3Asuccess+branch%3Amaster+workflow%3A%22Windows+Executable%22) | `Click on the Status Badge`   |
| AppImage      | <img src="https://guiscrcpy.github.io/img/linux.png" height=15px> | [![AppImage](https://github.com/srevinsaju/guiscrcpy/workflows/AppImage/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions?query=event%3Apush+branch%3Amaster+is%3Asuccess+workflow%3AAppImage+) | `Click on the Status Badge`   |

<br>

## Table of Contents

1. [Installation](docs/INSTALL.md) (detailed)
2. [Features](#Features)
3. [Configuration files](docs/CONFIGURATION.md)
4. [FAQ](docs/FAQ.md)

<br>

## Features

#### Customized settings for [`scrcpy`](https://github.com/Genymobile/scrcpy)

`scrcpy` is a android screen mirroring command line interface tool. It does not save your configuration for your each run. Moreover, it requires some command line knowledge of how to use scrcpy and some developer background. There are already many unnecessary issues on `scrcpy`‘s repository, which is caused due to the complexity at which scrcpy’s options are handled. `guiscrcpy` makes use of this complexity and converts into a simple graphical user interface which creates `scrcpy ` 

#### Desktop launcher

`scrcpy` is a command line interface, which seems quite non intuitive for users who do not use command line / non-developers. `guiscrcpy` creates a one click desktop shortcut, which enables users to start `guiscrcpy` by clicking on their desktop shortcut

#### Toolkits and Panels

`guiscrcpy` bundles side panels, bottom panels and an additional unique swipe panel, which does not exist in other screen mirroring clients. 

##### Swipe Panel (`guiscrcpy.ux.swipe.SwipeUX`)

To be filled in later :jack_o_lantern:




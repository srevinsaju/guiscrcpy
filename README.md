<img src=https://raw.githubusercontent.com/srevinsaju/guiscrcpy/master/guiscrcpy/ui/ui/guiscrcpy_logo.png width=25%>

# guiscrcpy

[![Financial Contributors on Open Collective](https://opencollective.com/guiscrcpy/all/badge.svg?label=financial+contributors)](https://opencollective.com/guiscrcpy) ![Linux](https://github.com/srevinsaju/guiscrcpy/workflows/Linux/badge.svg)![Windows](https://github.com/srevinsaju/guiscrcpy/workflows/Windows/badge.svg)![Mac OS](https://github.com/srevinsaju/guiscrcpy/workflows/Mac%20OS/badge.svg)

[![Updates](https://pyup.io/repos/github/srevinsaju/guiscrcpy/shield.svg)](https://pyup.io/repos/github/srevinsaju/guiscrcpy/)[![Python 3](https://pyup.io/repos/github/srevinsaju/guiscrcpy/python-3-shield.svg)](https://pyup.io/repos/github/srevinsaju/guiscrcpy/)[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/guiscrcpy?style=flat-square)![PyPI](https://img.shields.io/pypi/v/guiscrcpy?style=flat-square)![PyPI - Wheel](https://img.shields.io/pypi/wheel/guiscrcpy?style=flat-square)![PyPI - Downloads](https://img.shields.io/pypi/dm/guiscrcpy?color=dark%20green&logo=PYPI&logoColor=Green&style=flat-square)](https://pypi.org/project/guiscrcpy)

[![Get guiscrcpy AppImage](https://img.shields.io/endpoint?url=https%3A%2F%2Fwww.srevinsaju.me%2Fget-appimage%2Fguiscrcpy%2Fshields.json)](https://www.srevinsaju.me/get-appimage/guiscrcpy/)

[![AUR version](https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square)](https://aur.archlinux.org/packages/guiscrcpy)
[![guiscrcpy](https://snapcraft.io//guiscrcpy/badge.svg)](https://snapcraft.io/guiscrcpy)
[![GitHub All Releases](https://img.shields.io/github/downloads/srevinsaju/guiscrcpy/total?style=flat-square)](https://github.com/srevinsaju/guiscrcpy/releases)
[![Discord](https://img.shields.io/discord/679746670422261783?label=chat%20on%20Discord&logo=discord&logoColor=white&style=flat-square)](https://discord.gg/mFqj3a5)
[![Discord Server](https://badgen.net/badge/discord/join%20chat/7289DA?icon=discord)](https://discord.gg/mFqj3a5)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

----------

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/srevinsaju/guiscrcpy?color=red&label=pre-release&logo=github&sort=semver&style=flat-square) ![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/srevinsaju/guiscrcpy/latest?color=green&sort=semver&style=flat-square)[![Codacy Badge](https://api.codacy.com/project/badge/Grade/59c0214b5f2140e0be7af62f14ebdc42)](https://www.codacy.com/manual/srevinsaju/guiscrcpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=srevinsaju/guiscrcpy&amp;utm_campaign=Badge_Grade)

------------

[![Twitter Follow](https://img.shields.io/twitter/follow/srevinsaju?style=social)](https://twitter.com/srevinsaju)

[![GitHub followers](https://img.shields.io/github/followers/srevinsaju?label=srevin%20Saju&style=social)](https://github.com/srevinsaju)

[![Become a Patron](docs/img/guiscrcpy_branding.png)](https://www.patreon.com/srevinsaju?fan_landing=true)

![image of guiscrcpy](screen39.jpg)

![Live example of guiscrcpy](https://raw.githubusercontent.com/guiscrcpy/guiscrcpy.github.io/master/img/guiscrcpy.gif)

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
2. [Features](docs/FEATURES.md)
3. [Configuration files](docs/CONFIGURATION.md)
4. [FAQ](docs/FAQ.md)

<br>

## Further reading

Thanks to users around the world, 
guiscrcpy is one of the trending apps this month. 
You may like to see some articles written by well wishers:

* [Mirror your Android screen on your computer with Guiscrcpy - opensource.com](https://opensource.com/article/19/9/mirror-android-screen-guiscrcpy)
* [Helper GUI For scrcpy, The Android Desktop Display And Remote Control Tool - linuxuprising.com](https://www.linuxuprising.com/2019/09/helper-gui-for-scrcpy-android-desktop.html)
* [Mirror your Android display screen in your laptop with Guiscrcpy - breakingexpress.com](https://breakingexpress.com/2019/09/26/mirror-your-android-display-screen-in-your-laptop-with-guiscrcpy/)
* [guiscrcpy demonstration (windows) - Youtube](https://www.youtube.com/watch?v=Uc1ozt4AtrY)
* [guiscrcpy = OpenCollective](https://opencollective.com/guiscrcpy)


## Acknowledgements

Special thanks to [Jetbrains](https://www.jetbrains.com/?from=guiscrcpy) for sponsoring `guiscrcpy` with
a professional PyCharm IDE; It works fantastic!!3

[![jetbrains](docs/img/jetbrains.svg)](https://www.jetbrains.com/?from=guiscrcpy)

## Contributors

### Code Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].
<a href="https://github.com/srevinsaju/guiscrcpy/graphs/contributors"><img src="https://opencollective.com/guiscrcpy/contributors.svg?width=890&button=false" /></a>

### Financial Contributors

Become a financial contributor and help us sustain our community. [[Contribute](https://opencollective.com/guiscrcpy/contribute)]

#### Individuals

<a href="https://opencollective.com/guiscrcpy"><img src="https://opencollective.com/guiscrcpy/individuals.svg?width=890"></a>

#### Organizations

Support this project with your organization. Your logo will show up here with a link to your website. [[Contribute](https://opencollective.com/guiscrcpy/contribute)]

<a href="https://opencollective.com/guiscrcpy/organization/0/website"><img src="https://opencollective.com/guiscrcpy/organization/0/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/1/website"><img src="https://opencollective.com/guiscrcpy/organization/1/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/2/website"><img src="https://opencollective.com/guiscrcpy/organization/2/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/3/website"><img src="https://opencollective.com/guiscrcpy/organization/3/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/4/website"><img src="https://opencollective.com/guiscrcpy/organization/4/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/5/website"><img src="https://opencollective.com/guiscrcpy/organization/5/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/6/website"><img src="https://opencollective.com/guiscrcpy/organization/6/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/7/website"><img src="https://opencollective.com/guiscrcpy/organization/7/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/8/website"><img src="https://opencollective.com/guiscrcpy/organization/8/avatar.svg"></a>
<a href="https://opencollective.com/guiscrcpy/organization/9/website"><img src="https://opencollective.com/guiscrcpy/organization/9/avatar.svg"></a>

## License

```
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


Icon made by Dave Gandy from www.flaticon.com used under
Creative Commons 3.0 Unported. The original SVG black work
by Dave Gandy has been re-oriented, flipped or color-changed.
The rest of Terms and Conditions put forward by
CC-3.0:Unported has been feverently followed by the developer.
Icons have been adapted in all the three windows.

Icons pack obtained from www.flaticon.com
All rights reserved.

```

---------------------

Copyright &copy; [Srevin Saju](https://github.com/srevinsaju) 2019 - 2020


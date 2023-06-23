<p align="center">
    <img src="https://raw.githubusercontent.com/srevinsaju/guiscrcpy/master/guiscrcpy/ui/ui/guiscrcpy_logo.png" alt="guiscrcpy logo" width=128 height=128>

<h2 align="center">📱 guiscrcpy</h2>

  <p align="center">
    A simple, pluggable, graphical user interface for the fastest Android screen mirroring software, <a href="https://github.com/Genymobile/scrcpy">scrcpy</a>
    <br>
    <a href="https://github.com/srevinsaju/guiscrcpy/issues/new">Report bug</a>
    ·
    <a href="https://github.com/srevinsaju/guiscrcpy/issues/new">Request feature</a>
  </p>
</p>

<div align="center">



[![Financial Contributors on Open Collective](https://opencollective.com/guiscrcpy/all/badge.svg?label=financial+contributors)](https://opencollective.com/guiscrcpy) ![Linux](https://github.com/srevinsaju/guiscrcpy/workflows/Linux/badge.svg)![Windows](https://github.com/srevinsaju/guiscrcpy/workflows/Windows/badge.svg)![Mac OS](https://github.com/srevinsaju/guiscrcpy/workflows/Mac%20OS/badge.svg) 
[![Get guiscrcpy AppImage](https://img.shields.io/endpoint?url=https%3A%2F%2Fg.srev.in%2Fget-appimage%2Fguiscrcpy%2Fshields.json)](https://g.srev.in/get-appimage/guiscrcpy/) 
[![AUR version](https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square)](https://aur.archlinux.org/packages/guiscrcpy)
[![guiscrcpy](https://snapcraft.io//guiscrcpy/badge.svg)](https://snapcraft.io/guiscrcpy)
[![GitHub All Releases](https://img.shields.io/github/downloads/srevinsaju/guiscrcpy/total?style=flat-square)](https://github.com/srevinsaju/guiscrcpy/releases)
[![Matrix Chat](https://img.shields.io/badge/chat-%5Bmatrix%5D-green)](https://matrix.to/#/#guiscrcpy:matrix.org) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
[![GitHub followers](https://img.shields.io/github/followers/srevinsaju?label=Follow%20me&style=social)](https://github.com/srevinsaju) [![GitHub stars](https://img.shields.io/github/stars/srevinsaju/guiscrcpy?style=social)](https://github.com/srevinsaju/guiscrcpy/stargazers) 
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/srevinsaju/guiscrcpy?color=red&label=pre-release&logo=github&sort=semver&style=flat-square) ![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/srevinsaju/guiscrcpy/latest?color=green&sort=semver&style=flat-square) 
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/dacb6698a7d5410790e088235018f332)](https://www.codacy.com/gh/srevinsaju/guiscrcpy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=srevinsaju/guiscrcpy&amp;utm_campaign=Badge_Grade) [![Maintainability](https://api.codeclimate.com/v1/badges/c8db380280c4fce44e8b/maintainability)](https://codeclimate.com/github/srevinsaju/guiscrcpy/maintainability)


![image of guiscrcpy](docs/img/screenshot.jpg)
</div>

----------


------------


![Live example of guiscrcpy](https://raw.githubusercontent.com/guiscrcpy/guiscrcpy.github.io/master/img/guiscrcpy.gif)

guiscrcpy is a multiplatform, ready-to-use GUI layer for Android to PC screen mirroring written in the advancing programming language python3 for the most award winning open-source android screen mirroring system -- `scrcpy` located on `https://github.com/genymobile/scrcpy/` by [@rom1v](https://github.com/rom1v)

<br>

## Installation

These are the common methods of installation. To see more interesting ways, checkout [Installation wiki](docs/INSTALL.md) page for more information, and to find a compatible installation method for your device and device architecture

>NOTE: Out of the two links for downloading AppImage, the `.m` one does not include the scrcpy binary. The one with `.r` includes the scrcpy binary. See https://github.com/srevinsaju/guiscrcpy/discussions/341 for more information on the release builds.


| Package Type  | Platforms                                                    | Status                                                       | Command / Link                |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------- |
| Flatpak       | <img src="https://guiscrcpy.github.io/img/linux.png" height=15px> | [![guiscrcpy](https://img.shields.io/badge/flatpak-in.srev.guiscrcpy-green)](https://flathub.org/apps/details/in.srev.guiscrcpy) | `flatpak install flathub in.srev.guiscrcpy` |
| Snap Store    | <img src="https://guiscrcpy.github.io/img/linux.png" height=15px><img src="https://guiscrcpy.github.io/img/darwin.jpeg" height=15px style="border-radius: 50%"> | [![guiscrcpy](https://snapcraft.io//guiscrcpy/badge.svg)](https://snapcraft.io/guiscrcpy) | `sudo snap install guiscrcpy` |
| AUR*          | <img src="https://raw.githubusercontent.com/guiscrcpy/guiscrcpy.github.io/master/img/archlinux.png" height=15px> | [![AUR version](https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square)](https://aur.archlinux.org/packages/guiscrcpy) | `yay -S guiscrcpy`            |
| Windows (exe) | <img src="https://guiscrcpy.github.io/img/windows.png" height=15px> | [![Continuous](https://github.com/srevinsaju/guiscrcpy/actions/workflows/continuous.yml/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions/workflows/continuous.yml) | [Download `.exe`](https://github.com/srevinsaju/guiscrcpy/releases/tag/v2023.1.1)   |
| AppImage      | <img src="https://guiscrcpy.github.io/img/linux.png" height=15px> | [![Continuous](https://github.com/srevinsaju/guiscrcpy/actions/workflows/continuous.yml/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions/workflows/continuous.yml) | [Download `.AppImage`](https://github.com/srevinsaju/guiscrcpy/releases/tag/v2023.1.1) |

<br>

## Table of Contents

1. [Installation](docs/INSTALL.md) (detailed)
2. [Features](docs/FEATURES.md)
3. [Configuration files](docs/CONFIGURATION.md)
4. [FAQ](docs/FAQ.md)

<br>

## Further reading

Thanks to users around the world, 
you may like to see some articles written by well wishers:

* [Mirror your Android screen on your computer with Guiscrcpy - opensource.com](https://opensource.com/article/19/9/mirror-android-screen-guiscrcpy)
* [Helper GUI For scrcpy, The Android Desktop Display And Remote Control Tool - linuxuprising.com](https://www.linuxuprising.com/2019/09/helper-gui-for-scrcpy-android-desktop.html)
* [Mirror your Android display screen in your laptop with Guiscrcpy - breakingexpress.com](https://breakingexpress.com/2019/09/26/mirror-your-android-display-screen-in-your-laptop-with-guiscrcpy/)
* [guiscrcpy demonstration (windows) - Youtube](https://www.youtube.com/watch?v=Uc1ozt4AtrY)
* [guiscrcpy = OpenCollective](https://opencollective.com/guiscrcpy)


## Acknowledgements

Special thanks to [Jetbrains](https://www.jetbrains.com/?from=guiscrcpy) for sponsoring `guiscrcpy` with
a professional PyCharm IDE; It works fantastic!

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

Icons pack obtained from www.flaticon.com
All rights reserved.

```

---------------------

Copyright &copy; 2019 - 2023 [Srevin Saju](https://github.com/srevinsaju) and `guiscrcpy` contributors.


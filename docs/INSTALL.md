# Installation

## PyPI wheels ![PyPI](https://img.shields.io/pypi/v/guiscrcpy?color=green&logo=python&logoColor=white)

Installing from [PyPi](https://pypi.org/project/guiscrcpy/) is the most supported, fastest and compatible package across all platforms and operating systems. The list of compatible and tested platforms are:

* Windows 8, 8.1, 10 (64-bit)
* `manylinux2014` 
* macOS Catalina 10.15

The restriction of `manylinux2014` are because of the wheels for `PyQt5` are mostly `manylinux2014`. The `PyQt5==5.14` gives `manylinux1` wheels also. It can be preferably downgraded on respective linux distributions for compatibility. The minimum required version of `PyQt5` required to run `guiscrcpy` is `5.14`, if not used, it might create user specific errors like `AttributeErrors` while parsing the User Interface files.

### Installation

##### Stable Release

```bash
pip3 install -U guiscrcpy
```

##### Development Release

```bash
pip3 install https://github.com/srevinsaju/guiscrcpy/archive/master.zip
```

> **NOTE**: Development (`master` / `beta-*`) are expected to be highly unstable. If you would like to contribute to development by reporting issues before the next release, you consider using the above option.

Few points to consider:

* `pip` install might not work if you do not have `pip` installed on you system. On Windows, if the downloaded version of `python` is from the [python.org](https://python.org), it should not be an issue. However, if you install `python` from another source, (eg: Ubuntu `apt` repositories, or Alpine Python docker images), you would have to install pip. Check out [this](https://google.com/search?q=How+to+install+pip) for more information.

* If your `pip` version is below 20.0, then you are likely to expect a failure in the command with an `EnvironmentError` / `PermissionDenied` Error. This is because `pip` tries to install packages to global level, (aka `/usr/` on Linux). To fix that, you may either [upgrade pip](https://google.com/search?q=How+to+upgrade+pip) or use the `--user` flag as such:

  ```bash
  pip3 install guiscrcpy --user
  ```

* `guiscrcpy` requires Python `v3.6` or above. Installing on an older version of python is likely to fail. Python 2 is not supported in any previous releases also. Support for Python 3.5 can be attained by manual patching the `f-strings` and patching the requirements with an apt version of `PyQt5`.


<br>

## AppImages ![AppImage](https://github.com/srevinsaju/guiscrcpy/workflows/AppImage/badge.svg) [![Get guiscrcpy AppImage](https://img.shields.io/endpoint?url=https%3A%2F%2Fg.srev.in%2Fget-appimage%2Fguiscrcpy%2Fshields.json)](https://g.srev.in/get-appimage/guiscrcpy/)

AppImages are distributed on the AppImage catalog and on the releases page. To get seamless updates and desktop integration, install the AppImage
with [Zap AppImage Package Manager](https://github.com/srevinsaju/zap), and then just run

```bash
zap install guiscrcpy
``` 
and you are done!

If you already installed an older version of guiscrcpy 
using `zap`, then it would be easier to download only the 
changed parts, (or delta) of the binary. Just do

```bash
zap update guiscrcpy
```

Alternatively, the longer method : 

Download the AppImage either from the releases, or from by clicking the `Status` badge and then download the AppImage artifact for the latest commit.

**AppImages** are built on `manylinux2014` base image. Older linux might / might not support it. A possible test for it, might be to check if you can install the `wheel` of `PyQt5>=5.14`. 

AppImages are more supported than snaps. Snaps are containerised. So it is likely that guiscrcpy might not work as a snap.

```bash
wget https://github.com/srevinsaju/guiscrcpy/releases/v4.11.0/download/guiscrcpy-*.AppImage
chmod +x guiscrcpy-*.AppImage

# one time execution
./guiscrcpy-*.AppImage

# for systems without FUSE support
guiscrcpy-x86_64.AppImage --appimage-extract-and-run
```

> NOTE: The AppImage includes `scrcpy` pre-built binary along 
along with adb. This implies you do not need to have anything 
additionally installed other than to download this AppImage. 

For some linux desktops, it would be needed to install 
`libva-drm2` or `libva` to enable scrcpy's new video acceleration
feature using OpenGL.

On ubuntu, if you have enabled `universe` repositories, you can just
Ubuntu:
```bash
sudo apt install libva-drm2
```

The bug was found on ubuntu. Tested on Ubuntu 20.10, 20.04 (GNOME). Most linux distros (not live CDs) have these installed on them by default. I do not mind bundling this lib too, but it might break other linux'es. So feel free to pop into `guiscrcpy` 's Discord channel or open a GitHub issue, if you need some help.


[![Get Appimage](https://raw.githubusercontent.com/srevinsaju/get-appimage/master/static/badges/get-appimage-branding-blue.png)](https://srevinsaju.github.io/get-appimage/guiscrcpy)

<br>

## Snap Store [![guiscrcpy](https://snapcraft.io//guiscrcpy/badge.svg)](https://snapcraft.io/guiscrcpy) [![guiscrcpy](https://snapcraft.io//guiscrcpy/trending.svg?name=0)](https://snapcraft.io/guiscrcpy)

The guiscrcpy [snap](https://snapcraft.io) is a recent implementation of making `guiscrcpy` widely accessible for Ubuntu and its derivatives, and other operating systems with `snap` pre-installed. This increases the security, if you are concerned about them, and while using `guiscrcpy` because, “snap is confined”.

What makes a snap better than the `PyPI` package is:

* security
* `guiscrcpy` works out of the box, meaning,`scrcpy` and `adb` are pre-installed on the `guiscrcpy` snap. Thanks to [@sisco311](https://github.com/sisco311/scrcpy-snap)

`guiscrcpy` snap is supported for all `AMD64` aka `x86_64` devices which support the [`snappy daemon`](https://snapcraft.io/docs/installing-snapd). macOS is an exception from the list. Use `brew` to install `snapd`

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/guiscrcpy)

> **NOTE**: 
>
> For issues regarding the: 
>
> * Failure of `scrcpy`: Please create an issue at [sisco311/scrcpy-snap](https://github.com/sisco311/scrcpy-snap/issues) and make sure that a similar issue does not exist. You wouldn’t want to disturb the developer
> * Failure of `guiscrcpy`: Please report it [here](https://github.com/srevinsaju/guiscrcpy/issues)

<br> 

## Windows Executable [![Windows Executable](https://github.com/srevinsaju/guiscrcpy/workflows/Windows%20Executable/badge.svg)](https://github.com/srevinsaju/guiscrcpy/actions?query=+event%3Apush++is%3Asuccess+branch%3Amaster+workflow%3A%22Windows+Executable%22)

`guiscrcpy` provides a compiled windows executable, for users who are not interested in installing python and `pip`. Although this is not, suggested (guiscrcpy is converted to the compiled python `*.pyc`), it is useful for end consumers on the Windows system.

Download the windows `.exe` either from releases, or click on the status badge to download the `exe `matching the latest commit.

Along with `guiscrcpy.exe`; You would also want to download windows binary of [scrcpy](https://github.com/Genymobile/scrcpy/releases/latest) and extract the `.zip` file to any directory you wish to. You may add it to path, if you like; but it is completely optional. If `scrcpy` is not found on `PATH`, guiscrcpy will open a file selector to select `scrcpy.exe`, `adb.exe` and `scrcpy-server`. 

Optionally, to get better appearance, you would like to install [Titillium Web](https://fonts.google.com/specimen/Titillium+Web). 

> **NOTE**: Windows Binaries are now available only for 64-bit. If you would like to have 32-bit  binary, please build `guiscrcpy` from source 

<br>

## Building from source ![GitHub commits since tagged version](https://img.shields.io/github/commits-since/srevinsaju/guiscrcpy/latest?style=flat-square)

See [BUILD](BUILD.md) for more information 

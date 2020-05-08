## Features

## Comparison


| Feature       | `guiscrcpy`   | other `*scrcpy*` alternatives  | commercial software   |
| ------------- | ------------- | ------------------------------ | --------------------- |
| Speed         | Faster, as it is independent from scrcpy engine  | Mostly integrated into the engine, making a GUI layer (slower)| Contains Ads or is through Internet, (data charges are inclusive) |
| Language | Python  | C-alternatives | Binary (unknown) |
| Type | Open source (you can edit them) | Open source | Proprietary |
| Other | Can write configuration file and handle events like swipe up, swipe down, App-switch, volume up | Can handle all events which is using a forked version of scrcpy | Can do everything except swipes and pinches |
| Compatibility (PC) | Windows 10+ / MacOS 10.15+ / Linux |  Windows 7 (32/64) / MacOS / Linux   | Windows 7 (32/64) / MacOS / Linux  |
| Compatibility (Mobile) | Android 5.0+ (given by scrcpy)| Android 5.0+ | Android 4.4+ |
| Base | scrcpy (original, created by @rom1v | forked scrcpy | no scrcpy |
| Keyboard Shortcuts | All the shortcuts which are mentioned by scrcpy | Unknown | Unknown |
| Official Packages provided | AppImages, Snaps, Windows Executable, Python BInary (pip wheels), Source Code | Unknown | Windows BInary, MacOS Binary |

## Highlights

#### Customized settings for [`scrcpy`](https://github.com/Genymobile/scrcpy)

`scrcpy` is a android screen mirroring command line interface tool. It does not save your configuration for your each run. Moreover, it requires some command line knowledge of how to use scrcpy and some developer background. There are already many unnecessary issues on `scrcpy`‘s repository, which is caused due to the complexity at which scrcpy’s options are handled. `guiscrcpy` makes use of this complexity and converts into a simple graphical user interface which creates `scrcpy ` 

> Configuration files not stored? Check the [FAQ](FAQ.md)

#### Desktop launcher

`scrcpy` is a command line interface, which seems quite non intuitive for users who do not use command line / non-developers. `guiscrcpy` creates a one click desktop shortcut, which enables users to start `guiscrcpy` by clicking on their desktop shortcut

### Slick GUI

<img src="img/mainwindow.png" alt="image-20200508151737658" style="zoom:67%;" />

The GUI is built with the help of `PyQt5`, It includes all the important command line functions that `scrcpy` can support. Along with the checkboxes on the main sceen; there is also additional settings in the settings menu

<img src="img/settings.png" alt="image-20200508152433666" style="zoom:67%;" />

Connecting your device over the internet is also easy as pie on `guiscrcpy`‘s Network Manager. This gets rid of all the commands you have to run to make your device connected to your PC.

 

#### Toolkits and Panels

`guiscrcpy` bundles side panels, bottom panels and an additional unique swipe panel, which does not exist in other screen mirroring clients. 

##### Swipe Panel (`guiscrcpy.ux.swipe.SwipeUX`)

Swipe Panel is a handy tool for users finding it relatively difficult to perform a swipe on the `scrcpy` client. The `swipe` buttons help to do traditional horizontal and vertical swipes on the screen.

![image-20200508145846052](img/swipe.png)

##### Toolkit (Side Panel) (`guiscrcpy.ux.toolkit.ToolkitUX`)

![Toolkit image (v1.12.1)](https://raw.githubusercontent.com/srevinsaju/guiscrcpy/1.12.1/docs/images/toolkit.png)

##### Bottom Panel (`guiscrcpy.ux.panel.PanelUX`)

The bottom panel is useful for devices with hardware buttons and which do not have on-screen navigations or `Android 10`‘s Gesture Navigation. To cope up with these functions; `guiscrcpy` included a bottom panel which can do all the basic functions similar to an android navigation bar.

![image-20200508151312903](img/panel.png)

### Multi-device Support

One of the important features `guiscrcpy` v3.8+ includes is multiple device support. This reduces the hardwork which happens in `scrcpy`to ented the `device serial_id` to connect to a device if multiple devices are found. 
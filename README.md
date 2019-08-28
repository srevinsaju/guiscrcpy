<img src=/ui/guiscrcpy_logo.png width=25%>

# guiscrcpy
A full fledged GUI integration for the
most award winning open-source android
screen mirroring system -- `scrcpy`
located on `https://github.com/genymobile/scrcpy/`
by [@rom1v](https://github.com/rom1v)

![image of guiscrcpy](/screen2.png)

## Table of Contents:
1. [Installation](#Installation)
2. [Features](#Features)
3. [Build](#Build)
4. [Known Issues](#Issues)
5. [Why guiscrcpy?](#why-guiscrcpy)
6. [Future Releases](#future-releases)
7. [Support](#support-me)
8. [Changelog](#changelog)


## Installation
[(skip)](#Features)

(Also called Step 0). Put a star on my repo. Gives support to #opensource and me!!
### Linux
For Linux, download the latest `guiscrcpy_linux-*` release, double click the file, and you are good to go.
As pre-requisite, you should do `sudo snap install scrcpy` to install the scrcpy engine.
### Windows
For Windows, the executable is compiled into an Installer. Download the #TODO
### MacOS
Unfortunately, I do not own a Mac device, and hence cant compile for one, but it is easy to build one. Read the [build instruction](#Build)


## Features
### Contents
The package includes four parts:

#### Main UI controller
![Main Window](/docs/images/main.png)

It handles all the pre - runtime features and gives flags to the `scrcpy` engine. It also includes a configuration writing system, which write the configuration file to the home directory, so `guiscrcpy` can read the information and run it, without
giving flags quite often.


#### Toolkit UI controller
<img src=/docs/images/toolkit.png>

The `toolkit` is an independent module, which is in
neither way connected to `scrcpy` or `guiscrcpy`, except for launching.

#### Bottom Panel controller
![Bottom Panel](/docs/images/bottompanel.png)

The `bottom_panel` is an additional floating windows
that helps to do basic controlling like **Home Key, Back Key, Power Key**. This include the most important functions, one would like to do with an Android device.
The most important feature of this module, is that **it has no interference with the `scrcpy` SDL layer, and hence maximum speed**

##### scrcpy engine
The scrcpy engine, is the classic v1.10 scrcpy, found on [scrcpy's github page by @rom1v](https://github.com/genymobile/scrcpy). On Windows release files, scrcpy, binary executable is also attached to make `PATH` problems easier to solve. On Linux, scrcpy has to be manually downloaded from `snap`


## Build
guiscrcpy can also be built from source. But that's easy as pie!
### Dependencies
* `PyQt5`
* `psutil`
* `qdarkstyle` (optional)

Before everything, make sure you have scrcpy on your path. You can Google it out, on how to do it.

Only Scrcpy 1.10
1. (Also called Step 0). Put a star on my repo. Gives support to #opensource!!
2. Install python3. If you don't have it install it from
[Python Software Website](https://python.org) or on Linux by <p>`sudo apt install python3.7`

3. Clone my git repo. or copy paste this to your _bash_ <p>`git clone https://github.com/srevinsaju/guiscrcpy`

4. Run the Python Package installer `pip` and run the commands below <p> `python3 -m pip install PyQt5 psutil` <p>

5. You can also run <p> `python3 -m pip install qdarkstyle` <p> if you require the dark breeze theme as shown in the image above.

6. So you are all set! Run the program by <p> `python3 __main__.py`

7. Read [Known Issues](#Issues) if you fall into some errors.


## Issues
### Linux (X Server)
For Linux operating systems, if python raises `Xlib>>ModuleNotFoundError`, then run <p>
`sudo apt install python3-xlib` <p>
`sudo apt install python3-qt5`

To use toolkit (development, on Linux only), run: <p>
`sudo apt install wmctrl xdotool`

### Some buttons not working
Some buttons like `clipboard`, `pinch in/out` are not enabled. But, however, you may enable it by recompiling the source code. I am looking forward for pinching on Android help / Documentation / links.

## Why guiscrcpy?

I have Python as a subject for Class XI, so as a part of it's advanced learning experience,
and because of my daily use of scrcpy, wanted to integrate GUI into the CLIbased app!!
**GUI** stands for Graphical User Interface, and **Py** is not inherited from scrc<b>py</b> but rather from <b>Py</b> for Python


## Future Releases
Surely, guiscrcpy has great scope of improvement.
Compared to paid Screen Mirroring software, scrcpy gives
a lot of advantages, but my future plans are as follows
* ~~Fix HOME_key, BACK_key. (Will have to wait until @rom1v examines my work)~~ Fixed!
* ~~Add better UI support with adb functions out of scrcpy~~ Fixed again!
* Support python3.8.
* Add service running indicator
* ~~Create pre-built installer and files, Will try fbs build system, after a quite while~~ Fixed!

## Support me!
Share your ideas, issues with me on github and email [srevin03@gmail.com](srevin03@gmail.com)!!



## Changelog

### Build 1.10.0
#### Highlights
##### New logo for guiscrcpy
The new logo for `guiscrcpy` has been deployed, licensed under *Creative Commons License Attribution 4.0*. A comparison between old and new. <p>
<img src="/ui/android_circle.png" width=49%> <img src="/ui/guiscrcpy_logo.png"  width=49%>
##### New UI and distributed controls
The new UI aims for faster ergonomics and consumer oriented. Individual modules, now are separate from scrcpy executable to provide speed to the mirroring system. The new UI also looks way better than the old one ;) <p>
<img src="/screen.png" width=100%> **OLD**
<img src="screen2.png"  width=100%>
**NEW**

#### Raw
* Fixed many bugs
* Better UI, based on Material principles
* Switched to dark theme, thanks to  `qdarkstyle`
* Faster `scrcpy` loading. Re-converted `StartScrcpy`
into `MyApp` class. `QThread` is not very fast, as it is said to be.
* Configuration has been updated to add `Keep Display Off`
* Added Orientation change command (potrait / landscape)
* Added user configuration file write to home directory on static line system. Users now automatically save theit information into the `.cfg file`
* Separated main controls from subsidiary controls. Linear layout and horizontal layout are separate.
* Users can now perform top to bottom or bottom to top swipe with notification buttons,
* Button utility is mentioned in tooltip
* Added Reset button to reset user config to defaults.
* Fixed QProgressBar blocking mainthread.



### Build 1.9.6
* Minor Fixes

### Build 1.9.5
25062019 2159
* MEGA CHANGE :: Migrated from `PyQt4` to `PyQt5` due to late realization that PyQt4 support
for Windows is unfortunately discontinued.
* `mainwindow.ui` >> xml parsed file loaded in uic loader has been compiled to `mainui.py` as UI
* toolkit.py is deprecated. toolkit class is restructured into mainwindow class with multiprocesing.
* After `PyQt5` update, GTK-LTK-KDE no longer raises pixmap errors
* Unreleased .ui files for Build. Only dependencies for release are png pixmap files


### Build 1.9.4
23062018 1615 GMT+300
* Dumped terminal QTextEdit for multiprocessing to prevent QThread hang.
* Restructured StartScrcpy Class as two threads.

### Build 1.9.3
22062019 1948 GMT+3
* Fixed GUI hang (issue reported by @rom1v)
(code has been restructured. the old code is placed in `/backup/` folder as `main 1.9.2.py`. But however, terminal ui QTextEdit
is not functional.

### Build 1.9.2
21062019 2000 GMT+3
* Added GUIScrcpy icon
* Added pixmap icons
* Added check scrcpy process running or not
* Added GUIScrcpy Toolkit Experimental Support
###1.9.1
* Initial Build :)

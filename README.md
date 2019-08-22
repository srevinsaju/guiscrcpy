# GUIscrcPy
A full fledged GUI integration for the 
most award winning open-source android 
screen mirroring system -- `scrcpy` 
located on `https://github.com/genymobile/scrcpy/`
by [@rom1v](https://github.com/rom1v)

![image of GUIscrcpy](/screen.png)

GUIScrcPy is a Python 3.7 based script (haven't tested compatibility issues
so far, but it does not work on Python 3.8 because of incombatibility og PyAutoGUI module)



**Why GUIscrcPy?**

I had Python as a subject for Class XI, so as a part of it's advanced learning experience,
and because of my daily use of scrcpy, wanted to integrate GUI into the CLIbased app!!
**GUI** stands for Graphical User Interface, and **Py** is not inherited from scrc<b>py</b> but rather from <b>Py</b> for Python 

##Contents
The package includes two codelets:
##### Main UI controller
it is the UI system that executes the fixed command to scrcpy engine. These are static.
##### Toolkit UI controller
It is the UI controller, which gives commands to the Scrcpy window to execute certain actions. <p> Read **Issues** and **Future Releases** , before proceeding
## Installation
* Release 1.9.4 :: Linux only. A pre-build independant package is available. Checkout at Releases. 
Only do <p> `$ sudo apt install wmctrl xdotool ` <p> The executable file is in the main file. GUIscrcpy.
* Windows OS is not supported in 1.9.4 due to the incompatibility of PyQt4 (discontinued with Python 3.4)

## Building from Source
GUIscrcPy can also be built from source. But that's easy again!

Before everything, make sure you have scrcpy on your path. You can Google it out, on how to do it, next build will have a automated build.
Only Scrcpy 1.9
1. (Also called Step 0). Put a star on my repo. Gives support to #opensource!!
2. Install python3. If you don't have it install it using 
Python Software Website or on Linux by <p>`sudo apt install python3.7`
3. Clone my git repo. or copy paste this to your _bash_ <p>`git clone https://github.com/srevinsaju/guiscrcpy`
4. Activate the virtual env by executing <p> `source venv/bin/activate` on Linux </p><p> `call venv/bin/activate` on Windows <p> 
You should be able to see (venv)
5. Run the Python Package installer `pip` and run the commands below <p> `python3 -m pip install pyside2 pyqt5 psutil pyautogui` <p>
If your OS is Linux-based, to use Toolkit, you need to install `wmctrl` and `xdotool`. These are optional to run the toolkit.
6. So you are all set! Run the program by <p> `python3 main.py`

## Dependencies
* `pyside2` (required) 
* `pyqt5` 
* `psutil` 
* `pyautogui` (for toolkit, required for Windows)


For Linux operating systems, if python raises `Xlib>>ModuleNotFoundError`, then run <p>
`sudo apt install python3-xlib` <p>
`sudo apt install python3-qt5vent `


To use toolkit (on Linux only), run:
`sudo apt install wmctrl xdotool` 

## Issues
There are problems with the toolkit in executing certain functions like HOME key and BACK key. I am not able to solve this on 
Linux because of the Xlib Graphics manager. On Windows, it should work properly,
but however, this hasn't been tested so far. I would like to know the results on [srevin03@gmail.com](srevin03@gmail.com)

## Future Releases
Surely, this is an initial build with great scope of improvement. Compared to paid Screen Mirroring software, scrcpy gives
a lot of advantages, but my future plans are as follows
* ~~Fix HOME_key, BACK_key.~~ (Will have to wait until @rom1v examines my work)
* Add better UI support with adb functions out of scrcpy
* Support python3.8 with PyAutoGUI support. Most of the project is based on PyAutoGUI, which is based on Windows, with less support for Linux.
I am on Linux, so i can't test them out, except WINE
* Add service running indicator
* ~~Create pre-built installer and files, Will try fbs build system, after a quite while~~

## Support me!
Share your ideas, issues with me on github and email [srevin03@gmail.com](srevin03@gmail.com)!!



## Changelog

### Build 1.9.7
* Fixed many bugs
* Added Orientation change command (potrait / landscape)
* Added user configuration file write to home directory on static line system. Users now automatically save theit information into the `.cfg file`
* Spearated main controls from subsidiary controls. Linear layout and horizontal layout are separate.
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
* Unreleased *.ui files for Build. Only dependencies for release are png pixmap files


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
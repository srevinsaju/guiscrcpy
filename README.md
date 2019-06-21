# GUIscrcPy
A full fledged GUI integration for the 
most award winning open-source android 
screen mirroring system -- `scrcpy` 
located on `https://github.com/genymobile/scrcpy/`
by [@rom1v](https://github.com/rom1v)

GUIScrcPy is a Python 3.7 based script (haven't tested compatibility issues
so far, but it does not work on Python 3.8 because of incombatibility og PyAutoGUI module)

![image of GUIscrcpy](/screen.png)

**Why GUIscrcPy?**

I had Python as a subject for Class XI, so as a part of it's advanced learning experience,
and because of my daily use of scrcpy, wanted to integrate GUI into the CLIbased app!!
**GUI** stands for Graphical User Interface, and **Py** is not inherited from scrc<b>py</b> but rather from <b>Py</b> for Python 


## Building from Source
Fortunately or Unfortunately, GUIscrcPy has to be built from source. But that's easy again!
1. (Also called Step 0). Put a star on my repo. Gives support to #opensource!!
2. Install python3. If you don't have it install it using 
Python Software Website or on Linux by <p>`sudo apt install python3.7`
3. Clone my git repo. or copy paste this to your _bash_ <p>`git clone https://github.com/srevinsaju/guiscrcpy`
4. use **cd** to move to the downloaded directory. `/bin/`

## Dependencies
* `pyside2` (required) 
* `pyqt5` 
* `psutil` 
* `pyautogui` (for toolkit, required for Windows)


For Linux operating systems, if python raises `Xlib>>ModuleNotFoundError`, then run
`sudo apt install python3-xlib`

To use toolkit (on Linux only), run:
`sudo apt install wmctrl xdotool` 
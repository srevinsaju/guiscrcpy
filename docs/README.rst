guiscrcpy
========= 
|CircleCI| |codecov| |Updates| |Python 3| |PyPI - Python Version| 
|PyPI| |PyPI - Wheel| |PyPI - Downloads| |AUR version| |Snap Status|
|GitHub All Releases| 
|License: GPL v3| 
|Twitter Follow| |GitHub followers| 
.. figure:: /docs/screen3.png    :alt: image of guiscrcpy     image of guiscrcpy
guiscrcpy is a multiplatform, ready-to-use GUI layer for Android to PC
screen mirroring written in the advancing programming language python3
for the most award winning open-source android screen mirroring system
-- ``scrcpy`` located on ``https://github.com/genymobile/scrcpy/`` by
[@rom1v](https://github.com/rom1v) 
**NOTE**: Make sure you `enabled adb
debugging <https://developer.android.com/studio/command-line/adb.html#Enabling>`__
on your device(s). 
Download
-------- 
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
|            | Ultra fast download                                                                                                                                                                                                                         | GitHub Release download                                                                                                             | Nightly Downloads (bin)                                                                                    |
+============+=============================================================================================================================================================================================================================================+=====================================================================================================================================+============================================================================================================+
|  Windows   | `**1.11.0** Windows 32/64 bit <https://mega.nz/#!fDAFAACb!N-jhb6GwRR6I-QNQQmy4AJrj0g8L5TQgwrcA4afKB0o>`__                                                                                                                                   | `1.10.0 Windows 32/64 bit <https://github.com/srevinsaju/guiscrcpy/releases/download/1.10/guiscrcpy-1.10-27082019-windows.exe>`__   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
|  Linux     | `For faster execution, we recommend the **Source code** on Linux <https://github.com/srevinsaju/guiscrcpy/archive/master.zip>`__ or `**1.10.1** Linux (amd64) <https://mega.nz/#!uSJ3yaSS!QMs_hPAG0wkJ0nq6ErT4I61-vT5ABCV9D_bF4-BSmbk>`__   | `1.10.0 Linux (amd64) <https://github.com/srevinsaju/guiscrcpy/releases/download/1.10/guiscrcpy-1.10-27082019-linux>`__             | `**Binary** - Nightly Builds <https://github.com/srevinsaju/guiscrcpy/tree/nightly#guiscrcpy-nightly>`__   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+ 
.. figure:: docs/images/feature.png    :alt: guiscrcpy feature     guiscrcpy feature
Table of Contents:
------------------ 
1. `Installation <#Installation>`__
2. `Features <#Features>`__
3. `Requirements <#requirements>`__
4. `Build <#Build>`__
5. `Where thing go Wrong <#Issues>`__
6. `Why guiscrcpy? <#why-guiscrcpy>`__
7. `Future Releases <#future-releases>`__
8. `Support <#support-me>`__
9. `Changelog <#changelog>`__ 
Installation
------------ 
`(skip) <#Features>`__ 
``guiscrcpy`` can be installed through source code (recommended) or by
downloading the release binary (Windows, Linux ~ Nightly Builds). (Also
called Step 0). Put a star on my repo. Gives support to #opensource and
me!! 
Installing from pip
~~~~~~~~~~~~~~~~~~~ 
It is the easiest way of installing guiscrcpy. Just use
``pip install guiscrcpy`` Replace ``pip`` with ``pip3`` if ``python3``
is not your default version. 
Building from source
~~~~~~~~~~~~~~~~~~~~ 
It is always recommended to run guiscrcpy from source due to its
flexibility and fast I/O speeds. Thanks to Python's interpreter
technology, commands are executed faster than ever. The procedure to
install guiscrcpy from source is same for all platform or OSes which
support python3. 
1. Clone the guiscrcpy GitHub repository. If you have ``git`` installed,    you may run this:    ``git clone https://github.com/srevinsaju/guiscrcpy`` 
If you do not have ``git`` installed on your system, you may click the
drop down menu from ``Clone this repository > Download Zip`` or `click
here. <https://github.com/srevinsaju/guiscrcpy/archive/master.zip>`__ 
2. Extract the files to a directory 
3. Linux users have a shortcut to do the installation process. Just run    ``./guiscrcpy-src-installer.sh``. It might ask for sudo password to    install it to the application menu. You may either deny it or accept    it or edit the script file to match your needs. If the script    completes successfully, you might be able to run ``guiscrcpy`` from    any directory, and see a Desktop launcher from your Appplication    Launcher. You may skip step 4. guiscrcpy is ready to use! 
4. On Windows, MacOS or Linux, where you didn't run step 3, you should    install the dependencies. The dependencies are provided in the    requirements.txt file. It is easier to install with    ``python3 -m pip install -r requirements.txt`` Use the --user flag to    keep the modules limited to the user account. Alternatively, you can    perform ``python3 -m pip install PyQt5 psutil qdarkstyle`` A    dependency that is optional is ``pystray``, which is meant for    developers only. 
5. Fire up guiscrcpy with this terminal command on     -  **Linux**: ``guiscrcpy`` or click the ``guiscrcpy icon`` on your       desktop launcher!    -  **Windows**: ``python3 guiscrcpy`` 
**NOTE**: 
(i)  Do not use Ctrl+C or Ctrl+Z to stop the program as it might run      into an unresponsive window. Alternatively, use the close button on      the panels. 
(ii) Before running from source, make sure you have ``scrcpy`` on your      path. You can Google it out, on how to do it. The Windows binary      packages ``scrcpy`` binaries along with it. Using      ``guiscrcpy-src-installer.sh`` also does not require you to consult      ``scrcpy`` on path 
Installing from Binary
~~~~~~~~~~~~~~~~~~~~~~ 
Windows 
^^^^^^^^ 
For Windows, the executable is compiled into an Installer. Download the
Portable file from GitHub or Mega, given in the `Downloads
section <#Downloads>`__. 
You may want to add ``guiscrcpy`` to the Start Menu, using
``Pin to Start`` button on Windows Explorer Panel. #### Linux For Linux,
download the latest official ``guiscrcpy_linux-*`` release from GitHub
or Mega on `Downloads section <#Downloads>`__, double click the file,
and you are good to go. As pre-requisite, you should do
``sudo snap install scrcpy`` to install the scrcpy engine. 
For Arch Linux and derived OSes, a **third-party maintainer** has
released a ``guiscrcpy-AUR`` and ``guiscrcpy-git``. See `Arch User
Repository <https://aur.archlinux.org/packages/guiscrcpy/>`__ 
MacOS
~~~~~ 
Unfortunately, I do not own a Mac device, and hence cant compile for
one, but it is easy to build one. Read the `build
instruction <#Build>`__ 
Features
-------- 
``guiscrcpy`` has many features which is very much required for day to
day usage for app developers, common users, students, commerce
departments, testers, production managers and helpline centres. Its
powerful side panels, bottom panels and floating console makes using
almost a touch controlled Android device, completely comprehensive on a
Desktop, laptop or a ``multitouch`` Tablet. 
``guiscrcpy`` uses USB or WiFi for screen mirroring. In comparison to
other android screen mirroring software, ``guiscrcpy`` uses as less as
``6 MiB`` on a RAM\*, and has high definition screen quality and latency
through USB, more than 16MB/s quality. Using WiFi reduces 
**Aim**
~~~~~~~ 
It focuses on: \* lightness (native, displays only the device screen) \*
performance (30~60fps) \* quality (1920×1080 or above) \* low latency
(35~70ms) \* low startup time (~1 second to display the first image) \*
non-intrusiveness (nothing is left installed on the device) > ~ from
`scrcpy README <https://github.com/Genymobile/scrcpy>`__ 
guiscrcpy focuses on: \* independent add on controls \* faster execution
(no need to waste time to think; oh, what was the command for changing
bitrate, etc.) \* configuration writing \* one handed controls \* easy
GUI 
**Requirements** : *What you need for ``guiscrcpy``*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
All the requirements are the same as that of ``scrcpy``. A copy of the
requirements are given below. 
The Android device requires at least API 21 (Android 5.0). 
Make sure you `enabled adb
debugging <https://developer.android.com/studio/command-line/adb.html#Enabling>`__
on your device(s). 
On some devices, you also need to enable `an additional
option <https://github.com/Genymobile/scrcpy/issues/70#issuecomment-373286323>`__
to control it using keyboard and mouse. 
**Comparison**: *Why ``guiscrcpy`` is better*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Feature                  | ``guiscrcpy``                                                                                     | other ``*scrcpy*`` alternatives                                   | commercial software                                                 |
+==========================+===================================================================================================+===================================================================+=====================================================================+
| Speed                    | Faster, as it is independent from scrcpy engine                                                   | Mostly integrated into the engine, making a GUI layer (slower)    | Contains Ads or is through Internet, (data charges are inclusive)   |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Language                 | Python                                                                                            | C-alternatives                                                    | Binary (unknown)                                                    |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Type                     | Open source (you can edit them)                                                                   | Open source                                                       | Proprietary                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Other                    | Can write configuration file and handle events like swipe up, swipe down, App-switch, volume up   | Can handle all events which is using a forked version of scrcpy   | Can do everything except swipes and pinches                         |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Compatibility (PC)       | Windows 7 (32/64) / MacOS / Linux                                                                 | Windows 7 (32/64) / MacOS / Linux                                 | Windows 7 (32/64) / MacOS / Linux                                   |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Compatibility (Mobile)   | Android 5.0+ (given by scrcpy)                                                                    | Android 5.0+                                                      | Android 4.4+                                                        |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Base                     | scrcpy (original, created by @rom1v                                                               | forked scrcpy                                                     | no scrcpy                                                           |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Keyboard Shortcuts       | All the shortcuts which are mentioned by scrcpy                                                   | Unknown                                                           | Unknown                                                             |
+--------------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+---------------------------------------------------------------------+ 
Connecting *Wirelessly*
~~~~~~~~~~~~~~~~~~~~~~~ 
*guiscrcpy* uses ``adb`` to communicate with the device, and ``adb`` can
[connect] to a device over TCP/IP: 
1. Connect the device to the same Wi-Fi as your computer.
2. Get your device IP address (in Settings → About phone → Status).
3. Open a Command Prompt window in ``C:\Program Files\guiscrcpy\`` .    (needed for only wireless connection)
4. Enable adb over TCP/IP on your device: Type this command    ``adb tcpip 5555``.
5. Unplug your device.
6. Connect to your device: Type this command:    ``adb connect DEVICE_IP:5555`` *(replace ``DEVICE_IP``)*.
7. Run ``guiscrcpy`` as usual. 
It may be useful to decrease the bit-rate and the definition: [connect]:
https://developer.android.com/studio/command-line/adb.html#wireless      ~ Quoted from scrcpy. 
Contents
~~~~~~~~ 
The package includes four parts: 
Main UI controller
^^^^^^^^^^^^^^^^^^ 
.. figure:: /docs/images/main.png    :alt: Main Window     Main Window
It handles all the pre - runtime features and gives flags to the
``scrcpy`` engine. It also includes a configuration writing system,
which write the configuration file to the home directory, so
``guiscrcpy`` can read the information and run it, without giving flags
quite often. 
Toolkit UI controller
^^^^^^^^^^^^^^^^^^^^^ 
The ``toolkit`` is an independent module, which is in neither way
connected to ``scrcpy`` or ``guiscrcpy``, except for launching. > NOTE:
See `Issues: Unable to drag panel <#Issues>`__ 
Bottom Panel controller
^^^^^^^^^^^^^^^^^^^^^^^ 
.. figure:: /docs/images/bottompanel.png    :alt: Bottom Panel     Bottom Panel
The ``bottom_panel`` is an additional floating windows that helps to do
basic controlling like **Home Key, Back Key, Power Key**. This include
the most important functions, one would like to do with an Android
device. The most important feature of this module, is that **it has no
interference with the ``scrcpy`` SDL layer, and hence maximum speed** >
NOTE: See `Issues: Unable to drag panel <#Issues>`__ 
SwipeUX panel
^^^^^^^^^^^^^ 
The ``guiscrcpy v1.11`` features a Swipe panel. Controlling a multitouch
device like Android devices can be limited with a mouse. To enhance this
efficiency, a SwipeUX Panel is added to do common swipes on all four
directions 
.. figure:: docs/images/swipeux.png    :alt: Swipe Panel     Swipe Panel
scrcpy engine
''''''''''''' 
The scrcpy engine, is the classic v1.10 scrcpy, found on [scrcpy's
github page by @rom1v](https://github.com/genymobile/scrcpy). On Windows
release files, scrcpy, binary executable is also attached to make
``PATH`` problems easier to solve. On Linux, scrcpy has to be manually
downloaded from ``snap``. The installation script does it automatically
for you. 
Keyboard shortcuts
~~~~~~~~~~~~~~~~~~ 
guiscrcpy includes all the shortcuts that scrcpy packages. These are all
the `keyboard
shortcuts <https://github.com/Genymobile/scrcpy#shortcuts>`__ 
Why guiscrcpy?
-------------- 
I have Python as a subject for Class XI, so as a part of it's advanced
learning experience, and because of my daily use of scrcpy, wanted to
integrate GUI into the CLIbased app!! **GUI** stands for Graphical User
Interface, and **Py** is not inherited from scrcpy but rather from Py
for Python 
Manual Building
--------------- 
Dependencies (for developers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
-  ``PyQt5``
-  ``psutil``
-  ``qdarkstyle``
-  ``pystray`` (optional, developers)
-  ``PyAutoGui`` (optional, developers, Windows only) 
Manual Building
~~~~~~~~~~~~~~~ 
1. (Also called Step 0). Put a star on my repo. Gives support to    #opensource!!
2. Install python3. If you don't have it install it from `Python    Software Website <https://python.org>`__ or on Linux by     .. raw:: html        <p>     ``sudo apt install python3.7`` 
3. Clone my git repo. or copy paste this to your *bash*     .. raw:: html        <p>     ``git clone https://github.com/srevinsaju/guiscrcpy`` 
4. Run the Python Package installer ``pip`` and run the commands below     .. raw:: html        <p>      ``python3 -m pip install -r requirements.txt``     .. raw:: html        <p> 
5. So you are all set! Run the program by     .. raw:: html        <p>      ``python3 guiscrcpy`` 
6. Read `Known Issues <#Issues>`__ if you fall into some errors. 
Future Releases
--------------- 
Surely, guiscrcpy has great scope of improvement. Compared to paid
Screen Mirroring software, scrcpy gives a lot of advantages, but my
future plans are as follows \* [STRIKEOUT:Fix HOME\_key, BACK\_key.
(Will have to wait until @rom1v examines my work)] Fixed! \*
[STRIKEOUT:Add better UI support with adb functions out of scrcpy] Fixed
again! \* Support python3.8. \* Add service running indicator \*
[STRIKEOUT:Create pre-built installer and files, Will try fbs build
system, after a quite while] Fixed! 
Issues
------ 
Linux (X Server)
~~~~~~~~~~~~~~~~ 
For Linux operating systems, if python raises
``Xlib>>ModuleNotFoundError``, then run 
.. raw:: html     <p> 
``sudo apt install python3-xlib`` 
.. raw:: html     <p> 
``sudo apt install python3-qt5`` 
To use toolkit (development, on Linux only), run: 
.. raw:: html     <p> 
``sudo apt install wmctrl xdotool`` 
Some buttons not working
~~~~~~~~~~~~~~~~~~~~~~~~ 
Some buttons like ``clipboard``, ``pinch in/out`` are not enabled. But,
however, you may enable it by recompiling the source code. I am looking
forward for pinching on Android help / Documentation / links. 
Unable to drag Panel or Toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
`According to Issue
#4 <https://github.com/srevinsaju/guiscrcpy/issues/4#>`__ created by
[@logix2](https://github.com/logix2), regarding some problems in
dragging panels in the Linux OS, in this case, using the ``Meta``,
``Super`` or ``Alt`` keys, to use the Desktop Window Manager
functionality in moving the Panel. 
Support me!
----------- 
Sponsor me or share your ideas, issues with me on github and email
`srevin03@gmail.com <srevin03@gmail.com>`__!! 
Developers
---------- 
``guiscrcpy``, on initializing, creates a guiscrcpy.cfg file in \*
Windows: ``C:\Users\<UserName>\AppData\guiscrcpy.cfg`` \* Linux:
``~/.config/guiscrcpy.cfg`` \* Mac and other OSes: ``~/guiscrcpy.cfg`` 
A user may create backups of configuration file, or edit them manually.
It is created by guiscrcpy and stored in the respective directories. The
structure of the .cfg file is not based on structured language, but
based on backslash n (new line) in LF and CRLF file type The structure
is as given below 
the cfg file struct:: \* :bitrate0 [Line 4] \* :dimension0 [Line 5] \*
:swtouches0 [Line 6] \* :fullscreen0 [Line 7] \* :dispRO0 [Line 8] 
The Line Numbers are based on Python's index numbers, whuch starts from
0 and ends in 8, in this case. 
Credits
------- 
Thanks to all of the developers, testers, friends and family who helped
me in this project. 
Special thanks to \* @logix2 - Issue #5, #7 \* @Strubbl - Issue #8 \*
Panel icons (home, back, bell, etc. located in ``\icons\*``) made by
Dave Gandy from www.flaticon.com used under Creative Commons 3.0
Unported. The original SVG black work by Dave Gandy has ben re-oriented,
flipped or color-changed. The rest of Terms and Conditions put formward
by CC-3.0:Unported has been feverently followed by the developer. Icons
have been adapeted in all the three windows. 
Changelog
--------- 
Build 1.11.0
~~~~~~~~~~~~ 
-  Added ``guiscrcpy-src-installer.sh`` which installs guiscrcpy to your    path and creates a desktop launcher
-  Added Swipe UX Windows 
Build 1.10.0
~~~~~~~~~~~~ 
Highlights
^^^^^^^^^^ 
New logo for guiscrcpy
'''''''''''''''''''''' 
The new logo for ``guiscrcpy`` has been deployed, licensed under
*Creative Commons License Attribution 4.0*. A comparison between old and
new. 
.. raw:: html     <p>        ##### New UI and distributed controls The new UI aims for faster
ergonomics and consumer oriented. Individual modules, now are separate
from scrcpy executable to provide speed to the mirroring system. The new
UI also looks way better than the old one ;) 
.. raw:: html     <p>   **OLD** **NEW** 
Raw
^^^ 
-  Fixed many bugs
-  Better UI, based on Material principles
-  Switched to dark theme, thanks to ``qdarkstyle``
-  Faster ``scrcpy`` loading. Re-converted ``StartScrcpy`` into    ``MyApp`` class. ``QThread`` is not very fast, as it is said to be.
-  Configuration has been updated to add ``Keep Display Off``
-  Added Orientation change command (potrait / landscape)
-  Added user configuration file write to home directory on static line    system. Users now automatically save theit information into the    ``.cfg file``
-  Separated main controls from subsidiary controls. Linear layout and    horizontal layout are separate.
-  Users can now perform top to bottom or bottom to top swipe with    notification buttons,
-  Button utility is mentioned in tooltip
-  Added Reset button to reset user config to defaults.
-  Fixed QProgressBar blocking mainthread. 
Build 1.9.6
~~~~~~~~~~~ 
-  Minor Fixes 
Build 1.9.5
~~~~~~~~~~~ 
25062019 2159 \* MEGA CHANGE :: Migrated from ``PyQt4`` to ``PyQt5`` due
to late realization that PyQt4 support for Windows is unfortunately
discontinued. \* ``mainwindow.ui`` >> xml parsed file loaded in uic
loader has been compiled to ``mainui.py`` as UI \* toolkit.py is
deprecated. toolkit class is restructured into mainwindow class with
multiprocesing. \* After ``PyQt5`` update, GTK-LTK-KDE no longer raises
pixmap errors \* Unreleased .ui files for Build. Only dependencies for
release are png pixmap files 
Build 1.9.4
~~~~~~~~~~~ 
23062018 1615 GMT+300 \* Dumped terminal QTextEdit for multiprocessing
to prevent QThread hang. \* Restructured StartScrcpy Class as two
threads. 
Build 1.9.3
~~~~~~~~~~~ 
22062019 1948 GMT+3 \* Fixed GUI hang (issue reported by @rom1v) (code
has been restructured. the old code is placed in ``/backup/`` folder as
``main 1.9.2.py``. But however, terminal ui QTextEdit is not functional. 
Build 1.9.2
~~~~~~~~~~~ 
21062019 2000 GMT+3 \* Added GUIScrcpy icon \* Added pixmap icons \*
Added check scrcpy process running or not \* Added GUIScrcpy Toolkit
Experimental Support ###1.9.1 \* Initial Build :) 
.. |CircleCI| image:: https://circleci.com/gh/srevinsaju/guiscrcpy/tree/master.svg?style=svg    :target: https://circleci.com/gh/srevinsaju/guiscrcpy/tree/master
.. |codecov| image:: https://codecov.io/gh/srevinsaju/guiscrcpy/branch/master/graph/badge.svg    :target: https://codecov.io/gh/srevinsaju/guiscrcpy
.. |Updates| image:: https://pyup.io/repos/github/srevinsaju/guiscrcpy/shield.svg    :target: https://pyup.io/repos/github/srevinsaju/guiscrcpy/
.. |Python 3| image:: https://pyup.io/repos/github/srevinsaju/guiscrcpy/python-3-shield.svg    :target: https://pyup.io/repos/github/srevinsaju/guiscrcpy/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/guiscrcpy?style=flat-square
.. |PyPI| image:: https://img.shields.io/pypi/v/guiscrcpy?style=flat-square
.. |PyPI - Wheel| image:: https://img.shields.io/pypi/wheel/guiscrcpy?style=flat-square
.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dm/guiscrcpy?color=dark%20green&logo=PYPI&logoColor=Green&style=flat-square
.. |AUR version| image:: https://img.shields.io/aur/version/guiscrcpy?label=Arch%20Linux%20Package&style=flat-square
.. |Snap Status| image:: https://build.snapcraft.io/badge/srevinsaju/guiscrcpy.svg    :target: https://build.snapcraft.io/user/srevinsaju/guiscrcpy
.. |GitHub All Releases| image:: https://img.shields.io/github/downloads/srevinsaju/guiscrcpy/total?style=flat-square
.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg    :target: https://www.gnu.org/licenses/gpl-3.0
.. |Twitter Follow| image:: https://img.shields.io/twitter/follow/srevinsaju?style=social
.. |GitHub followers| image:: https://img.shields.io/github/followers/srevinsaju?label=srevin%20Saju&style=social

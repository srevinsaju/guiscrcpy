#!/usr/bin/env bash
echo guiscrcpy-installer by srevinsaju
echo All Rights Reserved
echo ====================
rm -r ~/.local/bin/guiscrc*
rm -r ~/.local/share/guiscr*
echo Removing obsolete files
mkdir ~/.local/share/guiscrcpy
cp -r guiscrcpy ~/.local/share/guiscrcpy
echo Copying scripts ... 
cp -r installers/linux/guiscrcpy-src-launcher.sh ~/.local/bin/guiscrcpy
chmod +x ~/.local/bin/guiscrcpy
echo Adding Desktop Launcher
rm -r ~/.local/share/applications/guiscrcpy.desktop
rm -r /usr/share/guiscrcpy
mkdir /usr/share/guiscrcpy

cp installers/linux/icons/guiscrcpy_logo.png /usr/share/guiscrcpy/
cp installers/linux/icons/guiscrcpy.desktop ~/.local/share/applications/
echo Script Succeeded


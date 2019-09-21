#!/usr/bin/env bash
echo guiscrcpy-installer by srevinsaju
echo All Rights Reserved
echo ====================
echo Installing dependencies
echo Installing scrcpy
sudo snap install scrcpy
echo Installing python modules
cat requirements.txt
python3 -m pip install -r requirements.txt
sudo rm -r ~/.local/bin/guiscrc*
sudo rm -r ~/.local/share/guiscr*
echo Removing obsolete files
sudo mkdir ~/.local/share/guiscrcpy
sudo cp -r guiscrcpy ~/.local/share/guiscrcpy
echo Copying scripts ... 
sudo cp -r installers/linux/guiscrcpy-src-launcher.sh ~/.local/bin/guiscrcpy
sudo chmod +x ~/.local/bin/guiscrcpy
echo Adding Desktop Launcher
sudo rm -r ~/.local/share/applications/guiscrcpy.desktop
sudo rm -r /usr/share/guiscrcpy
sudo mkdir /usr/share/guiscrcpy

sudo cp installers/linux/icons/guiscrcpy_logo.png /usr/share/guiscrcpy/
sudo cp installers/linux/icons/guiscrcpy.desktop ~/.local/share/applications/
echo Script Succeeded
echo Now You can run guiscrcpy by running 'guiscrcpy' from terminal or from your application launcher. 

#!/usr/bin/env python
"""
Create desktop shortcuts for Windows
"""
from __future__ import print_function

import os
from collections import namedtuple

import win32com.client
from win32com.shell import shell, shellcon

UserFolders = namedtuple("UserFolders", ("home", "desktop", "startmenu"))

scut_ext = 'lnk'
ico_ext = 'ico'


def get_conda_active_env():
    '''Return name of active conda environment or empty string'''
    conda_env = None
    try:
        conda_env = os.environ['CONDA_DEFAULT_ENV']
    except KeyError:
        print("No conda env active, defaulting to base")
        conda_env = ""
    return conda_env


# batch filename to activate the environment
# for Anaconda Python before running command.
conda_env = get_conda_active_env()
ENVRUNNER = """
@ECHO OFF
call %~dp0%activate {0}
echo # run in conda environment "%CONDA_DEFAULT_ENV%":
echo # %*
%*
""".format(conda_env)

_WSHELL = win32com.client.Dispatch("Wscript.Shell")


# Windows Special Folders
# see: https://docs.microsoft.com/en-us/windows/win32/shell/csidl

def get_homedir():
    '''Return home directory:
    note that we return CSIDL_PROFILE, not
    CSIDL_APPDATA, CSIDL_LOCAL_APPDATA,  or CSIDL_COMMON_APPDATA
    '''
    return shell.SHGetFolderPath(0, shellcon.CSIDL_PROFILE, None, 0)


def get_desktop():
    '''Return user Desktop folder'''
    return shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0)


def get_startmenu():
    '''Return user Start Menu Programs folder
    note that we return CSIDL_PROGRAMS not CSIDL_COMMON_PROGRAMS
    '''
    return shell.SHGetFolderPath(0, shellcon.CSIDL_PROGRAMS, None, 0)


def get_folders():
    """get user-specific folders
    Returns:
    -------
    Named tuple with fields 'home', 'desktop', 'startmenu'
    Example:
    -------
    """
    return UserFolders(get_homedir(), get_desktop(), get_startmenu())


def make_shortcut():
    userfolders = get_folders()

    desktop, startmenu = True, True
    for (create, folder) in ((desktop, userfolders.desktop),
                             (startmenu, userfolders.startmenu)):

        if not os.path.exists(folder):
            os.makedirs(folder)
        dest = os.path.join(folder, "guiscrcpy.lnk")

        wscript = _WSHELL.CreateShortCut(dest)
        wscript.Targetpath = 'guiscrcpy.exe'
        wscript.WorkingDirectory = userfolders.home
        wscript.WindowStyle = 0
        wscript.Description = "An Open Source Android Screen Mirroring System"
        wscript.IconLocation = os.path.join(os.path.abspath(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            'ui', 'icons',
            'guiscrcpy_logo_SRj_icon.ico')
        wscript.save()

    return True

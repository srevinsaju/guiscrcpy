from setuptools import setup
import sys,os
from os import path
import git
# from pyshortcuts import make_shortcut
import platform
from shutil import copyfile
repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name = 'guiscrcpy',
    version = repo.git.describe("--tags")[:-9],
    description = 'An Open Source - Fast -  Android Screen Mirroring system.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL v3',
    author = 'srevinsaju',
    author_email="srevin03@gmail.com",
    packages = ['guiscrcpy'],
    url = "https://srevinsaju.github.io/guiscrcpy",
    download_url = "https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    package_data={'guiscrcpy': ['*', '*.*', 'dark/*', 'icons/*', 'fonts/*', 'rsrc/*', 'ui/*'],
        '.':[".git/info/*"]
                 },
    include_package_data = True,
    install_requires=['PyQt5','psutil','qdarkstyle', 'pynput', 'gitpython'],
    scripts = ["guiscrcpy/guiscrcpy", "guiscrcpy/guiscrcpy-mapper"],
    classifiers = ['Operating System :: OS Independent',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)


#print("CREATING SHORTCUTS...")
#"""entry_points = {
#        'console_scripts': [
#            'guiscrcpy=guiscrcpy.__main__:launch_main']
#
"""
print("thanks to pyshortcuts by @newvile shortcuts for pip packages are easier than ever")

if platform.platform()=="Windows":
    cfgpath = os.path.expanduser("~/AppData/Local/guiscrcpy/")
else:
    cfgpath = os.path.expanduser("~/.config/guiscrcpy/")

#def last_i():
#    
    copyfile("./guiscrcpy/icons/guiscrcpy_logo_SRj_icon.ico", cfgpath+"logo.ico") 
    make_shortcut(
        script=os.path.expanduser("~/.local/bin/guiscrcpy"),
        name="guiscrcpy",
        description="Open Source GUI based Android Screen Mirroring System",
        icon=cfgpath + "logo.ico",
        desktop=True,
        startmenu=True,
        executable=None,
    )

            
last_i()
"""

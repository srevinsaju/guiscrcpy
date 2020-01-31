from setuptools import setup
import sys
import os
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

ver = repo.git.describe("--tags")
if '-' in ver:
    ver = ver[:-9]


setup(
    name='guiscrcpy',
    version=ver,
    description='An Open Source - Fast -  Android Screen Mirroring system.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL v3',
    author='srevinsaju',
    author_email="srevin03@gmail.com",
    packages=['guiscrcpy'],
    url="https://srevinsaju.github.io/guiscrcpy",
    download_url="https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    package_data={'guiscrcpy': ['*', '*.*', 'resources/*', 'ui/*', 'lib/*', 'platform/*', 'theme/*', 'ux/*'],
                  '.': [".git/info/*"]
                  },
    include_package_data=True,
    install_requires=['PyQt5>=5.14', 'psutil', 'pynput', 'gitpython'],
    scripts=["scripts/guiscrcpy", "scripts/guiscrcpy-mapper"],
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.8',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)

#!/usr/bin/env python3
"""

GUISCRCPY by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

from setuptools import setup
from setuptools import find_packages
import os
import platform

try:
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(
        os.path.join(this_directory, 'README.md'),
        encoding='utf-8'
    ) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = \
        "Open Source Android Screen Mirroring System by @srevinsaju"

requirements = ['PyQt5>=5.14,<5.16', 'pynput', 'qtpy']
if platform.system() == 'Windows':
    requirements.extend(['pywin32', 'psutil'])
elif platform.system() == 'Linux':
    requirements.extend(['psutil', 'cairosvg'])

data_files = [
        ('share/applications', ['guiscrcpy.desktop']),
        ('share/icons/hicolor/scalable/apps', ['appimage/guiscrcpy.png']),
    ]

setup(
    name='guiscrcpy',
    version='4.3.0',
    description='An Open Source - Fast - Android Screen Mirroring system.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL v3',
    author='srevinsaju',
    author_email="srevin03@gmail.com",
    packages=find_packages(),
    data_files=data_files,
    extras_require={'pyqt5': 'PyQt5', 'pyside2': 'PySide2'},
    url="https://srevinsaju.github.io/guiscrcpy",
    download_url="https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    include_package_data=True,
    install_requires=requirements,
    scripts=["scripts/guiscrcpy"],
    entry_points={'console_scripts': ['guiscrcpy = guiscrcpy.cli:cli']},  # noqa: E501
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
)

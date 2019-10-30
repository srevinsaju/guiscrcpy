from setuptools import setup
import sys,os
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'guiscrcpy',
    version = '1.11.40',
    description = 'an open source - fast -  android screen mirroring system.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='gpl v3',
    author = 'srevinsaju',
    packages = ['guiscrcpy'],
    url = "https://srevinsaju.github.io/guiscrcpy",
    download_url = "https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    package_data={'guiscrcpy': ['*', '*.*', 'dark/*', 'icons/*', 'fonts/*', 'rsrc/*', 'ui/*']
        
                 },
    include_package_data = True,
    install_requires=['pyqt5','psutil','qdarkstyle'],
    #entry_points = {
    #    'console_scripts': [
    #        'guiscrcpy=guiscrcpy.guiscrcpy:main']
    #        },
    scripts=['guiscrcpy/bin/guiscrcpy'],
    classifiers = ['operating system :: os independent',
            
            'programming language :: python :: 3.6',
            'operating system :: macos :: macos x',
            'operating system :: microsoft :: windows',
            'operating system :: posix',
            'license :: osi approved :: gnu general public license v3 (gplv3)'],
)

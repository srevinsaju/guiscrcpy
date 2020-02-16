from setuptools import setup
import sys
import os
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def gen_version():
    import git

    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    ver = repo.git.describe("--tags")
    raw_version = ver.split('-')
    if len(raw_version) == 1:
        # Stable Release
        v = "{}".format(raw_version[0])
    elif len(raw_version) == 2:
        # Release Candidate
        v = "{major}.post{minor}".format(major=raw_version[0], minor=raw_version[1])
    else:
        # Revision Dev
        v = "{major}.post{minor}.dev".format(major=raw_version[0], minor=raw_version[1])

    return v

try:
    v = gen_version()
except Exception as e:
    print("WARNING: {}".format(e))
    v = "3.x.src.dev"

setup(
    name='guiscrcpy',
    version="{}".format(v),
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
    install_requires=['PyQt5==5.14.1', 'psutil', 'pynput', 'gitpython'],
    scripts=["scripts/guiscrcpy", "scripts/guiscrcpy-mapper"],
    entry_points={
        'console_scripts': [
            'guiscrcpy = guiscrcpy.launcher:bootstrap',
        ]
    },
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.8',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)

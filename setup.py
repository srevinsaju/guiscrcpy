from setuptools import setup
import distutils.core
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="guiscrcpy",
    version="1.11.0",
    author="Srevin Saju",
    author_email="srevin03@gmail.com",
    description="A powerful UI/UX based Android Screen Mirroring software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srevinsaju/guiscrcpy",
    packages=['guiscrcpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GPL v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={'':['*','dark/*','fonts/*','icons/*','rsrc/*','ui/*']},

    include_package_data=True,
    install_requires=['PyQt5','psutil','qdarkstyle'],
    
)

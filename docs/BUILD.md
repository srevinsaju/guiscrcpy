# Build

`guiscrcpy` is delivered to users by building from source. It is not relatively complicated because, most of the build functions are handled by Python’s `setuptools` and `make`. 

To understand how the build works, it is important to understand the components of `guiscrcpy`

* External dependencies (`PyQt5`, `psutil`, ...)
* User Interface files
* Source Code

The order of the build is important for the successful build and deploy of `guiscrcpy` to your system, which is given above. 

<br>

## v3.8+

From **v3.8** onwards, the entire process has been simplified, to a single `MakeFile`.

### Local Installation

```bash
make
make install
```

### System Installation (`sudo`)

```bash
make
sudo make install
```

> **NOTE**: 
>
> * You should run `make` without `sudo`, otherwise, it might create permission conflicts. 
> * At most times, only `make install` is necessary; `make` is only necessary, if you tried to edit the files related to `guiscrcpy`
> * `make` is important and is required, if your system installation of `PyQt5` does not match the `5.14.x` version.
> * It is possible to build a custom version of `guiscrcpy` which works with `PyQt5==5.13`, `PyQt5==5.12`, `PyQt5==5.11` by appropriately running `make` and patching files (if necessary)

<br>

### Replicate `master`/ `branch` directly to your system

If you do not want to build `guiscrcpy`‘s UI on your system; you can only do

```
pip3 install .
```

Use `--user` parameter if necessary.



## v3.5+

A typical build (v**3.5**+) has a sequence of commands as:

```bash
# Install deps
pip3 install -r requirements.txt

# Regenerate the User Interface 
pyrcc5 guiscrcpy/ui/rsrc.qrc -o guiscrcpy/ui/rsrc_rc.py
pyuic5 guiscrcpy/ui/mainwindow.ui -o guiscrcpy/ui/main.py --from-imports
pyuic5 guiscrcpy/ui/downloader.ui -o guiscrcpy/ui/downloader.py --from-imports
pyuic5 guiscrcpy/ui/bottompanelui.ui -o guiscrcpy/ui/panel.py --from-imports
pyuic5 guiscrcpy/ui/toolkit_ui.ui -o guiscrcpy/ui/toolkit.py --from-imports
pyuic5 guiscrcpy/ui/network.ui -o guiscrcpy/ui/network.py --from-imports
pyuic5 guiscrcpy/ui/settings.ui -o guiscrcpy/ui/settings.py --from-imports

# Install it to system
pip3 install .
```


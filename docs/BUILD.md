# Build

```bash

git clone https://github.com/srevinsaju/guiscrcpy 
cd guiscrcpy 
poetry install
poetry run python3 -m guiscrcpy 
```


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

### M1 specific build instructions

Macs with Apple Silicon chips need to follow these steps to build. Watch [this video](https://youtu.be/JsqV5QJQ0Y4) for aid.

- Install `scrcpy` from [homebrew](https://brew.sh) and `poetry` from [python-poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions).

- Delete `python@3.9` dependency that comes along with scrcpy because `qtpy` and `pyside2` conflict with it. As long as you have any other python version in your `PATH`, it won't affect other dependencies.
    ```
    brew uninstall --ignore-dependencies python@3.9
    ```

- Clone the repository.

- `cd` into the directory with a Rosetta2 emulated terminal.

- Download `guiscrcpy` dependencies.
    ```
    poetry install -E PySide2
    ```

- Launch `guiscrcpy`:
    ```
    poetry run guiscrcpy
    ```
    
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


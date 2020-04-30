# Configuration

guiscrcpy places a configuration file called `guiscrcpy.json` in 

## Windows
`C:\Users\<username>\AppData\guiscrcpy\guiscrcpy.json`

## Linux
`$XDG_CONFIG_HOME/guiscrcpy/guiscrcpy.json` Environment Variable, which, if not defined defaults
to `~/.config/guiscrcpy/guiscrcpy.json`

The CLI are placed in `~/.local/bin` by default (PyPI) 

## macOS
`~/.config/guiscrcpy/guiscrcpy.json`

# Sample Configuration file
The configuration file uses JavaScript Object Notation, to easily retrieve and write data. A user may also edit the configuration file to edit the default settings

```json
{
    "adb": "/usr/bin/adb",
    "bitrate": 8000,
    "cmx": "",
    "dimension": null,
    "dispRO": false,
    "extra": "",
    "fullscreen": false,
    "paths": [
        "bin",
        "/usr/bin",
        "~/.local/bin",
        "~/bin",
        "/usr/local/bin"
    ],
    "scrcpy": "/usr/bin/scrcpy",
    "scrcpy-server": null,
    "swtouches": false
}
```
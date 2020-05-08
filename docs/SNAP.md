# Snap

The `snap` is a special distribution of `guiscrcpy` for Linux and Mac users. The `guiscrcpy` package also includes the `scrcpy` and `adb` package along with `guiscrcpy`. This helps to make `guiscrcpy` run it out of the box without any specific user configuration. However; `guiscrcpy` is published as a confined snap. It is important to connect the `home` plug to the snap so that `guiscrcpy` can run it and save the configuration files to you r `~/.config/guiscrcpy`. Moreover; the snap does not allow [Semaphores](https://google.com/search?=semaphores+multiprocessing); as a result; multi threading tasks cannot be run on the snap; for example; scanning the LAN for open ports might not be possible for now. You can manually enter the IP address of the device in the box below.

## Installation

The `guiscrcpy` `snap` can be installed as given below

```bash
snap install guiscrcpy
```

The above command installs the stable version of `guiscrcpy` on your system

To get bleeding-edge test releases

```bash
snap install guiscrcpy --edge
```

> NOTE: In some cases, you might need to use `sudo` before the snap installation command due to permission errors.

### Post-Installation

After installation; to enable saving your configuration files to your home folder; you will have to execute the following commands

```bash
snap connect guiscrcpy:home
```

> NOTE: Use `sudo` whenever necessary

The `network` plug is automatically connected on the `snap` install; So basically you do not need to worry about it.



## Accessing `scrcpy` and `adb` on the `guiscrcpy` snap

In some cases where you would like to do some debugging or to know why your device is not being displayed in the `guiscrcpy`‘s device panel, you might need to access guiscrcpy’s `adb` and `scrcpy`

To access scrcpy

```bash
guiscrcpy.scrcpy
```

To access adb

```bash
guiscrcpy.adb
```

If you have any problems related to `snaps` please create an issue with `[SNAP]` before the Issue title




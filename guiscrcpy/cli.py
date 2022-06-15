import os
import platform
import sys
import traceback

import click
import colorama
from click import Context
from qtpy.QtWidgets import QApplication
from qtpy import QtCore, QtWidgets

from .lib.utils import format_colors as fc, show_message_box
from .launcher import bootstrap
from .lib.bridge.exceptions import ScrcpyNotFoundError
from .lib.bridge.exceptions import AdbNotFoundError
from .lib.bridge.exceptions import ScrcpyServerNotFoundError
from .lib.bridge import AndroidDebugBridge
from .lib.config import InterfaceConfig, InvalidConfigurationError
from .version import VERSION
from . import __doc__ as lic


# initialize colorama on Windows systems
colorama.init()


# srevin: bad snap!
_sys_argv = list()
for arg in sys.argv:
    if not arg.startswith("/snap"):
        _sys_argv.append(arg)
sys.argv = _sys_argv


def show_version(ctx, param, value):  # noqa:
    """Prints the version of the utility"""
    if not value or ctx.resilient_parsing:
        return
    click.echo(fc("{g}guiscrcpy {rst}v{v}", v=VERSION))
    if os.getenv("APPIMAGE"):
        click.echo("Running from AppImage")
    if os.getenv("APPDIR"):
        click.echo("AppDir: {}".format(os.getenv("APPDIR")))
    import inspect
    from PyQt5 import Qt

    _pyqt5_version = [
        "%s = %s" % (k, v)
        for k, v in vars(Qt).items()
        if k.lower().find("version") >= 0 and not inspect.isbuiltin(v)
    ]
    print()
    print("== PyQt5 Version ==")
    print("\n".join(sorted(_pyqt5_version)))
    print()
    if platform.system() == "Linux":
        print("== CairoSVG version ==")
        from cairosvg import VERSION as CAIRO_VERSION  # noqa:

        print("CairoSVG == {}".format(CAIRO_VERSION))
        print()

    ctx.exit()


def show_license(ctx, param, value):  # noqa:
    """Prints the license of the utility"""
    if not value or ctx.resilient_parsing:
        return
    click.echo(lic)
    ctx.exit()


@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    "--version", is_flag=True, callback=show_version, expose_value=False, is_eager=True
)
@click.option(
    "--license",
    "--lic",
    is_flag=True,
    callback=show_license,
    expose_value=False,
    is_eager=True,
)
@click.option(
    "-T",
    "--theme",
    "theme",
    default="Breeze",
    help="Set the default theme (based on PyQt5 "
    "themes - Fusion, Breeze, Windows) "
    "(stored in configuration, override by --theme-no-cfg)",
)
@click.option(
    "-W",
    "--hide-wm-frame/--show-wm-frame",
    "hide_wm_frame",
    default=True,
    help="Show window manager border frame.",
)
@click.option(
    "--debug-disable-scrcpy",
    "debug_disable_scrcpy",
    default=False,
    is_flag=True,
    help="Do not launch scrcpy even when 'Start Scrcpy' is pressed",
)
@click.option(
    "-A",
    "--always-on-top/--disable-always-on-top",
    "aot",
    default=True,
    help="Forces the panels to be always of top",
)
def cli(
    ctx: Context,
    hide_wm_frame: bool = True,
    aot: bool = True,
    theme: str = "Breeze",
    debug_disable_scrcpy: bool = False,
):
    """guiscrcpy: Graphical user interface for scrcpy"""
    print(fc("\n{b}guiscrcpy {v}{rst}", v=VERSION))
    print(fc("by @srevinsaju"))
    print(fc("{x}https://github.com/srevinsaju/guiscrcpy{rst}\n\n"))
    if ctx.invoked_subcommand is not None:
        return
    try:
        # why this try block?
        # this is because, in case guiscrcpy crashes,
        # it will log the traceback to the terminal
        # but it would not be visible to users without CLI interface
        # enable High DPI scaling

        if platform.system() == "Windows":
            import ctypes

            # why this code?
            # In Windows 7 or later, the taskbar is not for "Application" but for "Application User Model/AppUserModel"
            # pythonw.exe application is host process, it means all application run by pythonw.exe will use same AppUserModel as pythonw.exe
            # So that applications runs by pythonw.exe will use same taskbar
            # To avoid this we must set AppUserModel id explicity
            # see this
            # https://stackoverflow.com/a/1552105/9986755
            # thttp://msdn.microsoft.com/en-us/library/dd378459%28VS.85%29.aspx#host
            appid = "srevinsaju.guiscrcpy"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        # use HIGH DPI icons
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        # init core
        app = QtWidgets.QApplication(sys.argv)
        config_manager = InterfaceConfig()
        bootstrap(
            app=app,
            config_manager=config_manager,
            theme=theme,
            aot=aot,
            hide_wm_frame=hide_wm_frame,
            debug_no_scrcpy=debug_disable_scrcpy,
        )
    except ScrcpyNotFoundError:
        _msg_box = show_message_box(
            text="Scrcpy not found",
            info_text="guiscrcpy could not find scrcpy. "
            "Make sure you select scrcpy in the dialog box "
            "or add scrcpy to PATH. You can get the latest release "
            "of scrcpy from <a href='"
            "https://github.com/Genymobile/scrcpy'>"
            "Genymobile/scrcpy 's GitHub Releases</a> "
            "and select the <pre>scrcpy{ext}</pre> when you run "
            "guiscrcpy next time".format(
                ext=".exe" if platform.system() == "Windows" else ""
            ),
        )
        _msg_box.exec_()
        print("Aborting!")
        sys.exit(-1)
    except AdbNotFoundError:
        _msg_box = show_message_box(
            text="ADB not found",
            info_text="guiscrcpy could not find adb. "
            "Make sure you select adb in the dialog box or add adb to PATH",
        )
        _msg_box.exec_()
        print("Aborting!")
        sys.exit(-1)
    except InvalidConfigurationError:
        _msg_box = show_message_box(
            text="Invalid configuration error",
            info_text="The configuration file for guiscrcpy is invalid. <br>"
            "This is possibly because a new version of guiscrcpy "
            "was installed, or the old paths to `adb` and `scrcpy` "
            "as defined in the configuration file, no longer exists "
            "in the same path. To fix this error,"
            "Run  "
            "<pre>guiscrcpy config -r</pre> on your terminal.",
        )
        _msg_box.exec_()
        print("Aborting!")
        sys.exit(-1)
    except ScrcpyServerNotFoundError:
        _msg_box = show_message_box(
            text="Scrcpy server not found error",
            info_text="The configuration file for guiscrcpy is invalid. <br>"
            "This is possibly because a new version of guiscrcpy "
            "was installed, or the old paths to `adb` and `scrcpy` "
            "as defined in the configuration file, no longer exists "
            "in the same path. To fix this error,"
            "Run  "
            "<pre>guiscrcpy config -r</pre> on your terminal.",
        )
        _msg_box.exec_()
        print("Aborting!")
        sys.exit(-1)
    except Exception:  # noqa:
        error_message = traceback.format_exc(chain=True)
        print(error_message)
        _msg_box = show_message_box(
            text="Error: Unhandled exception",
            info_text="<pre>{error_message}</pre>"
            "Please report this, if its a bug, to <a href="
            "'https://github.com/srevinsaju/guiscrcpy/issues'>"
            "guiscrcpy bug tracker</a> as it will help to improve "
            "the next release.".format(error_message=error_message),
        )
        _msg_box.exec_()
        print("Aborting!")
        sys.exit(-1)


@cli.command()
@click.option(
    "--device-id",
    "device_id",
    help="Sets the device-id for mapper to configure "
    " (optional, needed for multiple devices)",
)
@click.option(
    "-r",
    "--reset",
    "reset",
    is_flag=True,
    help="Reset guiscrcpy's mapper configuration file",
)
def mapper(device_id=None, reset=False):
    """Run the guiscrcpy mapper"""
    config_manager = InterfaceConfig()
    config = config_manager.get_config()
    mapper_cfg_path = os.path.join(
        config_manager.get_cfgpath(), "guiscrcpy.mapper.json"
    )
    if reset:
        # A ternary version of removing a file if it exists
        # https://stackoverflow.com/q/10840533/
        mapper_configuration_file_exists = (
            os.remove(mapper_cfg_path) if os.path.exists(mapper_cfg_path) else None
        )
        if mapper_configuration_file_exists:
            print("guiscrcpy mapper configuration file has been removed.")
            print("Removed {}".format(mapper_configuration_file_exists))
        else:
            print("guiscrcpy mapper configuration is not created yet.")
        return

    if os.getenv("GUISCRCPY_ADB"):
        adb_path = os.getenv("GUISCRCPY_ADB")
    else:
        adb_path = config["adb"]
    adb = AndroidDebugBridge(adb_path)
    adb_devices_list = adb.devices()
    if len(adb_devices_list) == 0:
        print("E: No devices found")
        sys.exit(1)
    elif len(adb_devices_list) == 1:
        mapper_device_id = adb_devices_list[0][0]
    elif not device_id:
        print("Please pass the --device-id <device_id> to initialize " "the mapper")
        sys.exit(1)
    else:
        mapper_device_id = device_id

    from guiscrcpy.lib.mapper.mapper import Mapper

    # Initialize the mapper if it is called.
    adb = AndroidDebugBridge(path=config_manager.get_config().get("adb"))
    mp = Mapper(mapper_device_id, adb=adb, config_path=mapper_cfg_path)
    if not os.path.exists(
        os.path.join(config_manager.get_cfgpath(), "guiscrcpy.mapper.json")
    ):
        print("guiscrcpy.mapper.json does not exist. ")
        print("Initializing Mapper Configuration for the first time use.")
        mp.initialize(initialize_qt=True)
    else:
        mp.read_configuration()
        print("guiscrcpy.mapper.json found. Starting the mapper...")
        print("Your keyboard is being listened by guiscrcpy-mapper")
        print("pressing any key will trigger the position.")
        print()
        print("If you would like to register new keys, pass --mapper-reset")
        print("\nInitializing\n\n")
        mp.listen_keypress()
        print("Done!")


@cli.command("adb")
@click.argument("args", nargs=-1)
def adb_cli(args):
    """Create an interface with the Android Debugging bridge"""
    config_manager = InterfaceConfig()
    config = config_manager.get_config()
    if os.getenv("GUISCRCPY_ADB"):
        adb_path = os.getenv("GUISCRCPY_ADB")
    else:
        adb_path = config["adb"]
    print("Interfacing guiscrcpy-adb")
    os.system("{} {}".format(adb_path, " ".join(args)))
    pass


@cli.command()
@click.argument("args", nargs=-1)
def scrcpy(args):
    """Create an interface with scrcpy"""
    config_manager = InterfaceConfig()
    config = config_manager.get_config()
    if os.getenv("GUISCRCPY_SCRCPY"):
        scrcpy_path = os.getenv("GUISCRCPY_SCRCPY")
    else:
        scrcpy_path = config["scrcpy"]
    print("Interfacing guiscrcpy-scrcpy")
    os.system("{} {}".format(scrcpy_path, " ".join(args)))
    pass


@cli.command("config")
@click.option(
    "-r", "--reset", "reset", is_flag=True, help="Reset the configuration files"
)
def _config(reset=False):
    """View / Edit the configuration file"""
    config_manager = InterfaceConfig(load=False)
    if reset:
        config_manager.reset_config()
        click.echo("Configuration file resetted successfully.")
        sys.exit(0)
    config_manager.load_config()
    print(config_manager)


@cli.command()
def fast_init():
    """Init scrcpy before guiscrcpy"""
    cfgmgr = InterfaceConfig()
    print(cfgmgr)


if __name__ == "__main__":
    cli()

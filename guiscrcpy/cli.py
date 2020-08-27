import os
import platform
import sys

import click
import colorama

from .lib.utils import format_colors as fc
from .launcher import bootstrap
from .lib.check import AndroidDebugBridge
from .lib.config import InterfaceConfig
from .version import VERSION
from . import __doc__ as lic


# initialize colorama on Windows systems
colorama.init()


def show_version(ctx, param, value):
    """Prints the version of the utility"""
    if not value or ctx.resilient_parsing:
        return
    click.echo(fc('{g}guiscrcpy {rst}v{v}', v=VERSION))
    if os.getenv('APPIMAGE'):
        click.echo("Running from AppImage")
    if os.getenv('APPDIR'):
        click.echo("AppDir: {}".format(os.getenv('APPDIR')))
    import inspect
    from PyQt5 import Qt
    _pyqt5_version = [
        '%s = %s' % (k, v) for k, v in
        vars(Qt).items() if
        k.lower().find('version') >= 0 and not inspect.isbuiltin(v)
    ]
    print()
    print("== PyQt5 Version ==")
    print('\n'.join(sorted(_pyqt5_version)))
    print()
    if platform.system() == "Linux":
        print("== CairoSVG version ==")
        from cairosvg import VERSION as CAIRO_VERSION  # noqa:
        print("CairoSVG == {}".format(CAIRO_VERSION))
        print()

    ctx.exit()


def show_license(ctx, param, value):
    """Prints the license of the utility"""
    if not value or ctx.resilient_parsing:
        return
    click.echo(lic)
    ctx.exit()


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--version', is_flag=True,
              callback=show_version,
              expose_value=False, is_eager=True)
@click.option('--license', '--lic', is_flag=True,
              callback=show_license,
              expose_value=False, is_eager=True)
@click.option('-T',
              '--theme', 'theme',
              default='Breeze',
              help="Set the default theme (based on PyQt5 "
                   "themes - Fusion, Breeze, Windows) "
                   "(stored in configuration, override by --theme-no-cfg)")
@click.option('-W',
              '--hide-wm-frame/--show-wm-frame',
              'hide_wm_frame',
              default=True,
              help="Show window manager border frame.")
@click.option('--debug-disable-scrcpy',
              'debug__disable_scrcpy',
              default=False, is_flag=True,
              help="Do not launch scrcpy even when 'Start Scrcpy' is pressed")
@click.option('-A', '--always-on-top/--disable-always-on-top', 'aot',
              default=True, help="Forces the panels to be always of top")
def cli(ctx, hide_wm_frame=True, aot=True, theme='Breeze',
        debug__disable_scrcpy=False):
    """ guiscrcpy: Graphical user interface for scrcpy"""
    print(fc("\n{b}guiscrcpy {v}{rst}", v=VERSION))
    print(fc("by @srevinsaju"))
    print(fc("{x}https://github.com/srevinsaju/guiscrcpy{rst}\n\n"))
    if ctx.invoked_subcommand is not None:
        return
    cfgmgr = InterfaceConfig()
    bootstrap(cfgmgr, theme=theme, aot=aot, hide_wm_frame=hide_wm_frame,
              debug__no_scrcpy=debug__disable_scrcpy)


@cli.command()
@click.option('--device-id', 'device_id',
              help="Sets the device-id for mapper to configure "
                   " (optional, needed for multiple devices)")
@click.option('-r', '--reset', 'reset', is_flag=True,
              help="Reset guiscrcpy's mapper configuration file")
def mapper(device_id=None, reset=False):
    """Run the guiscrcpy mapper"""
    cfgmgr = InterfaceConfig()
    config = cfgmgr.get_config()
    mapper_cfg_path = os.path.join(
        cfgmgr.get_cfgpath(), 'guiscrcpy.mapper.json'
    )
    if reset:
        # A ternary version of removing a file if it exists
        # https://stackoverflow.com/q/10840533/
        mapper_configuration_file_exists = os.remove(mapper_cfg_path) if \
            os.path.exists(mapper_cfg_path) else None
        if mapper_configuration_file_exists:
            print("guiscrcpy mapper configuration file has been removed.")
            print("Removed {}".format(mapper_configuration_file_exists))
        else:
            print("guiscrcpy mapper configuration is not created yet.")
        return

    if os.getenv('GUISCRCPY_ADB'):
        adb_path = os.getenv('GUISCRCPY_ADB')
    else:
        adb_path = config['adb']
    adb = AndroidDebugBridge(adb_path)
    adb_devices_list = adb.devices()
    if len(adb_devices_list) == 0:
        print("E: No devices found")
        sys.exit(1)
    elif len(adb_devices_list) == 1:
        mapper_device_id = adb_devices_list[0][0]
    elif not device_id:
        print("Please pass the --device-id <device_id> to initialize "
              "the mapper")
        sys.exit(1)
    else:
        mapper_device_id = device_id

    from guiscrcpy.lib.mapper.mapper import Mapper
    # Initialize the mapper if it is called.
    adb = AndroidDebugBridge(path=cfgmgr.get_config().get('adb'))
    mp = Mapper(mapper_device_id, adb=adb, config_path=mapper_cfg_path)
    if not os.path.exists(
            os.path.join(cfgmgr.get_cfgpath(), 'guiscrcpy.mapper.json')):
        print("guiscrcpy.mapper.json does not exist. ")
        print("Initializing Mapper Configuration for the first time use.")
        mp.initialize(initialize_qt=True)
    else:
        mp.read_configuration()
        print("guiscrcpy.mapper.json found. Starting the mapper...")
        print("Your keyboard is being listened by guiscrcpy-mapper")
        print("pressing any key will trigger the position.")
        print()
        print('If you would like to register new keys, pass --mapper-reset')
        print("\nInitializing\n\n")
        mp.listen_keypress()
        print("Done!")


@cli.command('adb')
@click.argument('args', nargs=-1)
def adb_cli(args):
    """Create an interface with the Android Debugging bridge"""
    cfgmgr = InterfaceConfig()
    config = cfgmgr.get_config()
    if os.getenv('GUISCRCPY_ADB'):
        adb_path = os.getenv('GUISCRCPY_ADB')
    else:
        adb_path = config['adb']
    print("Interfacing guiscrcpy-adb")
    os.system('{} {}'.format(adb_path, ' '.join(args)))
    pass


@cli.command()
@click.argument('args', nargs=-1)
def scrcpy(args):
    """Create an interface with scrcpy"""
    cfgmgr = InterfaceConfig()
    config = cfgmgr.get_config()
    if os.getenv('GUISCRCPY_SCRCPY'):
        scrcpy_path = os.getenv('GUISCRCPY_SCRCPY')
    else:
        scrcpy_path = config['scrcpy']
    print("Interfacing guiscrcpy-scrcpy")
    os.system('{} {}'.format(scrcpy_path, ' '.join(args)))
    pass


@cli.command('config')
@click.option('-r', '--reset', 'reset', is_flag=True,
              help="Reset the configuration files")
def _config(reset=False):
    """View / Edit the configuration file"""
    cfgmgr = InterfaceConfig()
    if reset:
        cfgmgr.reset_config()
        click.echo("Configuration file resetted successfully.")
        sys.exit(0)
    print(cfgmgr)


@cli.command()
def fast_init():
    """Init scrcpy before guiscrcpy"""
    cfgmgr = InterfaceConfig()
    print(cfgmgr)


if __name__ == "__main__":
    cli()

#!/usr/bin/env python3

import os,sys
import subprocess
import platform

def check_snap():
    if platform.platform()=="Linux":

        """Check if inside a snap"""

        if 'SNAP_COMMON' in os.environ:
            print ('running in a snap')
            return True
        return False
    else:
        return False

def add_path():
    """Add home dir to path for accessing tools from a snap"""
    
    toolspath = os.environ['SNAP_COMMON']
    #toolspath = os.path.join(home, 'tools')
    binpath = os.path.join(toolspath, 'bin')
    #if not os.path.exists(toolspath):
    print ('you should install external tools in %s' %toolspath)
    os.environ["PATH"] += os.pathsep + binpath
    print (os.environ["PATH"])
    return

def run_test():
    print(__file__)
    if(platform.platform()=="Windows"):
            print("DETECTED OS :: WINDOWS")
            pythonexec = "python"
    else:
            print("DETECTED OS :: *NIX")
            pythonexec = "python3"

    filename = str(__file__)[:-(len("app.py"))]
    os.chdir(str(os.path.abspath(__file__)[:-len("app.py")]))
    cmd = pythonexec + ' __main__.py'
    tmp = subprocess.Popen(cmd, shell=True)
    
    return

def main():
    "Run the application"

    if check_snap() is True:
        add_path()
    print ('Hello!')
    run_test()

if __name__ == '__main__':
    main()



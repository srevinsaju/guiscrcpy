import logging
import os
from guiscrcpy.platform.platform import System
environment = System()


def decode(raw_output):
    pass


def decode_process(process):
    try:
        output = process.stdout.readlines()
        for i in range(len(output)):
            output[i] = output[i].decode('utf-8')
    except NameError:
        logging.error("No stdout in process.")
        output = ""
    return output


def check_existence(paths, file=(), directory=True, PATH=False):
    for i in paths:
        j = os.path.expanduser(i)
        if os.path.exists(j):  # direcory exists
            if directory and os.path.isdir(j):
                return [j]
            else:
                if (type(file) is list) or (type(file) is tuple):
                    for exe in file:
                        if os.path.exists(os.path.join(j, exe)):
                            return [os.path.join(j, exe)]
                else:

                    if os.path.exists(os.path.join(j, file)):
                        return [os.path.join(j, file)]
        else:
            logging.debug("{} doesn't exist".format(i))

    if PATH:
        new_paths = os.getenv('PATH').split(os.pathsep)
        found_path = check_existence(
            new_paths, file=file, directory=directory, PATH=False)
        if found_path:
            return [found_path, 'path']
        else:
            return False
    else:
        return False

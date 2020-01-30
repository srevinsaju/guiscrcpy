from guiscrcpy.platform.platform import System
environment = System()


class termcolors:
    if environment.system() == "Linux":
        HEADER = "\033[95m"
        OKBLUE = "\033[94m"
        OKGREEN = "\033[92m"
        WARNING = "\033[93m"
        FAIL = "\033[91mERR:"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
    else:
        HEADER = ""
        OKBLUE = ""
        OKGREEN = ""
        WARNING = ""
        FAIL = "ERR:"
        ENDC = ""
        BOLD = ""
        UNDERLINE = ""

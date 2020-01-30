from guiscrcpy.theme.termcolor import termcolors


class header:
    def __init__(self, commit):
        print(
            termcolors.UNDERLINE +
            "                                  " +
            termcolors.ENDC)
        print()
        print("guiscrcpy")
        print("by srevinsaju")
        print(termcolors.OKBLUE + commit + termcolors.ENDC)
        print(
            termcolors.OKBLUE +
            "Licensed under GNU GPL v3 (c) 2019  " +
            termcolors.ENDC)
        print(
            termcolors.UNDERLINE +
            "                                  " +
            termcolors.ENDC)
        print(termcolors.OKBLUE + "" + termcolors.ENDC)

        print()
        print(
            "MSG: Please ensure you have enabled",
            termcolors.OKGREEN + "USB Debugging" + termcolors.ENDC,
            "on your device. See README.md for more details",
        )

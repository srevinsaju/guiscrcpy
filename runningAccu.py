import psutil

import main


def checkProcessRunning(processName):
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


if checkProcessRunning("scrcpy"):
    main.MyApp.__init__(self).self.setupUi(self).runningNot.setStyleSheet("background-color: green")
else:
    main.__init__().MyApp.runningNot.setStyleSheet("background-color: red")

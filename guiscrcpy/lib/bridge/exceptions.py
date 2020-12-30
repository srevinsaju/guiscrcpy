class ScrcpyNotFoundError(FileNotFoundError):
    pass


class ScrcpyServerNotFoundError(FileNotFoundError):
    pass


class AdbNotFoundError(FileNotFoundError):
    pass


class AdbRuntimeError(RuntimeError):
    pass

import shutil


from ...install.finder import open_exe_name_dialog


class Bridge:
    name = None

    def __init__(self, path=None):
        if path is not None:
            self.path = path
        elif shutil.which(self.name):
            self.path = shutil.which(self.name)
        else:
            self.path = open_exe_name_dialog(None, self.name)
        if self.path is None:
            raise FileNotFoundError(f"Could not find '{self.name}' on $PATH.")
        self.post_init()

    def post_init(self):
        pass

    def get_path(self):
        return self.path

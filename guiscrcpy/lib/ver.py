__version__ = '2.0-raw'
import logging
try:
    import git
except ModuleNotFoundError:
    logging.warning('GitPython not installed. Fallback to pip3 version reading')
    git = None

class version:
    def __init__(self):
        self.sha = None

        if self.get_repo():
            pass
        elif self.get_pip_version():
            pass
        else:
            pass

        self.build = self.version + " by srevinsaju"
        if not self.sha:
            self.commit = self.version
        else:
            self.commit = self.version + ":" + self.sha

    def get_pip_version(self):
        try:
            import pkg_resources
            self.version = pkg_resources.get_distribution(
                "guiscrcpy").version
            return True
        except BaseException:
            logging.warning("guiscrcpy not installed as pip package." +
                            "Version retrieve failed.")
            self.version = __version__
            return False

    def get_repo(self):
        if git:
            try:
                repo = git.Repo(search_parent_directories=True)
            except git.exc.InvalidGitRepositoryError:
                return False

            self.sha = "-" + repo.head.object.hexsha
            if not repo.git.describe("--tags").startswith('0.'):
                self.version = repo.git.describe("--tags")
            else:
                self.version = __version__
            return True
        else:
            return False

    def get_version(self):
        return  self.version

    def get_commit(self):
        return self.commit

    def get_sha(self):
        if self.sha:
            return self.sha
        else:
            return ''


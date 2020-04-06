"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


__version__ = '3.4-raw'
import logging
try:
    import git
except ModuleNotFoundError:
    logging.warning(
        'GitPython not installed. Fallback to pip3 version reading')
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
        return self.version

    def get_commit(self):
        return self.commit

    def get_sha(self):
        if self.sha:
            return self.sha
        else:
            return ''

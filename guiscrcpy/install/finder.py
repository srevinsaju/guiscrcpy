from qtpy.QtWidgets import QFileDialog
from qtpy.QtCore import QDir


def open_exe_name_dialog(parent, appname):
    options = QFileDialog.Options()
    options |= QDir.AllEntries
    options |= QDir.Hidden

    file_dialog = QFileDialog()
    file_dialog.setFilter(QDir.AllEntries | QDir.Hidden)
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setWindowTitle(
        f"{appname} could not be found. Please locate in" "manually"
    )
    if file_dialog.exec():
        file_name = file_dialog.selectedFiles()
        print(file_name[0])
        return file_name[0]
    else:
        print("No file is selected. guiscrcpy is likely to fail")

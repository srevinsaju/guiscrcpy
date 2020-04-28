from PyQt5.QtWidgets import QFileDialog


def open_exe_name_dialog(parent, appname):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_name, _ = \
        QFileDialog.getOpenFileName(
            parent,
            "{} could not be found. Please locate it manually".format(appname),
            "",
            "Valid {} executable (*);;".format(appname),
            options=options
        )
    if file_name:
        print(file_name)
        return file_name
    else:
        print("No file is selected. guiscrcpy is likely to fail")

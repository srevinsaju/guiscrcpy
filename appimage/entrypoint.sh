export LD_LIBRARY_PATH="${APPDIR}/usr/lib:${LD_LIBRARY_PATH}"
export GUISCRCPY_SCRCPY="${APPDIR}/usr/bin/scrcpy"
export GUISCRCPY_ADB="${APPDIR}/usr/bin/adb"
export ADB="${APPDIR}/usr/bin/adb"
export SCRCPY_SERVER_PATH="${APPDIR}/usr/share/scrcpy/scrcpy-server"
export PATH="${APPDIR}/usr/bin:${PATH}"
export GUISCRCPY_APPIMAGE="TRUE"

{{ python-executable }} -s ${APPDIR}/opt/python{{ python-version }}/bin/guiscrcpy "$@"

export GUISCRCPY_SCRCPY="${APPDIR}/usr/bin/scrcpy"
export GUISCRCPY_ADB="${APPDIR}/usr/bin/adb"
export SCRCPY_SERVER_PATH="${APPDIR}/usr/local/share/scrcpy/scrcpy-server"
export ADB="${APPDIR}/usr/bin/adb"
export GUISCRCPY_APPIMAGE=True
export PATH="${APPDIR}/usr/bin:${PATH}"
export SCRCPY_LDD="${APPDIR}/usr/libscrcpy"

"{{ python-executable }}" -s "${APPDIR}/opt/python{{ python-version }}/bin/guiscrcpy" "$@"

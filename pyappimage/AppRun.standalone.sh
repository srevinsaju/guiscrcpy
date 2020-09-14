#! /bin/bash

# Export APPRUN if running from an extracted image
self="$(readlink -f -- $0)"
here="${self%/*}"
APPDIR="${APPDIR:-${here}}"

export PYAPPIMAGE="TRUE"

export QT_API=pyside2
export GUISCRCPY_STANDALONE=true
export GUISCRCPY_APPIMAGE=True
${APPDIR}/guiscrcpy/guiscrcpy $@


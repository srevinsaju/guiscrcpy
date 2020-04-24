export PATH="${APPDIR}/usr/bin:${PATH}"

{{ python-executable }} -s ${APPDIR}/opt/python{{ python-version }}/bin/guiscrcpy "$@"

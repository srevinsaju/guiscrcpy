# Choose the correct python and virtualenv commands:

PYTHON      := python
SPHINXBUILD := sphinx-build

# If `python3` exists:
ifeq (1,$(shell python3 -c "print(1)" 2>&- ))
PYTHON      := python3
endif

PYTHON35    := python3
# If we are on cygwin:
ifeq (1,$(shell /cygdrive/c/Program\ Files/Python37/python.exe -c "print(1)" 2>&- ))
PYTHON      := /cygdrive/c/Program\ Files/Python37/python.exe
PYTHON37    := /cygdrive/c/Program\ Files/Python37/python.exe
endif

ifneq ($(EUID),0)
INSTALL_OPTS += "--user"
endif


export PYTHON # pass the variable to sub-makefiles through the environment

default: pyuic5

pyuic5:
	pyrcc5 guiscrcpy/ui/rsrc.qrc -o guiscrcpy/ui/pyqt5/rsrc_rc.py
	pyuic5 guiscrcpy/ui/mainwindow.ui -o guiscrcpy/ui/pyqt5/main.py --from-imports
	pyuic5 guiscrcpy/ui/downloader.ui -o guiscrcpy/ui/pyqt5/downloader.py --from-imports
	pyuic5 guiscrcpy/ui/bottompanelui.ui -o guiscrcpy/ui/pyqt5/panel.py --from-imports
	pyuic5 guiscrcpy/ui/toolkit_ui.ui -o guiscrcpy/ui/pyqt5/toolkit.py --from-imports
	pyuic5 guiscrcpy/ui/network.ui -o guiscrcpy/ui/pyqt5/network.py --from-imports
	pyuic5 guiscrcpy/ui/settings.ui -o guiscrcpy/ui/pyqt5/settings.py --from-imports
	rm guiscrcpy/theme/desktop_shortcut.py
	echo '#!/usr/bin/env/python\n' > guiscrcpy/theme/desktop_shortcut.py
	echo '# flake8: noqa' >> guiscrcpy/theme/desktop_shortcut.py
	echo 'def desktop_device_shortcut_svg():' >> guiscrcpy/theme/desktop_shortcut.py
	printf '    a="""' >> guiscrcpy/theme/desktop_shortcut.py
	cat guiscrcpy/ui/ui/guiscrcpy_shortcut.svg >> guiscrcpy/theme/desktop_shortcut.py
	echo '"""' >> guiscrcpy/theme/desktop_shortcut.py
	echo '    return a' >> guiscrcpy/theme/desktop_shortcut.py
	sed -i 's/#ffdc00/{}/g' guiscrcpy/theme/desktop_shortcut.py
	cp ./README.md docs/README.md
	sed -i 's/docs\// /g' docs/README.md

pysideuic:
	rcc --generator=python guiscrcpy/ui/rsrc.qrc -o guiscrcpy/ui/pyside2/rsrc_rc.py
	uic --generator=python guiscrcpy/ui/mainwindow.ui -o guiscrcpy/ui/pyside2/main.py --from-imports
	uic --generator=python guiscrcpy/ui/downloader.ui -o guiscrcpy/ui/pyside2/downloader.py --from-imports
	uic --generator=python guiscrcpy/ui/bottompanelui.ui -o guiscrcpy/ui/pyside2/panel.py --from-imports
	uic --generator=python guiscrcpy/ui/toolkit_ui.ui -o guiscrcpy/ui/pyside2/toolkit.py --from-imports
	uic --generator=python guiscrcpy/ui/network.ui -o guiscrcpy/ui/pyside2/network.py --from-imports
	uic --generator=python guiscrcpy/ui/settings.ui -o guiscrcpy/ui/pyside2/settings.py --from-imports
	sed -i '/from PySide2.QtWidgets import */ifrom PySide2.QtGui import QGradient' guiscrcpy/ui/pyside2/main.py
	sed -i 's/self.verticalLayout.setSpacing(0())/self.verticalLayout.setSpacing(0)/g' guiscrcpy/ui/pyside2/toolkit.py
	sed -i 's/self.verticalLayout.setMargin(0())/self.verticalLayout.setMargin(0)/g' guiscrcpy/ui/pyside2/toolkit.py
	rm guiscrcpy/theme/desktop_shortcut.py
	echo '#!/usr/bin/env/python\n' > guiscrcpy/theme/desktop_shortcut.py
	echo '# flake8: noqa' >> guiscrcpy/theme/desktop_shortcut.py
	echo 'def desktop_device_shortcut_svg():' >> guiscrcpy/theme/desktop_shortcut.py
	printf '    a="""' >> guiscrcpy/theme/desktop_shortcut.py
	cat guiscrcpy/ui/ui/guiscrcpy_shortcut.svg >> guiscrcpy/theme/desktop_shortcut.py
	echo '"""' >> guiscrcpy/theme/desktop_shortcut.py
	echo '    return a' >> guiscrcpy/theme/desktop_shortcut.py
	sed -i 's/#ffdc00/{}/g' guiscrcpy/theme/desktop_shortcut.py
	cp ./README.md docs/README.md
	sed -i 's/docs\// /g' docs/README.md

install: 
	$(PYTHON) setup.py install --user
	rm -f -R build

clean:
	rm -f *~ *.pyc *.tgz *.pyo
	rm -rf dist .coverage
	rm -f -R guiscrcpy.egg-info
	rm -f -R build
	find . -type d -path ".*/__pycache__" -print0 | xargs -0 rm -rf
	rm -f guiscrcpy/*~ guiscrcpy/*.pyc


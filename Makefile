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

ifdef LEVEL
INSTALL_OPTS += "$(LEVEL)"
endif

export PYTHON # pass the variable to sub-makefiles through the environment

default: uic

uic: 
	pyrcc5 guiscrcpy/ui/rsrc.qrc -o guiscrcpy/ui/rsrc_rc.py
	pyuic5 guiscrcpy/ui/mainwindow.ui -o guiscrcpy/ui/main.py --from-imports
	pyuic5 guiscrcpy/ui/downloader.ui -o guiscrcpy/ui/downloader.py --from-imports
	pyuic5 guiscrcpy/ui/bottompanelui.ui -o guiscrcpy/ui/panel.py --from-imports
	pyuic5 guiscrcpy/ui/toolkit_ui.ui -o guiscrcpy/ui/toolkit.py --from-imports
	pyuic5 guiscrcpy/ui/network.ui -o guiscrcpy/ui/network.py --from-imports
	pyuic5 guiscrcpy/ui/settings.ui -o guiscrcpy/ui/settings.py --from-imports
	
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


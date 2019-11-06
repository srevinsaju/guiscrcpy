import guiscrcpy
patz = list(guiscrcpy.__path__)[0]
import re
import sys
sys.path.append(patz)
sys.path.append('')
# print("PATH: ", sys.path)
from guiscrcpy import __main__
import os
os.chdir(patz)

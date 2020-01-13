import os
from guiscrcpy import __main__
import sys
import re
import guiscrcpy
patz = list(guiscrcpy.__path__)[0]
sys.path.append(patz)
sys.path.append('')
# print("PATH: ", sys.path)
os.chdir(patz)

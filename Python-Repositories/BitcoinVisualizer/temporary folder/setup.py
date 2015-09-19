__author__ = 'crispus'

import cx_Freeze
import sys
import matplotlib

base= None

if sys.platform == 'win32':
    base = "win32GUI"
executables = [cx_Freeze.Executable("tkinter tut.py", base = base)]

cx_Freeze.setup(
    name = "SeaofBTC-Client",
    options = {"build_exe": {"packages":["tkinter","matplotlib"]}},
    version = "0.01",
    description = "sea of BTC trading App",
    executables = executables
    )




import sys
import time
import os
from pystyle import *


class py2bat:
    def __init__(self) -> None:
        self.py2bat()

    def py2bat(self):
        # Code for creating the BAT file goes here
        start_code = """
0<0# : ^
'''
@echo off
echo batch
python "%~f0" %*
exit /b 0
'''
"""
        if len(sys.argv) < 2:
            print("Please provide the filename of the Python script as an argument!")
            time.sleep(3)
            os._exit(1)
        filename = sys.argv[1]
        if not filename.endswith(".py"):
            filename += ".py"
        python_code = os.path.join(os.getcwd(), filename)
        if not os.path.isfile(python_code):
            print("File does not exist!")
            time.sleep(3)
            os._exit(1)
        bat_filename = os.path.splitext(filename)[0] + ".bat"
        with open(python_code, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
        with open(bat_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(start_code + data)

py2bat()

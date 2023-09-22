import os
import hashlib

#os.system(r'C:\ransomtesting\internals\procmon.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys
import threading

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
#hide()
import time

def readmbr3():
    print 'inside readmbr'
    try:
        os.system(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula C:\ransomtesting\internals\dd.exe if=\\.\PhysicalDrive0 of=C:\ransomtesting\internals\s3.exe bs=1M count=5')
    except:
        pass 

def readmbr():
    print 'inside readmbr'
    try:
        os.system(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula C:\ransomtesting\internals\dd.exe if=\\.\PhysicalDrive0 of=C:\ransomtesting\internals\s1.exe bs=1M count=5')
    except:
        pass 

def writembr():
    print 'inside write mbr'
    try:
        os.system(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula C:\ransomtesting\internals\dd.exe if=C:\ransomtesting\internals\s1.exe of=\\.\PhysicalDrive0 bs=1M count=5')
    except:
        pass 

def monitormbr():
    while True:
        print 'inside monitoring'
        try:
            os.system(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula C:\ransomtesting\internals\dd.exe if=\\.\PhysicalDrive0 of=C:\ransomtesting\internals\s2.exe bs=1M count=5')
        except:
            pass 
        time.sleep(5)
        
        hashfile1=hashlib.md5(open(r'C:\ransomtesting\internals\s1.exe', 'rb').read()).hexdigest()
        hashfile2=hashlib.md5(open(r'C:\ransomtesting\internals\s2.exe', 'rb').read()).hexdigest()
        print hashfile1,hashfile2
        readmbr3()
        hashfile3=hashlib.md5(open(r'C:\ransomtesting\internals\s3.exe', 'rb').read()).hexdigest()
        print hashfile3
        raw_input('go again1..')
        if hashfile1!=hashfile2:
            print 'hash doesnot match'
            writembr()
            time.sleep(5)
            readmbr()
        else:
            print 'hash matches'
            time.sleep(2)
        raw_input('go again2..')

    


if __name__ == '__main__':
    freeze_support()
    """
    while True:
        print 'in 1st while loop'
        if os.path.exists(r'C:\ransomtesting\internals\whitembr.exe')==True: 
            print 'monitoring mbr'
            monitormbr()
            pass
        else:
            print 'reading mbr..'
            readmbr()
            f=open(r'C:\ransomtesting\internals\whitembr.exe','w')
            f.close()
            pass
    """

    readmbr()
    readmbr3()
    hashfile1=hashlib.md5(open(r'C:\ransomtesting\internals\s1.exe', 'rb').read()).hexdigest()
    hashfile2=hashlib.md5(open(r'C:\ransomtesting\internals\s3.exe', 'rb').read()).hexdigest()
    print hashfile1
    print hashfile2

    






    
import os

#os.system(r'C:\ransomtesting\internals\procmon.exe /AcceptEula /Quiet /Minimized /BackingFile testhhhaaaiii')
from multiprocessing import Process, freeze_support

import multiprocessing
import time
import sys

def daemonserv():
    os.system(r'C:\ransomtesting\internals\procmon.exe /AcceptEula /Quiet /Minimized /BackingFile C:\ransomtesting\internals\test')

def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True
hide()
import time

if __name__ == '__main__':
    freeze_support()
    #time.sleep(30) # for ransometestingreal2.exe to delete pending files on restart
    
    #######################################################################################
    import psutil
    import time
    process_name = "ransomtestingreal2.exe" 

    gotransomrr2=0
    def findransomtestingreal2():
        global gotransomrr2
        for proc in psutil.process_iter(): 
            process = psutil.Process(proc.pid)# Get the process info using PID
            pname = process.name()# Here is the process name
            #print pname
            #print pname,proc.pid
            #time.sleep(1)
            
            if pname == process_name: 
                gotransomrr2=1
            else:
                #print ("Dont have")
                pass

    while True:
        findransomtestingreal2()
        if gotransomrr2==1:
            time.sleep(5)
            break
        else:
            time.sleep(10)
            pass
    time.sleep(10)
    #############################################################################################




    sys.exit(0)
    from glob import glob
    a=glob(r"C:\ransomtesting\internals\*")
    listofresource=[r'C:\ransomtesting\internals'+os.sep+'ransomtestingreal.exe',r'C:\ransomtesting\internals'+os.sep+'startautorunsc.exe',\
    r'C:\ransomtesting\internals'+os.sep+'autorunsc.exe',r'C:\ransomtesting\internals'+os.sep+'sysmon64.exe',\
    r'C:\ransomtesting\internals'+os.sep+'procmon.exe',r'C:\ransomtesting\internals'+os.sep+'handle64.exe',\
    r'C:\ransomtesting\internals'+os.sep+'checkcrypto.exe',r'C:\ransomtesting\internals'+os.sep+'ransomtestingreal2.exe',\
    r'C:\ransomtesting\internals'+os.sep+'nssm.exe',r'C:\ransomtesting\internals'+os.sep+'procserv.exe',r'C:\ransomtesting\internals'+os.sep+'procstop.exe',\
    r'C:\ransomtesting\internals'+os.sep+'procprocess.exe',r'C:\ransomtesting\internals'+os.sep+'autoprocess.exe']
    for i in a:
        print i
        if os.path.isdir(i)==False:
            deletei=0
            for ku in listofresource:
                try:
                    i.index(ku)
                    deletei=1
                except:
                    pass
            if deletei==0:
                #os.system('del /F /Q /A '+i), deactivated for now, will check later
                pass

    print 'starting procmon...'
    try:
        os.system(r'C:\ransomtesting\internals\procmon.exe /AcceptEula /Quiet /Minimized /BackingFile C:\ransomtesting\internals\test')
        print 'Procmon started'
    except Exception as ex:
        print ex
    #d = multiprocessing.Process(name='daemonserv', target=daemonserv)
    #d.daemon = True



    #d.start()
    #time.sleep(1)
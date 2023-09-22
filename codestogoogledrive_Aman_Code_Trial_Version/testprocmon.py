import os
import time
import sys
import ctypes
import threading

raw_input('procmon.exe keep in same path.. ')

os.chdir(r'C:\ransomtesting\internals')
flagtorun=1


timetoexit=0
def terminateprocmon():
    os.system(r'procmon.exe /Terminate')


def startprocmon():
    global flagtorun
    while True:
        if flagtorun==1:
            os.chdir(r'C:\ransomtesting\internals')
            #os.system(r'rocmon.exe /AcceptEula /Quiet /Minimized /BackingFile test /Runtime 10')
            os.system(r'procmon.exe /AcceptEula /Quiet /Minimized /BackingFile test ')
            time.sleep(2)
            print 'procmon running'
        else:
            print 'procmon stopped'
            break
    print 'out of while loop startprocmon..'


def convertpml2csv():
    global timetoexit
    os.chdir(r'C:\ransomtesting\internals')
    os.system(r'procmon.exe /AcceptEula /Quiet /Minimized /OpenLog test.pml /SaveAs test.csv')
    timetoexit=1
    sys.exit(0)


def monitorfile():
    global flagtorun,timetoexit
    while True:
        time.sleep(2)
        if os.path.exists(r'C:\Users\Hemant\Desktop\1aaa_crypto.txt')==False:
            time.sleep(2)
            # todo check procmon is running , else wait for procmon to run
            flagtorun=0
            terminateprocmon()
            #convertpml2csv()
            timetoexit=1
            sys.exit(0)
            break
        else:
            print 'File present'

def exitme():
    global timetoexit
    while True:
        time.sleep(10)
        if timetoexit==1:
            print 'Exiting....'
            sys.exit(0)

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        if self.name=='monitorfile':
            monitorfile()
        if self.name=='startprocmon':
            startprocmon()

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "monitorfile", 5)
thread2 = myThread(2, "startprocmon", 6)


# Start new Threads
thread1.start()
thread2.start()


# Add threads to thread list
threads.append(thread1)
threads.append(thread2)


# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"
raw_input('keep malwaredeinfection in same place..')
os.system('malwaredeinfection.exe')
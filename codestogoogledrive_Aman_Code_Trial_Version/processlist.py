import psutil
import time
process_name = "Roadblock_desktop.exe" 
for proc in psutil.process_iter(): 
    process = psutil.Process(proc.pid)# Get the process info using PID
    pname = process.name()# Here is the process name
    #print pname
    #print pname,proc.pid
    #time.sleep(1)
    
    if pname == process_name: 
        print ("have") 
        print pname,proc.pid
    else:
        #print ("Dont have")
        pass
    
searchitem='drpbx'

processidtodelete=[]
processname=[]

getparentname=''
import os
count=1
def processme2tree(line):
    global searchitem,processname,processidtodelete,getparentname,count
    splitinfo=line.split('_$#_')
    foundsearchitem=0
    if count==1:
        kl=splitinfo[1]
        try:
            kl.index(searchitem)
            foundsearchitem=1
        except:
            pass
    elif count==0:
        kl=splitinfo[0]
        try:
            if kl==searchitem:
                foundsearchitem=1
        except:
            pass
    if foundsearchitem==1 and count==1: # first time
        processidtodelete.append(splitinfo[0])
        processname.append(splitinfo[1])
        processidtodelete.append(splitinfo[2])
        processname.append(splitinfo[3])
        #getparentname=splitinfo[3]
        #getparentname=getparentname.split(os.sep)# this get the name
        #getparentname=getparentname[len(getparentname)-1]
        getparentname=splitinfo[2] # its better to get the parent id
        searchitem=getparentname
        #print '---------------------------------------'
        #print line
        #print '-----'
        #print searchitem
        #print '------------'
        #print processname
        #print '-------------------'
        #print processidtodelete
        #print '----------------------------'
        #print splitinfo
        #print '-----------------------------------'
        
        ##raw_input(' ')
        count=0
    elif foundsearchitem==1 and count==0: # second time n going..
        #processidtodelete.append(splitinfo[0])
        #processname.append(splitinfo[1])
        processidtodelete.append(splitinfo[2])
        processname.append(splitinfo[3])
        #getparentname=splitinfo[3]
        #getparentname=getparentname.split(os.sep)# this get the name
        #getparentname=getparentname[len(getparentname)-1]
        getparentname=splitinfo[2] # its better to get the parent id
        searchitem=getparentname
        #print '---------------------------------------'
        #print line
        #print '-----'
        #print searchitem
        #print '------------'
        #print processname
        #print '-------------------'
        #print processidtodelete
        #print '----------------------------'
        #print splitinfo
        #print '-----------------------------------'
        ##raw_input(' ')
    ##print searchitem




for line in reversed(open("sysmonxml.txt").readlines()):
    processme2tree(line.rstrip())
print processname
print processidtodelete


"""
2884_$#_C:\Windows\System32\dllhost.exe_$#_628_$#_C:\Windows\System32\svchost.exe

''
3372_$#_C:\Windows\System32\consent.exe_$#_988_$#_C:\Windows\System32\svchost.exe

''
2140_$#_C:\Users\Hemant\AppData\Local\Drpbx\drpbx.exe_$#_3900_$#_C:\Users\Hemant\Desktop\jigsaw2.exe
"""
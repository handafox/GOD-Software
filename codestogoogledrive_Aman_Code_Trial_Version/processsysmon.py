import mmap

import contextlib

import argparse

from Evtx.Evtx import FileHeader

from Evtx.Views import evtx_file_xml_view

"""
<EventData><Data Name="UtcTime">2017-11-17 10:49:07.062</Data>
<Data Name="ProcessGuid">{de17afb2-bea3-5a0e-0000-0010e5154a00}</Data>
<Data Name="ProcessId">3916</Data>
<Data Name="Image">C:\Users\Hemant\Desktop\jigsaw2.exe</Data>
<Data Name="CommandLine">"C:\Users\Hemant\Desktop\jigsaw2.exe" </Data>
<Data Name="CurrentDirectory">C:\Users\Hemant\Desktop\</Data>
<Data Name="User">MININT-QN8U0KK\Hemant</Data>
<Data Name="LogonGuid">{de17afb2-f512-59d0-0000-002090f70500}</Data>
<Data Name="LogonId">0x000000000005f790</Data>
<Data Name="TerminalSessionId">1</Data>
<Data Name="IntegrityLevel">Medium</Data>
<Data Name="Hashes">SHA1=27D99FBCA067F478BB91CDBCB92F13A828B00859</Data>
<Data Name="ParentProcessGuid">{de17afb2-f517-59d0-0000-00104f340600}</Data>
<Data Name="ParentProcessId">2932</Data>
<Data Name="ParentImage">C:\Windows\explorer.exe</Data>
<Data Name="ParentCommandLine">C:\Windows\Explorer.EXE</Data>
"""
treestore=[]
searchfor='drpbx'
strr=''
def maketree(xml):
    global treestore,searchfor,strr
    strr=''
    #raw_input('-=-=-=')
    #print xml
    #raw_input('=-=-=-')
    dxc=xml.split('\n')
    #print dxc
    #raw_input('######')
    #dxc=xml
    gotpid=0
    for jkk in dxc:
        #rasearchw_input('44444')
        #print jkk
        #raw_input('77777')
        xml=str(jkk)
        ##print xml
        
        
        try:
            xml.index('Qualifiers')
            strr=''
            avar=xml.split('>')
            avar=avar[1].split('<')
            avar=avar[0]
            #strr=avar+'_'
            ##print xml
            ##print strr
            if avar!='1':
                #print 'next event'
                #raw_input('88888')
                continue
            else:
                gotpid=1
        except Exception as ex:
            #print ex
            #print '1'
            pass
        try:
            if gotpid==1:
                xml.index('"ProcessId')
                strr=''
                avar=xml.split('>')
                avar=avar[1].split('<')
                avar=avar[0]
                strr=avar+'_$#_'
                ##print xml
                #print strr
                #gotpid=1
                pass
        except Exception as ex:
            #print ex
            #print '2'
            #gotpid=0
            pass
        try:
            if gotpid==1:
                xml.index('"Image')
                avar=xml.split('>')
                avar=avar[1].split('<')
                avar=avar[0]
                strr=strr+avar+'_$#_'
                ##print xml
                #print strr
        except Exception as ex:
            ##print ex
            pass
        try:
            if gotpid==1:
                xml.index('ParentProcessId')
                avar=xml.split('>')
                avar=avar[1].split('<')
                avar=avar[0]
                strr=strr+avar+'_$#_'
                ##print xml
                #print strr
        except Exception as ex:
            ##print ex
            pass
        try:
            if gotpid==1:
                xml.index('ParentImage')
                avar=xml.split('>')
                avar=avar[1].split('<')
                avar=avar[0]
                strr=strr+avar
                treestore.append(strr)
                ##print xml
                #print strr
        except Exception as ex:
            ##print ex
            pass
        ##raw_input('--')



    #raw_input('----88')
    #print strr
    #raw_input('=====7')
    pass


def main():
    global treestore,searchfor
    evtxfile=r'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx'


    fv=open('sysmonxml.txt','w')

    with open(evtxfile, 'r') as f:

        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as buf:

            fh = FileHeader(buf, 0x0)

            ###print "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>"
            #fv.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>"+"\n")
            ###print "<Events>"
            #fv.write("<Events>"+"\n")

            for xml, record in evtx_file_xml_view(fh):

                ###print xml
                #fv.write(xml)
                maketree(xml)

            ###print "</Events>"
            #fv.write("</Events>")
    for tt in treestore:
        fv.write(str(tt)+'\n')
    fv.close()

if __name__ == "__main__":

    main()
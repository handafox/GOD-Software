susphandleprocess=[]
susname=[]
currentpid=''
currentname=''
f=open('handleinfectdout.txt','r')
listofusername=[]
import os
# get username folder lisitng
from glob import glob
a=glob(r"C:\Users\*")
for i in a:
  if os.path.isdir(i)==True:
    try:
      #print i
      #raw_input('---')
      if i!=r'C:\Users\All Users':
        #delete this afterwards
        try:
          i.index('hemant.g.kumar')
          i=i.replace('hemant.g.kumar','Hemant')
          listofusername.append(i)
        except:
          listofusername.append(i)
        #################
        
    except:
      pass

#print listofusername


for ju in f.readlines():
  #raw_input('--')
  #print ju
  ju=ju.strip()
  
  try:
    ju.index('---------------------------------------------')
    currentpid=''
    currentname=''
    continue
  except:
    pass

  try:
    ju.index('pid:')
    gf=ju.split(' ')
    currentpid=gf[2]
    currentname=gf[0]
  except:
    pass
  #print currentpid
  if currentpid!='':
    try:
      for uy in listofusername:
        ##print 'checking Desktop'
        #print uy
        try:
          #print uy+os.sep+'Desktop'
          ju.index(uy+os.sep+'Desktop')

          if currentpid in susphandleprocess:
            pass
          else:
            susphandleprocess.append(currentpid)
            susname.append(currentname)
            #print currentpid,currentname,ju,'1'

        except Exception as ex:
          #print ex
          pass
        ##print 'checking download'
        try:
          ju.index(uy+os.sep+'Documents')
          if currentpid in susphandleprocess:
            pass
          else:
            susphandleprocess.append(currentpid)
            susname.append(currentname)
            #print currentpid,currentname,ju,'2'
        except Exception as ex:
          #print ex
          pass
        try:
          ju.index(uy+os.sep+'Downloads')
          if currentpid in susphandleprocess:
            pass
          else:
            susphandleprocess.append(currentpid)
            susname.append(currentname)
            #print currentpid,currentname,ju,'3'
        except Exception as ex:
          #print ex
          pass
        """
        try:
          ju.index(uy)
          if currentpid in susphandleprocess:
            pass
          else:
            susphandleprocess.append(currentpid)
            susname.append(currentname)
            #print currentpid,currentname,ju,'4'
        except Exception as ex:
          #print ex
          pass
        """
    except Exception as ex:
      #print ex
      pass
    """
    try:
      ju.index('C:')
      if currentpid in susphandleprocess:
        pass
      else:
        susphandleprocess.append(currentpid)
        susname.append(currentname)
        #print currentpid,currentname,ju,'5'
    except:
      pass
    """

f.close()
print susphandleprocess
print susname








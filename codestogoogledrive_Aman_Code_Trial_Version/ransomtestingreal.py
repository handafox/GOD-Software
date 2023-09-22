import subprocess
import os
import hashlib
import time
def hide():
	import win32console,win32gui
	window = win32console.GetConsoleWindow()
	win32gui.ShowWindow(window,0)
	return True
hide()
def extractrealransomtesting():
	#return 1
	try:
		#os.system(r'C:\ransomtesting\internals\ransomtestingreal2.exe')
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\ransomtestingreal2.exe', shell=True)
	except:
		pass
	subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula   C:\ransomtesting\internals\roadblock_starter.exe', shell=True)

import win32event, win32api, winerror
from _winreg import *


def addStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name=sys.argv[0].split("\\")[-1]
    new_file_path=r'C:\ransomtesting\internals\roadblock_desktop.exe'
    print new_file_path
    #return 1
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

    key2change= OpenKey(HKEY_LOCAL_MACHINE,
    keyVal,0,KEY_ALL_ACCESS)

    SetValueEx(key2change, "Roadblock_Desktop",0,REG_SZ, new_file_path)



def setserviceforransomtesting():
	#return 1
	
	try:
		#commd=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "ransomtesting" /TR "C:\ransomtesting\ransomtestingreal2.exe"'
		# this is schtask one, trying nssm one
		commd=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "roadblock_starter" /TR "C:\ransomtesting\internals\roadblock_starter.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		os.system(commd)
		
		pass
		
	except Exception as ex:
		print ex

	time.sleep(3)
	print '11111111111111111'
	
	pass

	try:
		print "Adding roadblock_desktop to autostart"
		addStartup()
		#commd=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "ransomtesting" /TR "C:\ransomtesting\ransomtestingreal2.exe"'
		# this is schtask one, trying nssm one
		#commd=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "ransomtesting" /TR "C:\ransomtesting\internals\ransomtestingreal2.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		#os.system(commd)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\roadblock_desktop.exe', shell=True)
		#subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\roadblock_desktop.exe', shell=True)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\ransomtestingreal2.exe', shell=True)
		pass
		
	except Exception as ex:
		print ex

	print '22222222222222'
	pass

	time.sleep(3)
	"""
	try:
		commd1=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "Roadblock_conn" /TR "C:\ransomtesting\internals\Roadblock_conn.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		
		#os.system(commd1)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\Roadblock_conn.exe', shell=True)
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\Roadblock_conn.exe', shell=True)
		
	except Exception as ex:
		print ex
	time.sleep(5)
	print '3333333333333'
	pass



	try:
		commd10=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "procserv" /TR "C:\ransomtesting\internals\procserv.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		
		#os.system(commd10)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\procserv.exe', shell=True)
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\procserv.exe', shell=True)
		
	except Exception as ex:
		print ex
	time.sleep(5)
	print '44444444444444441'
	pass


	try:
		commd9=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "procdelete" /TR "C:\ransomtesting\internals\procdelete.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		
		#os.system(commd9)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\procdelete.exe', shell=True)
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\procdelete.exe', shell=True)
		
	except Exception as ex:
		print ex
	time.sleep(5)
	print '5555555555555555555'
	pass



	try:
		commd8=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "procstop" /TR "C:\ransomtesting\internals\procstop.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		#os.system(commd8)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\procstop.exe', shell=True)
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\procstop.exe', shell=True)
		
	except Exception as ex:
		print ex
	time.sleep(5)
	print '666666666666666666666'
	pass

	try:
		commd7=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "procprocess" /TR "C:\ransomtesting\internals\procprocess.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		#os.system(commd7)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\procprocess.exe', shell=True)
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\procprocess.exe', shell=True)
		
	except Exception as ex:
		print ex
	time.sleep(5)
	print '777777777777777777777777771'
	pass


	try:
		commd6=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "autoprocess" /TR "C:\ransomtesting\internals\autoprocess.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		#os.system(commd6)
		#subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\autoprocess.exe', shell=True)
		subprocess.Popen(r'C:\ransomtesting\internals\PsExec64.exe -i -d -s -accepteula  C:\ransomtesting\internals\autoprocess.exe', shell=True)
		
	except Exception as ex:
		print ex
	time.sleep(5)
	"""
	"""
	try:
		commd=r'c:\\windows\system32\SchTasks.exe /Create /RU SYSTEM /SC ONSTART /TN "procdelete" /TR "C:\ransomtesting\internals\procdelete.exe"'
		#tryying nssmone
		#commd=r'C:\ransomtesting\internals\nssm.exe install rahuketu C:\ransomtesting\internals\ransomtestingreal2.exe'

		os.system(commd)
		subprocess.Popen(r'start cmd /C C:\ransomtesting\internals\procdelete.exe', shell=True)
	except Exception as ex:
		print ex
	time.sleep(5)
	"""
	pass
	
def installsysmon():
	try:
		os.chdir(r'C:\ransomtesting\internals')
		os.system(r'sysmon64.exe -accepteula -i')
	except:
		pass

def startserviceransomtesting():
	#raw_input('For now, start the service manually.... later make it start by command prompt...')
	pass


def getautorunlist1st():
	#### here we will start a programm that starts with no window visbile, and it executes autorunsc -a * present in temp folder
	os.system(r'C:\ransomtesting\internals'+os.sep+'startautorunsc.exe') # this takes the 1stautorunlist and saved in system32 folder
	# get autorun date and time
	commdate='date /T'
	output = subprocess.check_output(commdate,shell=True)
	commtime='time /T'
	output = output.replace('\r\n','')
	output = output+'___'+subprocess.check_output(commtime,shell=True)
	output = output.replace('\r\n','')
	#print output
	try:
		os.system(r'mkdir "C:\ransomtesting"')
	except:
		pass
	f=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.exe','w')
	#f=open('C:\Windows\System32'+os.sep+'ransomtesting'+os.sep+'the1stautodatentime.exe','w')
	f.write(output)
	f.close()


def placefiles(username):

	#--- List of users Locations ---#
	try:
		#gettheusername=os.environ.get("USERNAME")
		location1=username+os.sep+'Desktop'
		location2=username+os.sep+'Documents'
		location3=username
		location4=username+os.sep+'Downloads'
		location5='C:'
	except Exception as ex:
		print ex
		sys.exit(0)

	#--- List of files with specific names to be generated ---#
	filename1="1aaa_crypto.txt"
	filename2="eee_crypto.txt"
	filename3="zzz_crypto.txt"
	filename4="99hh__crypto.txt"


	#--- Creating specific files in particular locations ---#
	try:
		f=open(location1+os.sep+filename1,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location1+os.sep+filename1)
		f=open(location1+os.sep+filename2,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location1+os.sep+filename2)
		f=open(location1+os.sep+filename3,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location1+os.sep+filename3)
		f=open(location1+os.sep+filename4,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location1+os.sep+filename4)
	except Exception as ex:
		print ex
		sys.exit(0)

	try:
		f=open(location2+os.sep+filename1,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location2+os.sep+filename1)
		f=open(location2+os.sep+filename2,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location2+os.sep+filename2)
		f=open(location2+os.sep+filename3,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location2+os.sep+filename3)
		f=open(location2+os.sep+filename4,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location2+os.sep+filename4)
	except Exception as ex:
		print ex
		sys.exit(0)


	try:
		f=open(location3+os.sep+filename1,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location3+os.sep+filename1)
		f=open(location3+os.sep+filename2,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location3+os.sep+filename2)
		f=open(location3+os.sep+filename3,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location3+os.sep+filename3)
		f=open(location3+os.sep+filename4,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location3+os.sep+filename4)
	except Exception as ex:
		print ex
		sys.exit(0)

	try:
		f=open(location4+os.sep+filename1,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location4+os.sep+filename1)
		f=open(location4+os.sep+filename2,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location4+os.sep+filename2)
		f=open(location4+os.sep+filename3,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location4+os.sep+filename3)
		f=open(location4+os.sep+filename4,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location4+os.sep+filename4)
	except Exception as ex:
		print ex
		sys.exit(0)

	try:
		f=open(location5+os.sep+filename1,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location5+os.sep+filename1)
		f=open(location5+os.sep+filename2,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location5+os.sep+filename2)
		f=open(location5+os.sep+filename3,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location5+os.sep+filename3)
		f=open(location5+os.sep+filename4,"w")
		f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
		f.close()
		os.system('attrib +h '+location5+os.sep+filename4)
	except Exception as ex:
		print ex
		sys.exit(0)

	#--- Calculating hashes and saving it in a file placed in Temp folder
	try:
		hashfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
		#hashfile2=hashlib.md5(open(location1+os.sep+filename2, 'rb').read()).hexdigest()
		
		#hashfile3=hashlib.md5(open(location1+os.sep+filename3, 'rb').read()).hexdigest()
		#hashfile4=hashlib.md5(open(location1+os.sep+filename4, 'rb').read()).hexdigest()

		try:
			os.system(r'mkdir '+r'C:\ransomtesting'+os.sep+'hashvalue')
		except:
			pass
		filewa=r"C:\ransomtesting"+os.sep+'hashvalue'+os.sep+'hashlist.exe'
		#filewa=os.environ['TEMP']+os.sep+'hashlistransomtesting.exe'
		f=open(filewa,"w")
		f.write(hashfile1)
		#f.write(hashfile2+'\n')
		#f.write(hashfile3+'\n')
		#f.write(hashfile4+'\n')
		f.close()
	except Exception as ex:
		print ex
		sys.exit(0)

	#############################################################


	pass


import os
"""
l=os.environ['TEMP']+os.sep+'outtt.exe'
print l
cmd="net session > '"+l+"'"
print cmd

os.system(cmd)
"""
########### this is not needded , so commenting...
"""
from subprocess import check_output as qx

cmd = r'C:\Windows\System32\net.exe session'

from subprocess import STDOUT
adminflag=0

try:
	output = qx(cmd, stderr=STDOUT)
	adminflag=1
except:
	pass

if adminflag==1:
	print 'I have admin privillge..'
	extractrealransomtesting()
	print 'going to set service...'
	setserviceforransomtesting()
"""
###############################################################
# directly executing the functions::::
print 'I have admin privillge..'
try:
	print 'deleting infdtc'
	os.system('del /F /Q /A '+r'C:\ransomtesting\internals'+os.sep+'infdtc.exe')
except Exception as ex:
	print ex
	pass

print 'going to set service...'
setserviceforransomtesting()
print 'going to install sysmon64...'
installsysmon()
#print 'starting the service..'
#startserviceransomtesting()
print 'getting autorunlist: remove this line afterwards...the 1st whitelist...'
getautorunlist1st()
print 'Putting files at specified locations..'
# get username folder lisitng
from glob import glob
a=glob(r"C:\Users\*")
for i in a:
	if os.path.isdir(i)==True:
		try:
			print i
			#raw_input('---')
			if i!=r'C:\Users\All Users' and i!=r'C:\Users\Default' and i!=r'C:\Users\Default User' and i!=r'C:\Users\Public':
				placefiles(i)
				print i
				#raw_input('going again..')
				pass
		except:
			pass

#print 'Executing ransomtestingreal2'
#extractrealransomtesting()

print 'Installing Drivers...'

os.system(r'rundll32 syssetup,SetupInfObjectInstallAction DefaultInstall 128 .\MBRFilter.inf')
time.sleep(3)
os.system('shutdown /r /t 00')


###############################################################

#schtasks.exe /s "\" /ru "SYSTEM" /Create /SC DAILY /MO "7" /ST "12:00" /TN "mytask" /TR "C:\test.exe "C:\"
#'c:\\windows\system32\SchTasks.exe /s "\" /ru "SYSTEM" /Create /SC ONSTART /TN "2heychecking" /TR C:\Windows\System32\ransomtestingreal2.exe'


# raw_input('exit..')
pass
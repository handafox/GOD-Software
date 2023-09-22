# I do monitoring.. that's my job.. don't disturb me..
# todo: add autorun taking functionality every 10 days
import os
import sys
import hashlib
import win32event, win32api, winerror
import string 
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


#Disallowing Multiple Instance
def createmutex():
	mutex = win32event.CreateMutex(None, 1, 'mutex_var_xbozx')
	if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
		mutex = None
		print "Multiple Instance not Allowed"
		sys.exit(0)
#raw_input('place ransomtestingcheck.exe in system32 folder..')
"""
gettheusername=os.environ.get("USERNAME")
location1='C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Desktop'
location2='C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'
location3='C:'+os.sep+'Users'+os.sep+'hemant'
location4='C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Downloads'
location5='C:'
filename1="1aaa_crypto.txt"
filename2="eee_crypto.txt"
filename3="zzz_crypto.txt"
filename4="99hh_crpto.txt"
"""

def getuptime():
	import uptime
	

def placefiles(username):
	#global location1,location2,location3,location4,location5,filename1,filename2,filename3,filename4
	#--- List of users Locations ---#
	try:
		location1=username+os.sep+'Desktop'
		location2=username+os.sep+'Documents'
		location3=username
		location4=username+os.sep+'Downloads'
		location5='C:'
	except Exception as ex:
		print ex
		##sys.exit(0)

	#--- List of files with specific names to be generated ---#
	filename1="1aaa_crypto.txt"
	filename2="eee_crypto.txt"
	filename3="zzz_crypto.txt"
	filename4="99hh_crpto.txt"


	#--- Creating specific files in particular locations ---#
	try:
		if os.path.exists(location1+os.sep+filename1)==False:
			f=open(location1+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename1)
		if os.path.exists(location1+os.sep+filename2)==False:
			f=open(location1+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename2)
		if os.path.exists(location1+os.sep+filename3)==False:
			f=open(location1+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename3)
		if os.path.exists(location1+os.sep+filename4)==False:
			f=open(location1+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location1+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	try:
		if os.path.exists(location2+os.sep+filename1)==False:
			f=open(location2+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename1)
		if os.path.exists(location2+os.sep+filename2)==False:
			f=open(location2+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename2)
		if os.path.exists(location2+os.sep+filename3)==False:
			f=open(location2+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename3)
		if os.path.exists(location2+os.sep+filename4)==False:
			f=open(location2+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location2+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)


	try:
		if os.path.exists(location3+os.sep+filename1)==False:
			f=open(location3+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename1)
		if os.path.exists(location3+os.sep+filename2)==False:
			f=open(location3+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename2)
		if os.path.exists(location3+os.sep+filename3)==False:
			f=open(location3+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename3)
		if os.path.exists(location3+os.sep+filename4)==False:
			f=open(location3+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location3+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	try:
		if os.path.exists(location4+os.sep+filename1)==False:
			f=open(location4+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename1)
		if os.path.exists(location4+os.sep+filename2)==False:
			f=open(location4+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename2)
		if os.path.exists(location4+os.sep+filename3)==False:
			f=open(location4+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename3)
		if os.path.exists(location4+os.sep+filename4)==False:
			f=open(location4+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location4+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	try:
		if os.path.exists(location5+os.sep+filename1)==False:
			f=open(location5+os.sep+filename1,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename1)
		if os.path.exists(location5+os.sep+filename2)==False:
			f=open(location5+os.sep+filename2,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename2)
		if os.path.exists(location5+os.sep+filename3)==False:
			f=open(location5+os.sep+filename3,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename3)
		if os.path.exists(location5+os.sep+filename4)==False:
			f=open(location5+os.sep+filename4,"w")
			f.write("Don't Delete this file. Placed by Security Team. Deleting this will lead to system getting shutdown..")
			f.close()
			os.system('attrib +h '+location5+os.sep+filename4)
	except Exception as ex:
		print ex
		##sys.exit(0)

	#--- Calculating hashes and saving it in a file placed in Temp folder
	try:
		hashfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
		

		try:
			os.system(r'mkdir c:\ransomtesting\hashvalue')
		except:
			pass

		f=open(r'c:\ransomtesting\hashvalue'+os.sep+'Hashlist.txt',"w")
		f.write(hashfile1)
		f.close()
	except Exception as ex:
		print ex
		##sys.exit(0)


#checking if running for 1st time, if yes, then place the files
def checkfirsttime():
	# get username folder lisitng
	from glob import glob
	a=glob(r"C:\Users\*")
	for i in a:
		if os.path.isdir(i)==True:
			try:
				if i!=r'C:\Users\All Users':
					placefiles(i)
			except:
				pass
		
###############################################################

#checking if ransomtestingcheck is present in c drivefolder, if no, then place the files
def copyransomcheck():
	haikya=os.path.exists(r"C:\ransomtesting"+os.sep+'ransomtestingcheck.exe')
	if haikya==False:
		try:
			from shutil import copyfile
			copyfile(os.environ['TEMP']+os.sep+'ransomtestingcheck.exe',r"C:\ransomtesting"+os.sep+'ransomtestingcheck.exe')
		except:
			pass
###############################################################


hashfile1=hashfile2=hashfile3=hashfile4=''

def gethashes():
	global hashfile1,hashfile2,hashfile3,hashfile4
	#### getting the hashes.....
	try:
		filewa=r"C:\ransomtesting\hashvalue"+os.sep+'hashlist.txt'
		f=open(filewa,"r")
		icount=0
		"""
		while True:
			icount+=1
			if icount==5:
				break
			linee=f.readline()
			linee=linee.strip()
			if icount==1:
				hashfile1=str(linee)
			elif icount==2:
				hashfile2=str(linee)
			elif icount==2:
				hashfile3=str(linee)
			elif icount==2:
				hashfile4=str(linee)
		"""
		linee=f.readline()
		linee=linee.strip()
		hashfile1=hashfile2=hashfile3=hashfile4=str(linee)
		f.close()
	except Exception as ex:
		print ex
		#sys.exit(0)

#############################################################


#### Module to monitor file and Terminate abruptly###########
import time
import ctypes
import threading
import datetime
def monitorfile(username):
	
	location1=username+os.sep+'Desktop'
	location2=username+os.sep+'Documents'
	location3=username
	location4=username+os.sep+'Downloads'
	location5='C:'
	

	#--- List of files with specific names to be generated ---#
	filename1="1aaa_crypto.txt"
	filename2="eee_crypto.txt"
	filename3="zzz_crypto.txt"
	filename4="99hh_crpto.txt"

	try:
		class myThread (threading.Thread):
			def __init__(self, threadID, name, counter):
				threading.Thread.__init__(self)
				self.threadID = threadID
				self.name = name
				self.counter = counter
			def run(self):
				print "Starting " + self.name
				# Get lock to synchronize threads
				if self.threadID==5:
					checkforautorun()
				else:
					print_time(self.name, self.counter, 3)
				# Free lock to release next thread
		
		def checkforautorun():
			try:
				while True:
					time.sleep(60)
					# get autorun date and time
					commdate='date /T'
					output = subprocess.check_output(commdate,shell=True)
					commtime='time /T'
					output = output.replace('\r\n','')
					nowdate= output
					output = output+'___'+subprocess.check_output(commtime,shell=True)
					output = output.replace('\r\n','')

					def calculatedatediff(y1,m1,d1,y2,m2,d2):
						from datetime import date
						d0 = date(y1, m1, d1)
						d1 = date(y2, m2, d2)
						delta = d1 - d0
						return int(delta.days)
						pass

					def takeautorunlist():
						os.system(r"C:\ransomtesting\tools"+os.sep+'autorunsc.exe -a * /accepteula > '+r'C:\ransomtesting'+os.sep+'the2ndwhitelistauto.txt')

					if os.path.exists(r"C:\ransomtesting"+os.sep+'concurrenttime.txt')==False:
						# check if date is >=15 than time noted in the1stautoodatetime.txt
						ghb=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.txt','r')
						datefirst=ghb.read().strip()
						ghb.close()

						#Mon 11/13/2017___hh:mm:ss  m/d/y
						datefirst=datefirst.split('___')[0]
						datefirst=datefirst.split(' ')[1]
						datefirst=datefirst.split(os.sep)
						m1=datefirst[0]
						d1=datefirst[1]
						y1=datefirst[2]

						nowdate=nowdate.split(' ')[1]
						nowdate=nowdate.split(os.sep)
						m2=nowdate[0]
						d2=nowdate[1]
						y2=nowdate[2]

						diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

						if diffdays>=15:
							dcf=open(r"C:\ransomtesting"+os.sep+'concurrenttime.txt','w')
							dcf.write(output)
							dcf.close()
							takeautorunlist()

					else:
						ghb=open(r"C:\ransomtesting"+os.sep+'concurrenttime.txt','r')
						datefirst=ghb.read().strip()
						ghb.close()

						#Mon 11/13/2017___hh:mm:ss  m/d/y
						datefirst=datefirst.split('___')[0]
						datefirst=datefirst.split(' ')[1]
						m1=datefirst[0]
						d1=datefirst[1]
						y1=datefirst[2]

						nowdate=nowdate.split(' ')[1]
						nowdate=nowdate.split(os.sep)
						m2=nowdate[0]
						d2=nowdate[1]
						y2=nowdate[2]

						diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

						if diffdays>=15:
							dcf=open(r"C:\ransomtesting"+os.sep+'concurrenttime.txt','w')
							dcf.write(output)
							dcf.close()
							takeautorunlist()






						


					
					"""
					try:
						os.system(r'mkdir "C:\ransomtesting"')
					except:
						pass
					f=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.txt','w')
					#f=open('C:\Windows\System32'+os.sep+'ransomtesting'+os.sep+'the1stautodatentime.txt','w')
					f.write(output)
					f.close()
					"""
					pass
			except:
				pass		

		def print_time(threadName, delay, counter):
			#global hashfile1,hashfile2,hashfile3,hashfile4,location1,location2,location3,location4

			while counter:
				time.sleep(delay)
				print 'I am '+threadName
				if threadName=="Thread-1":
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file1'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l1f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location2+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file1'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l2f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location3+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file1'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l3f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location4+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file1'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l4f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location5+os.sep+filename1, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file1'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l5f1')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

					except Exception as ex:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print ex
						print 'th1'
						randstr=str(id_generator())
						exc=str(ex)
						cmdf='echo "'+exc+'"'
						cmdf=cmdf+' > C:\Users\Hemant\Desktop'+os.sep+'th1'+randstr+'.txt'
						os.system(cmdf)
						a=os.system('bcdedit /set {current} safeboot network');
						b=os.system('shutdown /s /f /t 00')
						print a,b;
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('in ex th1')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

				elif threadName=="Thread-2":
					#--I will montior filename2 in all 4 locations
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file2'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l1f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location2+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file2'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l2f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location3+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file2'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l3f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location4+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file2'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l4f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

						monfile1=hashlib.md5(open(location5+os.sep+filename2, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file2'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l5f2')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							#f.close()

					except Exception as ex:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print ex
						print 'th2'
						randstr=str(id_generator())
						exc=str(ex)
						cmdf='echo "'+exc+'"'
						cmdf=cmdf+' > C:\Users\Hemant\Desktop'+os.sep+'th2'+randstr+'.txt'
						a=os.system('bcdedit /set {current} safeboot network');
						b=os.system('shutdown /s /f /t 00')
						print a,b;
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('in ex th2')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
				elif threadName=="Thread-3":
					#--I will montior filename3 in all 4 locations
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file3'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l1f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location2+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file3'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l2f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location3+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file3'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l3f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location4+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file3'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l4f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location5+os.sep+filename3, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file3'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l5f3')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					except Exception as ex:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print ex
						print 'th3'
						randstr=str(id_generator())
						exc=str(ex)
						cmdf='echo "'+exc+'"'
						cmdf=cmdf+' > C:\Users\Hemant\Desktop'+os.sep+'th3'+randstr+'.txt'
						a=os.system('bcdedit /set {current} safeboot network');
						b=os.system('shutdown /s /f /t 00')
						print a,b;
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('in ex th3')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
				elif threadName=="Thread-4":
					#--I will montior filename4 in all 4 locations
					try:
						#--I will montior filename1 in all 4 locations
						monfile1=hashlib.md5(open(location1+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo1,file4'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l1f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location2+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo2,file4'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l2f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location3+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo3,file4'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l3f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location4+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo4,file4'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l4f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

						monfile1=hashlib.md5(open(location5+os.sep+filename4, 'rb').read()).hexdigest()
						if monfile1!=hashfile1:
							try:
								f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
								f.write('Infected Machine: Do not Turn ON')
								f.close()
								"""
								try:
									SPI_SETDESKWALLPAPER = 20
									ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'Documents'+os.sep+'infected.png' , 0)
								except Exception as ex:
									print 'Setting Wallpaper failed'
								"""

								now=datetime.datetime.now()
								pasttime=uptime.boottime()
								fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
								fp.write(str(now)+'\n')
								fp.write(str(pasttime))
								fp.close()
							except:
								pass
							print 'lo5,file4'
							a=os.system('bcdedit /set {current} safeboot network');
							b=os.system('shutdown /s /f /t 00')
							print a,b;
							#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
							l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
							fc=open(l,'a+')
							fc.write('l5f4')
							fc.close()
							##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					except Exception as ex:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							#f.close()
							
							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+'hemant'+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print ex
						print 'th4'
						randstr=str(id_generator())
						exc=str(ex)
						cmdf='echo "'+exc+'"'
						cmdf=cmdf+' > C:\Users\Hemant\Desktop'+os.sep+'th4'+randstr+'.txt'
						a=os.system('bcdedit /set {current} safeboot network');
						b=os.system('shutdown /s /f /t 00')
						print a,b;
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('in ex th4')
						fc.write(str(ex))
						fc.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
				else:
					pass   



		threadLock = threading.Lock()
		threads = []

		# Create new threads
		thread1 = myThread(1, "Thread-1", 5)
		thread2 = myThread(2, "Thread-2", 6)
		thread3 = myThread(3, "Thread-3", 4)
		thread4 = myThread(4, "Thread-4", 3)
		thread5 = myThread(5, "Thread-4", 5)## only for autorun list

		# Start new Threads
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
		thread5.start()

		# Add threads to thread list
		threads.append(thread1)
		threads.append(thread2)
		threads.append(thread3)
		threads.append(thread4)
		threads.append(thread5)

		# Wait for all threads to complete
		for t in threads:
			t.join()
		print "Exiting Main Thread"
	except Exception as ex:
		print ex
		#sys.exit(0)

import multiprocessing
import time
import os
import psutil
from multiprocessing import Process, freeze_support

if __name__ == '__main__':
	#service = multiprocessing.Process(name='my_service', target=my_service)
	#worker_1 = multiprocessing.Process(name='worker 1', target=worker)
	#worker_2 = multiprocessing.Process(target=worker) # use default name

	#worker_1.start()
	#worker_2.start()
	#service.start()
	freeze_support()
	
	cv=psutil.Process(os.getpid()).parent()
	cv=str(cv.name())
	print cv
	#raw_input('---')
	"""
	if cv=='taskeng.exe' or cv=='cmd.exe':
		createmutex()
		checkfirsttime()
		copyransomcheck()
		gethashes()
		monitorfile()
	"""
	current_process = psutil.Process()
	children = current_process.children(recursive=True)
	for child in children:
		print('Child pid is {}'.format(child.pid))
	else:
		randstr=str(id_generator())
		cmdf='dir > C:\Users\Hemant\Desktop'+os.sep+'yy'+randstr+'.txt'
		os.system(cmdf)
		createmutex()
		checkfirsttime()
		copyransomcheck()
		gethashes()
		# get autorunlist every 15 days
		#TODO: doing now


		############################################################3
		from glob import glob
		a=glob(r"C:\Users\*")
		for i in a:
			if os.path.isdir(i)==True:
				try:
					if i!=r'C:\Users\All Users':
						monitorfile(i)
				except:
					pass
		

	
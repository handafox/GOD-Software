# I do monitoring.. that's my job.. don't disturb me..
#
import os
import sys
import hashlib
#raw_input('place ransomtestingcheck.exe in system32 folder..')
gettheusername=os.environ.get("USERNAME")
location1='C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Desktop'
location2='C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'
location3='C:'+os.sep+'Users'+os.sep+gettheusername
location4='C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Downloads'
location5='C:'
filename1="1aaa_crypto.txt"
filename2="eee_crypto.txt"
filename3="zzz_crypto.txt"
filename4="99hh_crpto.txt"
def placefiles():
	global location1,location2,location3,location4,location5,filename1,filename2,filename3,filename4
	#--- List of users Locations ---#
	try:
		gettheusername=os.environ.get("USERNAME")
		location1='C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Desktop'
		location2='C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'
		location3='C:'+os.sep+'Users'+os.sep+gettheusername
		location4='C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Downloads'
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
		##sys.exit(0)

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
		##sys.exit(0)


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
		##sys.exit(0)

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
		##sys.exit(0)

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
		##sys.exit(0)

	#--- Calculating hashes and saving it in a file placed in Temp folder
	try:
		hashfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
		hashfile2=hashlib.md5(open(location1+os.sep+filename2, 'rb').read()).hexdigest()
		hashfile3=hashlib.md5(open(location1+os.sep+filename3, 'rb').read()).hexdigest()
		hashfile4=hashlib.md5(open(location1+os.sep+filename4, 'rb').read()).hexdigest()

		try:
			os.system(r'mkdir c:\windows\system32\ransomtesting\hashvalue')
		except:
			pass

		f=open(r'c:\windows\system32\ransomtesting\hashvalue'+os.sep+'Hashlist.txt',"w")
		f.write(hashfile1+'\n')
		f.write(hashfile2+'\n')
		f.write(hashfile3+'\n')
		f.write(hashfile4+'\n')
		f.close()
	except Exception as ex:
		print ex
		##sys.exit(0)


#checking if running for 1st time, if yes, then place the files
haikya=os.path.exists(r'c:\windows\system32\ransomtesting\firsttime.txt')
if haikya==False:
	placefiles()
	ff=open(r'c:\windows\system32\ransomtesting\firsttime.txt','w')
	ff.close()# created the file, if its firsttime...
###############################################################

#checking if ransomtestingcheck is present in c drivefolder, if no, then place the files
haikya=os.path.exists(r'C:'+os.sep+'ransomtestingcheck.exe')
if haikya==False:
	try:
		from shutil import copyfile
		import os
		copyfile(r'c:\windows\system32\ransomtesting\ransomtestingcheck.exe','C:'+os.sep+'ransomtestingcheck.exe')
	except:
		pass
###############################################################




#### getting the hashes.....
try:
	f=open(r'c:\windows\system32\ransomtesting\hashvalue'+os.sep+'Hashlist.txt',"r")
	icount=0
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
			
			print_time(self.name, self.counter, 3)
			# Free lock to release next thread
			

	def print_time(threadName, delay, counter):
		global hashfile1,hashfile2,hashfile3,hashfile4,location1,location2,location3,location4
		while counter:
			time.sleep(delay)
			print 'I am '+threadName
			if threadName=="Thread-1":
				try:
					#--I will montior filename1 in all 4 locations
					monfile1=hashlib.md5(open(location1+os.sep+filename1, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo1,file1'
						
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l1f1')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location2+os.sep+filename1, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo2,file1'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l2f1')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location3+os.sep+filename1, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo3,file1'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l3f1')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location4+os.sep+filename1, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo4,file1'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l4f1')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location5+os.sep+filename1, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo5,file1'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l5f1')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

				except Exception as ex:
					try:
						f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
						f.write('Infected Machine: Do not Turn ON')
						f.close()
						
						now=datetime.datetime.now()
						pasttime=uptime.boottime()
						fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
						fp.write(str(now)+'\n')
						fp.write(str(pasttime))
						fp.close()
					except:
						pass
					print ex
					print 'th1'
					##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
					l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
					fc=open(l,'a+')
					fc.write('in ex th1')
					fc.close()
					#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

			elif threadName=="Thread-2":
				#--I will montior filename2 in all 4 locations
				try:
					#--I will montior filename1 in all 4 locations
					monfile1=hashlib.md5(open(location1+os.sep+filename2, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo1,file2'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l1f2')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location2+os.sep+filename2, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo2,file2'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l2f2')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location3+os.sep+filename2, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo3,file2'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l3f2')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location4+os.sep+filename2, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo4,file2'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l4f2')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

					monfile1=hashlib.md5(open(location5+os.sep+filename2, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo5,file2'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l5f2')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						#f.close()

				except Exception as ex:
					try:
						f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
						f.write('Infected Machine: Do not Turn ON')
						f.close()
						
						now=datetime.datetime.now()
						pasttime=uptime.boottime()
						fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
						fp.write(str(now)+'\n')
						fp.write(str(pasttime))
						fp.close()
					except:
						pass
					print ex
					print 'th2'
					##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
					l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
					fc=open(l,'a+')
					fc.write('in ex1 th3')
					fc.close()
					#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
			elif threadName=="Thread-3":
				#--I will montior filename3 in all 4 locations
				try:
					#--I will montior filename1 in all 4 locations
					monfile1=hashlib.md5(open(location1+os.sep+filename3, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo1,file3'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l1f3')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location2+os.sep+filename3, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo2,file3'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l2f3')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location3+os.sep+filename3, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo3,file3'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l3f3')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location4+os.sep+filename3, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo4,file3'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l4f3')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location5+os.sep+filename3, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo5,file3'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l5f3')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

				except Exception as ex:
					try:
						f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
						f.write('Infected Machine: Do not Turn ON')
						f.close()
						
						now=datetime.datetime.now()
						pasttime=uptime.boottime()
						fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
						fp.write(str(now)+'\n')
						fp.write(str(pasttime))
						fp.close()
					except:
						pass
					print ex
					print 'th3'
					##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
					l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
					fc=open(l,'a+')
					fc.write('in ex th3')
					fc.close()
					#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
			elif threadName=="Thread-4":
				#--I will montior filename4 in all 4 locations
				try:
					#--I will montior filename1 in all 4 locations
					monfile1=hashlib.md5(open(location1+os.sep+filename4, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo1,file4'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l1f4')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location2+os.sep+filename4, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo2,file4'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l2f4')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location3+os.sep+filename4, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo3,file4'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l3f4')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location4+os.sep+filename4, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo4,file4'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l4f4')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

					monfile1=hashlib.md5(open(location5+os.sep+filename4, 'rb').read()).hexdigest()
					if monfile1!=hashfile1:
						try:
							f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
							f.write('Infected Machine: Do not Turn ON')
							f.close()
							"""
							try:
								SPI_SETDESKWALLPAPER = 20
								ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'Documents'+os.sep+'infected.png' , 0)
							except Exception as ex:
								print 'Setting Wallpaper failed'
							"""

							now=datetime.datetime.now()
							pasttime=uptime.boottime()
							fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
							fp.write(str(now)+'\n')
							fp.write(str(pasttime))
							fp.close()
						except:
							pass
						print 'lo5,file4'
						##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
						l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
						fc=open(l,'a+')
						fc.write('l5f4')
						fc.close()
						#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')

				except Exception as ex:
					try:
						f=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'Abruptransomtesting.txt',"w")
						f.write('Infected Machine: Do not Turn ON')
						#f.close()
						
						now=datetime.datetime.now()
						pasttime=uptime.boottime()
						fp=open('C:'+os.sep+'Users'+os.sep+gettheusername+os.sep+'AppData'+os.sep+'Local'+os.sep+'Temp'+os.sep+'timeransomtesting.txt','w')
						fp.write(str(now)+'\n')
						fp.write(str(pasttime))
						fp.close()
					except:
						pass
					print ex
					print 'th4'
					##os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
					l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
					fc=open(l,'a+')
					fc.write('in ex th4')
					fc.close()
					#os.system('bcdedit /set {current} safeboot network');os.system('shutdown /s /f /t 00')
			else:
				pass   



	threadLock = threading.Lock()
	threads = []

	# Create new threads
	thread1 = myThread(1, "Thread-1", 5)
	thread2 = myThread(2, "Thread-2", 6)
	thread3 = myThread(3, "Thread-3", 4)
	thread4 = myThread(4, "Thread-4", 3)
	# Start new Threads
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

	# Add threads to thread list
	threads.append(thread1)
	threads.append(thread2)
	threads.append(thread3)
	threads.append(thread4)

	# Wait for all threads to complete
	for t in threads:
		t.join()
	print "Exiting Main Thread"
except Exception as ex:
	print ex
	#sys.exit(0)

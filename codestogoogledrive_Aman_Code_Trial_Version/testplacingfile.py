import subprocess
import os
import hashlib
import time


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




from glob import glob
a=glob(r"C:\Users\*")
for i in a:
	if os.path.isdir(i)==True:
		try:
			print i,'normal'
			#raw_input('---')
			if i!=r'C:\Users\All Users' and i!=r'C:\Users\Default' and i!=r'C:\Users\Default User' and i!=r'C:\Users\Public':
				#placefiles(i)
				print i
				raw_input('going again..')
				pass
		except:
			pass

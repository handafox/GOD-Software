def deinfectautoruns():
	global gofordeinfection
	takeautorunlist()
	try:
		#os.system(r'C:\ransomtesting\internals'+os.sep+'autorunsc.exe -a /accepteula > '+r'C:\ransomtesting'+os.sep+'infectedauto.exe')

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

		# check if 2ndwhitelist date is around 10 dat\ys before than today, then deinfect using that

		if os.path.exists(r"C:\ransomtesting"+os.sep+'concurrenttime.exe')==False: # this means only first whitelist is available
			# 
			#takeautorunlist()

			fv1=open(r"C:\ransomtesting"+os.sep+'infectedauto.exe','r')
			fv1s=fv1.read()
			fv1.close()


			fv2=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.exe','r')
			fv2s=fv2.read()
			fv2.close()



			import string
			printable = set(string.printable)
			fv1s=filter(lambda x: x in printable,fv1s)
			fv2s=filter(lambda x: x in printable,fv2s)
			#fv1s=fv1s.split('\r\n')# infected one
			#fv2s=fv1s.split('\r\n')

			listofsofttodel=[]

			fv1s=fv1s.split('\r\n')
			fv2s=fv2s.split('\r\n')

			fv1snospace=[]
			fv2snospace=[]

			for sw1 in fv1s:
				fv1snospace.append(sw1.lstrip())

			for sw1 in fv2s:
				fv2snospace.append(sw1.lstrip())


			for sw1 in fv1snospace:
				if sw1.startswith('c:'+os.sep) and sw1 not in fv2snospace:
					sw1=sw1.replace('\r\n','')
					sw1=sw1.strip()
					listofsofttodel.append(sw1)


			print listofsofttodel

			for jk in listofsofttodel:
				try:
					quarantinebyname(jk)
				except Exception as ex:
					print ex

		else: # need to check 2nd whitelist creation time
			#takeautorunlist()

			fv1=open(r"C:\ransomtesting"+os.sep+'the2ndwhitelistauto.exe','r')
			fv1s=fv1.read()
			fv1.close()


			fv2=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.exe','r')
			fv2s=fv2.read()
			fv2.close()



			import string
			printable = set(string.printable)
			fv1s=filter(lambda x: x in printable,fv1s)
			fv2s=filter(lambda x: x in printable,fv2s)
			#fv1s=fv1s.split('\r\n')# infected one
			#fv2s=fv1s.split('\r\n')

			listofsofttodel=[]

			fv1s=fv1s.split('\r\n')
			fv2s=fv2s.split('\r\n')

			fv1snospace=[]
			fv2snospace=[]

			for sw1 in fv1s:
				fv1snospace.append(sw1.lstrip())

			for sw1 in fv2s:
				fv2snospace.append(sw1.lstrip())


			for sw1 in fv1snospace:
				if sw1.startswith('c:'+os.sep) and sw1 not in fv2snospace:
					sw1=sw1.replace('\r\n','')
					sw1=sw1.strip()
					listofsofttodel.append(sw1)


			print listofsofttodel

			
			for jk in listofsofttodel:
				try:
					quarantinebyname(jk)
				except Exception as ex:
					print ex
	except Exception as ex:
		print ex
		raw_input('---------------------')
		pass
	pass

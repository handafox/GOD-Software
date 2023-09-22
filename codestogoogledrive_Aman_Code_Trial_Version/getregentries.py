import _winreg
from _winreg import *
import os
d4=open("autoentry.txt","w")
d4.close()

noofsubkey=0
def dead(a,b,count):
	global noofsubkey
	#print '\t'*count+a+os.sep+b
	try:
		key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,b,0,_winreg.KEY_READ)
	except:
		return
	query=_winreg.QueryInfoKey(key)
	#print '\t'*count+str(query[0]),'lol'
	#query=QueryInfoKey(a+os.sep+b)
	ko=a+os.sep+b
	#take one subkey at a time and print its value
	for i in range(0,query[0]):
		#print '\t'*count+str(i),'iiiiiiiiiiii',query[0]
		#key1 = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,ko,0,_winreg.KEY_READ)
		#enum=_winreg.EnumKey(key1,i)
		#print '\t'*count+ko
		#ko="HKEY_CURRENT_USER"+ko
		#now we check the first name of subkey from line 20
		enum=_winreg.EnumKey(key,i)#--------------------------------
		# If there are no subkeys left then pass.
	
		#print enum+'\n')#--------------------------------
		ko1=enum
		#print '\t'*count+ko1,'111111'
		patt=b+os.sep+ko1
		#print '\t'*count+patt
		print '\t'*count+"HKEY_LOCAL_MACHINE"+os.sep+patt+'\n'
		try:
			key1 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,patt,0,_winreg.KEY_READ)
		except:
			return
		noofsubkey=_winreg.QueryInfoKey(key1)[0]
		#print '\t'*count+str(noofsubkey),'33333333333'
		for i in xrange(0, _winreg.QueryInfoKey(key1)[1]):
			#print str(_winreg.EnumValue(key1, i))+'\n')
			#print '\t'*count+str(_winreg.EnumValue(key1, i))
			print '\t'*count+str(_winreg.EnumValue(key1, i))+'\n'
		if noofsubkey >0:
			#print '\t'*count+'------------------------->>>>>>--------------'
			#print '\t'*count+b+os.sep+ko1,'9999999999999999999'
			dead('HKEY_LOCAL_MACHINE',b+os.sep+ko1,count+1)
			#print '\t'*count+'After dead'
		else:
				pass
		#print '\t'*count+str(i),query[0],'laba lab'
	else:
		#print '\t'*count
		pass

##############################################################################

def getvalues(ko):
	#ko="System\CurrentControlSet\Control\Session Manager"
	query=QueryInfoKey(HKEY_LOCAL_MACHINE)
	#kl="SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
	#print kl==ko
	#print "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
	key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, ko, 0, _winreg.KEY_READ)

	for i in xrange(0, _winreg.QueryInfoKey(key)[1]):
		print str(_winreg.EnumValue(key, i))+'---s\n'


def getsubkeysvalue(ko):
	#ko="System\CurrentControlSet\Control\Session Manager"
	query=QueryInfoKey(HKEY_LOCAL_MACHINE)
	#kl="SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
	#print kl==ko
	#print "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
	key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, ko, 0, _winreg.KEY_READ)

	for i in xrange(0, _winreg.QueryInfoKey(key)[1]):
		print str(_winreg.EnumValue(key, i))+'---s\n'

	count=0
	for i in range(0,query[0]):
		enum=EnumKey(HKEY_LOCAL_MACHINE,i)
		count+=1
		#print '\t'*count+"HKEY_LOCAL_MACHINE"+os.sep+str(enum)+'===\n'
		ko=enum
		print ko
		try:
			key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,ko,0,_winreg.KEY_READ)
			print key,'ppp'
			for i in xrange(0, _winreg.QueryInfoKey(key)[1]):
				print str(_winreg.EnumValue(key, i))+'-=-=-=\n'
		except:
			pass
		#print '\t'+ko,'0000000000'
		#print ko
		#dead('HKEY_LOCAL_MACHINE',ko,1)

gg=open('listwa.txt','r')
for jk in gg.readlines():
	if jk.startswith('HKLM'):
		jk=jk.replace('HKLM'+os.sep,'')
		print jk.strip()+'----'
		ko=jk.strip()
		try:
			raw_input('go.. ')
			getsubkeysvalue(ko)
			
		except Exception as ex:
			print '#@#@',ex,'####'
			ko=ko.split(os.sep)
			print ko
			lenoflist=len(ko)
			lp=''
			for i in range(0,lenoflist-1):
				if i!=lenoflist-2:
					lp=lp+ko[i]+os.sep
				else:
					lp=lp+ko[i]
			print lp
			getvalues(lp)


	



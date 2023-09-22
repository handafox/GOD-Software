import os
"""
l=os.environ['TEMP']+os.sep+'outtt.txt'
print l
cmd="net session > '"+l+"'"
print cmd

os.system(cmd)
"""

import time

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
	while True:
		print 'I have admin privillge..'
		l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
		fc=open(l,'w')
		fc.write('11111111111111111')
		fc.close()
		time.sleep(1)
		break
else:
	while True:
		print "I don't have admin privillge"
		l=os.environ['TEMP']+os.sep+'outttnowlol.txt'
		fc=open(l,'w')
		fc.write('no admin')
		fc.close()
		time.sleep(1)
		break
#raw_input('exit..')
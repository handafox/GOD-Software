fv1=open('autorunslist.txt','r')
fv1s=fv1.read()
fv1.close()


fv2=open('listwa.txt','w')




import string
printable = set(string.printable)
fv1s=filter(lambda x: x in printable,fv1s)

fv1s=fv1s.split('\r\n')

for sw1 in fv1s:
	print sw1
	if sw1.startswith('HK'):
		fv2.write(sw1+'\n')
	if sw1.startswith('C:'):
		fv2.write(sw1+'\n')

fv2.close()
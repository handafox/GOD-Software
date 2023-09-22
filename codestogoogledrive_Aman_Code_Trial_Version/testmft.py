import os
# this codeis on hold for sometime, will check it later, if it can be used anyhow
def processmft():
	processtorunmft=' -extract c:'+os.sep+'$Mft '+location1+os.sep+'Mftextracted'
	fgetpathh=location1+os.sep+'zextr.exe'

	os.system(fgetpathh+processtorunmft)

	os.system(location1+os.sep+'analyzemft.exe  -f '+location1+os.sep+'Mftextracted -c '+location1+os.sep+'Mftextractedcsv.csv')


	## need to process mft csv file here and get top exes executed over then...
	vgh=open(location1+os.sep+'timee.txt','r')
	timeshot=[]
	for ihb in vgh.readLines():
		timeshot.append(ihb.strip())

	timeofcatch=timeshot[0]
	vgh.close()

	parsingtime=timeofcatch.split(' ')
	
	datteofattack=parsingtime[0]
	timmeofattack=parsingtime[1]
	
	datteofattack=datteofattack.split('-')
	timmeofattack=timmeofattack.split(':')

	yrrofattack=datteofattack[0]
	mntofattack=datteofattack[1]
	dayyofattack=datteofattack[2]

	hourrofattack=timmeofattack[0]
	minttofattack=timmeofattack[1]
	#secondd=timme[2]

	pastimeofturnon=timeshot[1]

	parsingtime=pastimeofturnon.split(' ')
	
	datteofturnon=parsingtime[0]
	timmeofturnon=parsingtime[1]
	
	datteofturnon=datteofturnon.split('-')
	timmeofturnon=timmeofturnon.split(':')

	yrrofturnon=datteofturnon[0]
	mntofturnon=datteofturnon[1]
	dayyofturnon=datteofturnon[2]

	hourrofturnon=timmeofturnon[0]
	minttofturnon=timmeofturnon[1]
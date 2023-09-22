import multiprocessing
import time
import os
import psutil

def worker():
	name = multiprocessing.current_process().name
	print name, 'Starting'
	time.sleep(2)
	print os.getpid()
	print psutil.Process(os.getpid()).ppid()
	print name, 'Exiting'

def my_service():
	name = multiprocessing.current_process().name
	#print dir(multiprocessing)
	#print dir(name)
	print '###########'
	print str(os.getpid())+'----->'
	print str(psutil.Process(os.getpid()).ppid())+'<--------'
	cv=psutil.Process(os.getpid()).parent()
	print str(cv.name())+'..-..'
	current_process = psutil.Process()
	children = current_process.children(recursive=True)
	for child in children:
		print('Child pid is. {}'.format(child.pid))
	else:
		print 'no chillld'
	print '#############'
	#print dir(os)
	print name, 'Starting'
	time.sleep(3)
	print psutil.Process(os.getpid()).ppid()
	print name, 'Exiting'
from multiprocessing import Process, freeze_support

if __name__ == '__main__':
	freeze_support()
	service = multiprocessing.Process(name='my_service', target=my_service)
	#worker_1 = multiprocessing.Process(name='worker 1', target=worker)
	#worker_2 = multiprocessing.Process(target=worker) # use default name

	#worker_1.start()
	#worker_2.start()
	service.start()
	print '-----'
	print str(os.getpid())+'***'
	print str(psutil.Process(os.getpid()).ppid())+'*--'
	print str(psutil.Process(os.getpid()).parent())+'*-8-8'
	#print dir(psutil.Process(os.getpid()))
	current_process = psutil.Process()
	children = current_process.children(recursive=True)
	for child in children:
		print('Child pid is {}'.format(child.pid))
	print '====='
	raw_input('---')
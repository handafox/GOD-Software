import psutil
mydictread={}
mydictwrite={}

for p in psutil.process_iter(attrs=['pid', 'name', 'username']):
    #print p
    
    
    #print p.io_counters().read_count
    #print p.io_counters().write_count
    #print p.info['name']
    if p.info['name']=='System':
        print p.io_counters()
    #if p.info['name']=='chrome.exe':
    #    p.terminate()
    #print p.pid
    mydictread[p.io_counters().read_count]=p
    mydictwrite[p.io_counters().write_count]=p
    pass

print mydictwrite
print mydictread

#mydictread=sorted(mydictread, reverse=True)
b=sorted(mydictwrite.keys(), reverse=True)
c=sorted(mydictread.keys(), reverse=True)
#print b
#print '----------'
#print mydictwrite
#print mydictread
for i in range(0,10):
    print mydictwrite[b[i]]
pass

for i in range(0,10):
    print mydictread[c[i]]
pass

"""
for p in f:
    if p.info['name']=='chrome.exe':
   
        p.terminate()
"""
pass


import os
import time
while True:
    time.sleep(2)
    if os.path.exists(r'C:\Users\Hemant\Desktop\abc.txt')==False:
        os.system('handle64.exe * /accepteula> '+r'handleme.exe')
        print 'done'
        raw_input('....')
        break
    else:
        print 'File present'
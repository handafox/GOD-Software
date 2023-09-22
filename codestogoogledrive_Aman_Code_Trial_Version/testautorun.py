def checkforautorun():
    try:
        while True:
            if gofordeinfection==1:
                break
            time.sleep(60)
            # get autorun date and time
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

            def takeautorunlist():
                os.system(r'C:\ransomtesting\internals'+os.sep+'autorunsc.exe -a * /accepteula > '+r'C:\ransomtesting'+os.sep+'the2ndwhitelistauto.exe')

            if os.path.exists(r"C:\ransomtesting"+os.sep+'concurrenttime.exe')==False:
                # check if date is >=15 than time noted in the1stautoodatetime.exe
                ghb=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.exe','r')
                datefirst=ghb.read().strip()
                ghb.close()

                #Mon 11/13/2017___hh:mm:ss  m/d/y
                datefirst=datefirst.split('___')[0]
                datefirst=datefirst.split(' ')[1]
                datefirst=datefirst.split(os.sep)
                m1=datefirst[0]
                d1=datefirst[1]
                y1=datefirst[2]

                nowdate=nowdate.split(' ')[1]
                nowdate=nowdate.split(os.sep)
                m2=nowdate[0]
                d2=nowdate[1]
                y2=nowdate[2]

                diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

                if diffdays>=15:
                    dcf=open(r"C:\ransomtesting"+os.sep+'concurrenttime.exe','w')
                    dcf.write(output)
                    dcf.close()
                    takeautorunlist()

            else:
                ghb=open(r"C:\ransomtesting"+os.sep+'concurrenttime.exe','r')
                datefirst=ghb.read().strip()
                ghb.close()

                #Mon 11/13/2017___hh:mm:ss  m/d/y
                datefirst=datefirst.split('___')[0]
                datefirst=datefirst.split(' ')[1]
                m1=datefirst[0]
                d1=datefirst[1]
                y1=datefirst[2]

                nowdate=nowdate.split(' ')[1]
                nowdate=nowdate.split(os.sep)
                m2=nowdate[0]
                d2=nowdate[1]
                y2=nowdate[2]

                diffdays=calculatedatediff(y1,m1,d1,y2,m2,d2)

                if diffdays>=15:
                    dcf=open(r"C:\ransomtesting"+os.sep+'concurrenttime.exe','w')
                    dcf.write(output)
                    dcf.close()
                    takeautorunlist()






                


            
            """
            try:
                os.system(r'mkdir "C:\ransomtesting"')
            except:
                pass
            f=open(r"C:\ransomtesting"+os.sep+'the1stautodatentime.exe','w')
            #f=open('C:\Windows\System32'+os.sep+'ransomtesting'+os.sep+'the1stautodatentime.exe','w')
            f.write(output)
            f.close()
            """
            pass
    except:
        pass        
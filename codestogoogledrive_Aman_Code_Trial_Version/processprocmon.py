import csv
findingslistafterprocessing=[]
with open('test.csv','rb') as f:
     reader=csv.reader(f)
     for row in reader:
            #print row
            if row[3]=='WriteFile':
               try:
                   ju=row[4].index('abc.txt')
                   findingslistafterprocessing.append(row)
               except:
                   pass
            if row[5]=='Delete: True':
                try:
                    ju=row[4].index('abc.txt')
                    findingslistafterprocessing.append(row)
                except:
                    pass
            if row[3]=='Process Create':
               findingslistafterprocessing.append(row)


gg=open('proc.txt','w')
for i in findingslistafterprocessing:
    for jj in i:
        try:
            gg.write(str(jj)+' ')
        except:
            pass
    gg.write('\n')
gg.close()             


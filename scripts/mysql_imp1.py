#This builds a file MySQL can import, empty records need
#to be encoded with '\N' for NULL
import csv

sql_path = 'C:\\ProgramData\MySQL\\MySQL Server 5.6\\data\\ctr17b\\all.csv'

fout = open(sql_path,'w')

with open('train.csv') as f:
    reader = csv.reader(f)
    #reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            if i == 0: my_row = v 
            else:
                if v == "": my_row += ',\\N'
                else: my_row += ',' + v
        my_row += '\n'
        fout.write(my_row)

f.close()                
fout.close()
            
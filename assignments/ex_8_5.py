ffile_name = input('Enter file file_name:-')
# enter file ' mbox-short.txt'
cntr = 0
file1 = open(ffile_name)
for line in file1 :
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    x = line.split()
    print (x[1])
    cntr=cntr+1
print ('There were', cntr, 'lines in the file with From as the first word')
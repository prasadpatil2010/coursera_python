ffile_name = raw_input('Enter file file_name: ')
if len(ffile_name) == 0:
    ffile_name = 'mbox-short.txt'
x = open(ffile_name)
count = 0
tot = 0
ans = 0
for line in x:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    tot = num + tot
ans = tot / count
print ('Average spam confidence:', ans)
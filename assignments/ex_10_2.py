
file_name = 'mbox-short.txt' #input('Enter file:')
file_name = input('Enter the file_name of the  file:-')
# print(len(file_name))
# if len(file_name) < 1 :
text = open(file_name)

hours = dict() # directory

for line in text:
    line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    hour = words[5].split(':')
    hours[hour[0]] = hours.get(hour[0],0) + 1
# print(words)
# print('\n')
#  print(hours)
lst = []
for a,b in hours.items():
    lst.append((a,b))
lst.sort()
# print(lst)

for v,k in lst:
    print (v,k)
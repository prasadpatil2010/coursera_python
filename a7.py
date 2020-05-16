# (1, 2, 3) <(6, 8, 1)
#

file1=open('romeo.txt')
# file1=input('Enter file file_name: ')
counts=dict()
for i in file1:
    line=i.split()
    for j in line:
        counts[j]=counts.get(j,0)+1
print(counts)
print('\n')
print(counts.items())
print('\n')
list1=list()
for a,b in counts.items():
    new_tuple=(a,b)
    list1.append(new_tuple)
    # print(list1.append(new_tuple))
list1=sorted(list1)
print(list1)
print('\n')
list1=sorted(list1, reverse=True)
print(list1)
print('\n')
for b,a in list1[:10]:
    print(a,b)


x={'pvp':10, 'pp':5, 'prasad':8}
print(sorted([(b,a) for a, b in x.items()]))
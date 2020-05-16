file_file_name = input("Enter file file_name:-")
x = open(file_file_name) #direct give file file_name with extension
a = list()
for line in x:
    line = line.strip().split()
    for w in line:
        a.append(w)
x = sorted(a)
l3 = []
for i in x:
    if i not in l3:
        l3.append(i)
print (l3)
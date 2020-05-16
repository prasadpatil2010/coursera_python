ffile_name = input("Enter file file_name: ")
x = open(ffile_name)

for line in x:
    line = line.rstrip()
# line = line.upper()
    print (line.upper())
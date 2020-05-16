# fruit='banana'
# print(fruit)
# print('fruit')
# print(fruit[2])
# for letter in fruit:
#     print(letter)

# ff='Hello PVP'
# dd=ff.replace('PVP', 'PP')
# print(ff)
# print(dd)
# ff.startswith('Hello')
# f=ff.startswith('Hello')
# print(f)

# x='Hello, how are you? '
# x=x.find(',')
# print(x)
# a3=x[7]  #find 8th letter
# print(a3)
# a4=x[7:10] #find 8,9,10 letter
# print(a4)
# a5=len(a4)
# print(a5)
# a6=type(a5)
# print(a6)
# a7=x+' '+ 'where are u?'
# print(a7)
# a8='THNX'
# a9=a7+' '+a8
# print(a9)
#
# x = '40'
# y1 = x + '2'
# print(y1)
# y2 = int(x) + 2
# print(y2)

# d=open('11.txt')
# d1=d.read()
# # print(d1)
# # print(len(d1)) # this icludes spaces also
# for line in d:
#     line=line.rstrip()
#     if line.startswith('1:'):
#         print(line)
#     # print(line)
# # print(line)
# # print(d1)


ffile_name = input("Enter file file_name: ")
x = open(ffile_name)

for line in x:
    line = line.rstrip()
# line = line.upper()
    print (line.upper())

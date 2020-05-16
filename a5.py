# list1=list()  # this is for  list
# # list1=[5, 3 , 6] # list:[]
# print(list1)
# list1.append(5)
# print(list1)
# list1.append(8)
# print(list1)

# jjj=dict()  # this is for  dictionary
# print(jjj)
#
# jjj={'jan':10, 'feb':2, 'april':4} # dictionary:{}
# print(jjj)
#
# # jjj.apend('may':5)
# jjj['may']=5
# print(jjj)
# print(jjj['may'])


# counts=dict() # this is for  dictionary
# month=['jan', 'feb', 'april', 'may'] # this is for  list
# print(month)
# for i in month:
#     print(i)
#     if i not in counts:
#         counts[i]=1
#     else:
#         counts[file_name] = 1+ counts[file_name]
# print(counts)

counts=dict() # this is for  dictionary
month=['feb','april', 'jan', 'feb', 'april', 'may'] # this is for  list
print(month)
month=sorted(month)
print(month)
for i in month:
    counts[i]=counts.get(i,0)+1
print(counts)

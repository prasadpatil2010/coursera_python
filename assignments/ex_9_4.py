
file_name = 'mbox-short.txt' #input('Enter file:')
# print(len(file_name))
# if len(file_name) < 1 : #file_name = "mbox-short.txt"
text = open(file_name)

maxauthor = dict()
# print(maxauthor)
# print(text)
for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    maxauthor[words[1]] = maxauthor.get(words[1],0)+1

largest = None
largest_author = None

for key in maxauthor:
    if largest is None: largest = maxauthor[key]

    if largest < maxauthor[key]:
        largest = maxauthor[key]
        largest_author = key

print (largest_author, largest)




# a=2
# b=20
# c=a*b
# print(c)
# print('c')
# print("c")
#
# #
# jj=4**2
# print(jj)
#
# ff=jj%5  # reminder
# print(ff)
#
# ddd='hi '+ 'prasad'
# print(ddd)
# type(ddd)

# j=input('who are you?')
# print('welcome ',j)

# floor=input('enter floor number : ')
# us_floor=1+int(floor)
# print('ur floor is ', us_floor, 'in usa system')


# file_name = input("Enter your file_name")
# print('Hello ', file_name)


# hrs = input("Enter Hours:")
# rate=input("Enter rate per hour")
# pay=int(hrs)*float(rate)
# print(pay)

# astr = 'Hello Bob'
# istr = 0
# try:
#     istr = int(astr)
# except:
#     istr = -1
# print(istr)


hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numerical value")
    quit()

print(h, r)
if h > 40:
    pay = 40 * r + (h - 40) * r * 1.5
elif h <= 40:
    pay = h * r
print(pay)

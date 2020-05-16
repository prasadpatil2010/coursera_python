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

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done": break

    try:
        num = float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = 0
    elif largest > num:
        largest = largest
    else:
        largest = num
    if smallest is None:
        smallest = num
    elif num<smallest:
        smallest = num
    else:
        smallest= smallest
# print("Maximum", largest)
print('Maximum is', largest)
print('Minimum is', smallest)
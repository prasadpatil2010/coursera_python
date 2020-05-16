
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
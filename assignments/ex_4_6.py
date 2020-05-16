

#h = input("Enter Hours:")
hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

h = float(hrs)
r = float(rate)

def computepay(h,r):
    if h > 40:
        p = 40 * r + (h - 40) * r * 1.5
    elif h <= 40:
        p = h * r
    return p

p = computepay(h,r)
print("Pay",p)
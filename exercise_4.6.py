def computepay(h,r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * r * 1.5
    return pay

hrs = float(input("Enter Hours:"))
rt = float(input("Enter Rate:"))
p = computepay(hrs, rt)
print("Pay",p)

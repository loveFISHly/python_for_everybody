hrs = float(input("Enter Hours:"))
rt = float(input("Enter Rates:"))

if hrs <= 40:
    print(hrs * rt)
else:
    print(40 * rt + (hrs - 40) * rt * 1.5)

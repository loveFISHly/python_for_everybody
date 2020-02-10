name = input("Enter file:")
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From:'):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1
    else:
        continue

maxEmail = None
maxCount = None

for email, count in counts.items():
    if maxCount is None or maxCount < count:
        maxCount = count
        maxEmail = email
                  
print(maxEmail,maxCount)

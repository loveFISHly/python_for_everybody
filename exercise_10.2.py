name = input("Enter file:")
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        hour = line.split()[5][:2]
        counts[hour] = counts.get(hour, 0) + 1
    else:
        continue
        
lst = list()
for hour, count in counts.items():
    lst.append((hour, count))
    
lst.sort()

for hour, count in lst:
    print (hour, count)

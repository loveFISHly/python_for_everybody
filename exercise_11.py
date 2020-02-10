import re
file = open('regex_sum_37511.txt')

total = 0

for line in file:
    num = re.findall('[0-9]+', line)
    num = list(map(int, num))
    for n in range(len(num)):
        total += num[n]
print(total)

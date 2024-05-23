from itertools import product
s = product('АПРСУ', repeat=5)
count = 0
for str in s:
    count += 1
    line = ''.join(str)
    if line.count('У') <= 1:
        print(count, line)
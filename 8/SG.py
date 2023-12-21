from itertools import product
s = product('АВЕСТ', repeat=5)
count = 1
for str in s:
    line = ''.join(str)
    if line == 'СВЕТА':
        print(count)
    count += 1
from itertools import product
s = product('ABCD', repeat=2)
count = 0
for str in s:
    c
    line = ''.join(str)
    if not (line == 'AA' or line == 'BB' or line == 'CC' or line == 'DD'):
        print(count, line)
from itertools import product
s = product('УОА', repeat=6)
count = 0
for str in s:
    line = ''.join(str)
    if line == 'ОУУУОО':
        print(count)
    count += 1
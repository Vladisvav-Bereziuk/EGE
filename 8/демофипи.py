from itertools import product
s = product('АБЗИ', repeat=4)
count = 0
for str in s:
    count += 1
    line = ''.join(str)
    if line == "ИЗБА":
        print(count, line)
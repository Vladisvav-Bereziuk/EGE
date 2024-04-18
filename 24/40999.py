txt = open('40999.txt').readline().split('E')
print(txt)
max_len = 0
for i in txt:
    if i.count('A') > 2:
        max_len = max(max_len, len(i))
print(max_len)
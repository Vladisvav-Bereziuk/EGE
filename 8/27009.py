import itertools

count = 0
listSting = itertools.product('НИКОЛАЙ', repeat=4)

for str in listSting:
    line = ''.join(str)
    if line[1] != 'Й':
        if line.count('И') > 0 or line.count('О') or line.count('А'):
            count += 1
print(count)


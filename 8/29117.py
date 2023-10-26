import itertools

count = 0
listString = itertools.product('ТИМОФЕЙ',repeat= 5)

for str in listString:
    line = ''.join(str)
    if line[0] != 'Й' and line[4] != 'Й':
        if line.count('Й') < 2 and line.count('ЙИ') == 0 and line.count('ИЙ') ==0:
            count += 1
print(count)

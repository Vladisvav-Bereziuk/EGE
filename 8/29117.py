import itertools

count = 0
listString = itertools.product('ПОЛИНА',repeat= 4)
listStringS = list(itertools.product('ПЛН',repeat= 2)) #согласные
listStringG = list(itertools.product('ОИА',repeat= 2)) #гласные
for str in listString:
    line = ''.join(str)
    if line != listStringS and line != listStringG:
        count += 1

print(count)
#не решено
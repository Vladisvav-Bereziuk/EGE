from itertools import product

listString = product('ПОЛИНА', repeat = 4)
count = 0

for str in listString:
    line = ''.join(str)
    if line.count('ПП') == 0 and line.count('ПЛ') == 0 and line.count('ПН') == 0 and line.count('ЛЛ') == 0 and line.count('ЛП') == 0 and line.count('ЛН') == 0 and line.count('НП') == 0 and line.count('НЛ') == 0 and line.count('НН') == 0 and line.count('ОО') == 0 and line.count('ОИ') == 0 and line.count('ОА') == 0 and line.count('ИО') == 0 and line.count('ИИ') == 0 and line.count('ИА') == 0 and line.count('АО') == 0 and line.count('АИ') == 0 and line.count('АА') == 0:
        count += 1
print(count)
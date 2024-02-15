#35465 - номер задания
for i in range(99,1488):
    b = bin(i)[2:]
    for o in range(3):
        one = b.count('1')
        nul = b.count('0')
        if nul == one:
            b = b + b[-1]
        else:
            if nul<one:
                b = b + '0'
            else:
                b = b + '1'
    n = int(b,2)
    if n % 4 == 0:
        print('конечное', n)
        print('начальное', i)




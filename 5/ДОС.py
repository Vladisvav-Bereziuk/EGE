for n in range(1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '01'
    else:
        b = '1' + b + '1'
    res = int(b,2)
    if res >= 156:
        print(n,res)
        break
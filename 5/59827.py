def convert(num):
    res = ""
    while num > 0:
        o = num % 3
        num = num // 3
        res += str(o)
    return res[::-1]

for n in range(1,1000):
    t = convert(n)
    if n % 3 == 0:
        t += t[-2:]
    else:
        t += convert((n % 3)*5)
    t = int(t,3)
    if t <= 173:
        print(t)




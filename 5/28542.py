def convert(num):
    result = ""
    while num > 0:
        result = str(num % 3) + result
        num = num // 3
    return result


for i in range(1, 99999):
    t = convert(i)
    n = int(t) % 3
    res = t + str(n)
    res = int(res, 3)

    if res >= 1000:
        print(res)
        break

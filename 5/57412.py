for num in range(1000):
    b = bin(num)[2:]
    if num % 3 == 0:
        b += b[-3:]
    else:
        b += bin((num % 3) * 3)[2:]
    res = int(b, 2)
    if res >= 76:
        print(num)
        break

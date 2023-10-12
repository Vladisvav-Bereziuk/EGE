for num in range(1000):
    b = bin(num)[2:]
    if num % 2 == 0:
        b = "10" + b
    else:
        b = "1"+b+"01"
    res = int(b, 2)
    if res > 441:
        print(num)
        break
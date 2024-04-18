
for i in range(1000):
    b = bin(i)[2:]
    if i % 3 == 0:
        b += b[:-3]
        n = int(b, 2)
    else:
        bi = bin(i % 3)[2:]
        b = b+bi
        n = int(b,2)
    if n >= 151:
        print(n)
        break

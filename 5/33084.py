for n in range(1,1000):
    b = bin(n)[2:]
    for i in range(2):
        counts = b.count('1') % 2
        b =  b + str(counts)
        r = int(b,2)
        if r > 154:
            print(n)
            break
for a in range(64):
    f = True
    for x in range(64):
        if not ((x & a != 0) <= ((x & 36 == 0) <= (x & 6 != 0))):
            f = False
    if f:
        print(a)

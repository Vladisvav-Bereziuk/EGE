def dell(x,A):
    if (not x % A) <= ((x % 28) <= (not x % 49)):
        return 1
    else:
        return 0

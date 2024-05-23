res = 0
for i in range(33):
    i = str(i)
    ip = '192.168.1.'+i
    ip = ' '.join([bin(int(o))[2:].zfill(8) for o in ip.split('.')])

    if ip.count('1') % 4 == 0:
        res += 1
        print(res)

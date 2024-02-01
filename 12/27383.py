
def convert(d):
    s = '12' * d + (10-d)*'1'
    while '12' in s:
        s = s.replace('12', '4', 1)
    return s

for i in range(1,1000):
    x = convert(i)
    if x.count('1') + x.count('2')*2 + x.count('4')*4 == 25:
        print(i)


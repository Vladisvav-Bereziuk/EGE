def convert(d):
    s = '1'*(100+d)
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    return s

for i in range(0,1000):
    result = convert(i)
    if result.count('1') == 1:
        print(i+100, result.count('1'))
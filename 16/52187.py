def f(n):
    if n == 0:
        return 0
    else:
        return f(n // 10) + (n % 10)
x = 0
for i in range(1488):
    if f(i) > f(i+1):
        print(i, f(i))

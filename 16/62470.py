from sys import setrecursionlimit
setrecursionlimit(99999)
count = 0
def f(n):
    if n < 9:
        return(n)
    if n >= 9:
        return(f(n % 9)+f(n // 9))

for i in range(3656158440062976):
    if f(i) == 121:
        count =+ 1
        print(count)
# не решено, компьютер начал издавать звуки бомбы
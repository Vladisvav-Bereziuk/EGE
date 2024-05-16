from sys import setrecursionlimit
setrecursionlimit(99999)
count = 0
def f(n):
    if n == 0:
        return(0)
    if n > 0 and n % 2 == 0:
        return(f(n/2))
    if not(n % 2 == 0):
        return(1+f(n-1))

for  i in range(1,901):
    if f(i) == 9:
        count +=1
        print(count)
from sys import setrecursionlimit
setrecursionlimit(99999)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return(f(n-1)*n)
print(f(5))
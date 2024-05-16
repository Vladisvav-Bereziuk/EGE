from sys import setrecursionlimit
setrecursionlimit(99999)
def f(n):
    if n == 1:
        return(1)
    if n == 2:
        return(1)
    if n > 2:
        return(f(n-2)*n)
print(f(7))
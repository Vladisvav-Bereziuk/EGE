from sys import *
def f(n):
    if n <11: return 10
    else: return n+f(n-1)
setrecursionlimit(14888)
print(f(2024)-f(2022))
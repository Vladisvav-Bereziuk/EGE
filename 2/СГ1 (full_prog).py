from itertools import product, permutations


def f1(x, y, z, w):
    return (x == y) and (w <= z)


def f2(x, y, z, w):
    return (x <= y) <= (w == z)


for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    table = [
        (1,  x1, 1,  1,  1, 0),
        (0,  1,  0,  x2, 1, x3),
        (x4, 0,  0,  x5, 0, 0)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(f1(**dict(zip(p, s))) == s[-2] and f2(**dict(zip(p, s))) == s[-1] for s in table):
                print(p)

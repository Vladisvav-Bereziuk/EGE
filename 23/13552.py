def f(current, to):
    if current > to:
        return 0
    if current == to:
        return 1
    return f(current + 1, to) + f(current + 2, to) + f(current + 4, to)


# Ограничение "траектория содержит число n"
print(f(1, 8) * f(8, 15))
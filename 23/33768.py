def f(current, to):
    # Ограничение "траектория не содержит число n"
    if current > to or current == 15:
        return 0
    if current == to:
        return 1
    return f(current + 1, to) + f(current + 2, to) + f(current * 3, to)


print(f(2, 11) * f(11, 16))
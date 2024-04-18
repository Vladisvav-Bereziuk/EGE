def f(current, to):
    # Ограничение "траектория не содержит число n"
    if current > to or current == 15 or current == 11:
        return 0
    if current == to:
        return 1
    return f(current + 1, to) + f(current * 2, to) + f(current + 3, to)


# Ограничение "траектория содержит число n"
print(f(2, 8) * f(8, 20) )
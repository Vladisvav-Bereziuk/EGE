def f(current, to,is_mul):
    # Ограничение "траектория не содержит число n"
    if current > to:
        return 0
    if current == to:
        return 1
    if is_mul:
        return f(current + 1, to, False) + f(current * 2, to, False)
    else:
        return f(current + 1, to, False) + f(current * 2, to, True)


print(f(1, 14,True))
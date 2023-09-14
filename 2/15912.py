print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # Если в таблице в последнем столбце результат равен 0, то
                # необходимо всё выражение взять под знаком отрицания (not())
                if not(((x <= y) == (z <= w)) or (x and w)):
                    print(x, y, z, w)

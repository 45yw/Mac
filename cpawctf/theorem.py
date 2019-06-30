for q in range(10000000):
    y = 3438478 * q + 160993
    a = y % 1584891
    if a == 0:
        x = y + 32134
        print(x)

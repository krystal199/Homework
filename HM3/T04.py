def line_fun (x, y):

    powered = x

    if y > 0:
        for _ in range(1, y):
            powered *= x
    else:
        for _ in range(1, y, -1):
            powered /= x

    return powered


a, b = float(input("Число a >>> ")), int(input("Число b >>> "))

print(line_fun(a, b))
def dev (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


x = int(input("Введите число x: "))
y = int(input("Введите число y: "))

print(dev(x, y))

total = 0

while True:
    numbers = input("Введите строку из чисел через пробел >>> ").split()
    unique_point = False

    for number in numbers:
        if number.isdigit():
            total += int(number)
        else:
            unique_point = True
            break

    print(f"Общая сумма чисел = {total}")

    if unique_point:
        break
#rabota s oshibkami
try:
    num = int(input("Введите число: "))
    result = 10 / num
    print("Результат:", result)
except ZeroDivisionError:
    print("Ошибка: Деление на ноль невозможно.")
except ValueError:
    print("Ошибка: Введите корректное число.")

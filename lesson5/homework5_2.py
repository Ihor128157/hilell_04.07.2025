print("Простий калькулятор")

run = 'y'
while run in ('y', 'yes'):
    num1 = input("Введіть перше число: ")
    num2 = input("Введіть друге число: ")
    op = input("Введіть операцію (+, -, *, /): ")

    if num1.count('.') <= 1 and num2.count('.') <= 1:
        n1 = float(num1) * 1.0
        n2 = float(num2) * 1.0

        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            if n2 != 0:
                result = n1 / n2
            else:
                result = "Помилка: ділення на нуль!"
        else:
            result = "Невідома операція"
    else:
        result = "Помилка: неправильний ввід числа!"

    print("Результат:", result)
    run = input("Продовжити? (y/yes): ").lower()



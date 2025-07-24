print("Простий калькулятор")
num1 = float(input("Введіть перше число: "))
op = input("Введіть операцію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль!"
else:
    result = "Невідома операція"

print("Результат:", result)

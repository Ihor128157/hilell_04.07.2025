number = int(input("Введіть п’ятизначне число: "))

reversed_number = (number % 10) * 10000 + ((number // 10) % 10) * 1000 + ((number // 100) % 10) * 100 + ((number // 1000) % 10) * 10 + (number // 10000)

print("Число задом наперед:", reversed_number)

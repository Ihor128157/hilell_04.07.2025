import math

class Fraction:
    def __init__(self, a, b):  # Конструктор класу, ініціалізує чисельник та знаменник дробу
        if b == 0:  # Перевірка, чи знаменник не дорівнює нулю
            raise ValueError("Denominator cannot be zero")
        self.a = a  # Встановлює чисельник дробу
        self.b = b  # Встановлює знаменник дробу
        self.simplify()  # Спрощує дріб

    def simplify(self):  # Метод для спрощення дробу
        gcd = math.gcd(self.a, self.b)  # Обчислює найбільший спільний дільник
        self.a //= gcd  # Ділить чисельник на НСД
        self.b //= gcd  # Ділить знаменник на НСД

    def __mul__(self, other):  # Перевизначення методу множення дробів
        new_a = self.a * other.a  # Множить чисельники
        new_b = self.b * other.b  # Множить знаменники
        return Fraction(new_a, new_b)  # Повертає новий екземпляр класу Fraction

    def __add__(self, other):  # Перевизначення методу додавання дробів
        new_a = self.a * other.b + other.a * self.b  # Обчислює новий чисельник
        new_b = self.b * other.b  # Обчислює новий знаменник
        return Fraction(new_a, new_b)  # Повертає новий екземпляр класу Fraction

    def __sub__(self, other):  # Перевизначення методу віднімання дробів
        new_a = self.a * other.b - other.a * self.b  # Обчислює новий чисельник
        new_b = self.b * other.b  # Обчислює новий знаменник
        return Fraction(new_a, new_b)  # Повертає новий екземпляр класу Fraction

    def __eq__(self, other):  # Перевизначення методу порівняння дробів на рівність
        return self.a == other.a and self.b == other.b  # Порівнює чисельники та знаменники

    def __gt__(self, other):  # Перевизначення методу порівняння дробів на більше
        return self.a * other.b > other.a * self.b  # Порівнює дроби шляхом перетворення до спільного знаменника

    def __lt__(self, other):  # Перевизначення методу порівняння дробів на менше
        return self.a * other.b < other.a * self.b  # Порівнює дроби шляхом перетворення до спільного знаменника

    def __str__(self):  # Перевизначення методу для рядкового представлення об'єкта
        return f"Fraction: {self.a}, {self.b}"  # Повертає рядкове представлення дробу


f_a = Fraction(2, 3)  # Створює екземпляр дробу 2/3
f_b = Fraction(3, 6)  # Створює екземпляр дробу 3/6 (який буде спрощено до 1/2)
f_c = f_b + f_a  # Додає два дроби
assert str(f_c) == 'Fraction: 7, 6'  # Перевіряє, чи результат додавання правильний
f_d = f_b * f_a  # Множить два дроби
assert str(f_d) == 'Fraction: 1, 3'  # Перевіряє, чи результат множення правильний
f_e = f_a - f_b  # Віднімає два дроби
assert str(f_e) == 'Fraction: 1, 6'  # Перевіряє, чи результат віднімання правильний

assert f_d < f_c  # Перевіряє, чи дріб f_d менший за дріб f_c
assert f_d > f_e  # Перевіряє, чи дріб f_d більший за дріб f_e
assert f_a != f_b  # Перевіряє, чи дроби f_a і f_b не рівні
f_1 = Fraction(2, 4)  # Створює екземпляр дробу 2/4 (який буде спрощено до 1/2)
f_2 = Fraction(3, 6)  # Створює екземпляр дробу 3/6 (який буде спрощено до 1/2)
assert f_1 == f_2  # Перевіряє, чи дроби f_1 і f_2 рівні
print('OK')  # Виводить 'OK', якщо всі перевірки пройшли успішно


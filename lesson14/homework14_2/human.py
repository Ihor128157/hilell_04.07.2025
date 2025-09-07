class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender  # Зберігає стать людини
        self.age = age  # Зберігає вік людини
        self.first_name = first_name  # Зберігає ім'я людини
        self.last_name = last_name  # Зберігає прізвище людини

    def __str__(self):
        # Повертає рядок з основною інформацією про людину
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'

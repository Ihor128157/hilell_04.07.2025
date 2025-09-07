from human import Human  # Імпортує клас Human з модуля human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)  # Виклик ініціалізатора класу Human
        self.record_book = record_book  # Зберігає номер залікової книжки студента

    def __str__(self):
        # Повертає рядок з розширеною інформацією про студента
        return f'{super().__str__()}, Record Book: {self.record_book}'

    def __eq__(self, other):
        # Метод порівняння студентів за рядком, який повертає метод __str__
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        # Метод хешування для використання екземплярів класу Student в множинах
        return hash(str(self))

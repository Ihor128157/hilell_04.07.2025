from student import Student  # Імпортує клас Student з модуля student

class Group:
    def __init__(self, number):
        self.number = number  # Зберігає номер групи
        self.group = set()  # Ініціалізує пусту множину для студентів

    def add_student(self, student):
        self.group.add(student)  # Додає студента до групи

    def delete_student(self, last_name):
        student = self.find_student(last_name)  # Знаходить студента по прізвищу
        if student:
            self.group.remove(student)  # Видаляє студента з групи, якщо знайдено

    def find_student(self, last_name):
        for student in self.group:  # Перебирає всіх студентів у групі
            if student.last_name == last_name:
                return student  # Повертає студента, якщо прізвище співпадає
        return None  # Повертає None, якщо студента не знайдено

    def __str__(self):
        # Створює рядок з інформацією про всіх студентів у групі
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\n{all_students}'  # Повертає номер групи та список студентів


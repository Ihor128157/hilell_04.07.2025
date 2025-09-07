from student import Student  # Імпортує клас Student з модуля student
from group import Group  # Імпортує клас Group з модуля group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')  # Створює екземпляр студента
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')  # Створює ще одного екземпляра студента
gr = Group('PD1')  # Створює екземпляр групи

gr.add_student(st1)  # Додає першого студента до групи
gr.add_student(st2)  # Додає другого студента до групи
print(gr)  # Виводить інформацію про групу та студентів

assert gr.find_student('Jobs') == st1  # Перевіряє правильність пошуку студента з прізвищем Jobs
assert gr.find_student('Jobs2') is None  # Перевіряє, що студент з прізвищем Jobs2 не знайдений
gr.delete_student('Taylor')  # Видаляє студента з прізвищем Taylor
print(gr)  # Виводить інформацію про групу після видалення студента

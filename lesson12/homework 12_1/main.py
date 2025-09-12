import codecs  # Імпортуємо модуль codecs для роботи з файлами з підтримкою кодувань
import re  # Імпортуємо модуль re для роботи з регулярними виразами

def delete_html_tags(html_file, result_file='cleaned.txt'):
    '''
    Функція для видалення HTML-тегів з тексту у файлі
    html_file: Ім'я вхідного HTML файлу, який потрібно очистити
    result_file: Ім'я вихідного файлу, куди буде записаний очищений текст (за замовчуванням 'cleaned.txt')
    '''

    # Відкриваємо HTML-файл для читання в кодуванні UTF-8
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()  # Читаємо весь вміст файлу у змінну html

    # Видалення HTML-тегів за допомогою регулярного виразу
    cleaned_text = re.sub(r'<[^>]*>', '', html)  # Замінюємо всі підрядки, що відповідають шаблону <...>, на порожній рядок

    # Видалення порожніх рядків
    cleaned_text = ' '.join([line.strip() for line in cleaned_text.splitlines() if line.strip()])

    # Відкриваємо вихідний файл для запису в кодуванні UTF-8
    with codecs.open(result_file, 'w', 'utf-8') as outfile:
        outfile.write(cleaned_text)  # Записуємо очищений текст у вихідний файл з назвою cleaned.txt

# Виклик функції для очищення файлу draft.html і збереження результату у файл cleaned.txt
delete_html_tags('draft.html', 'cleaned.txt')

# import codecs  # Імпортуємо модуль codecs для роботи з файлами з різними кодуваннями
# import re  # Імпортуємо модуль re для роботи з регулярними виразами
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:  # Відкриваємо HTML файл з кодуванням utf-8 для читання
#         result = []  # Ініціалізуємо порожній список для зберігання тексту без HTML тегів
#         for line in file:  # Проходимо по кожному рядку у файлі
#             current_text_list = re.findall(r">(.+)</", line)  # Знаходимо текст між ">" та "</" за допомогою регулярного виразу
#             if len(current_text_list) > 0:  # Якщо знайдено текст
#                 result += current_text_list  # Додаємо знайдений текст до результату
#         print(f"Result: {result}")  # Виводимо результат
#         if len(result) > 0:  # Якщо результат не порожній
#             with open(result_file, 'w', encoding='utf-8') as new_file:  # Відкриваємо новий файл для запису з кодуванням utf-8
#                 new_file.write('\n'.join(result))  # Записуємо результат у новий файл, розділяючи рядки символом нового рядка
#
# delete_html_tags("draft.html")  # Викликаємо функцію з файлом "draft.html"

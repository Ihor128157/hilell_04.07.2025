import string

letters = input("Введіть дві літери через дефіс: ")

start, end = letters.split('-')

all_letters = string.ascii_letters

start_index = all_letters.index(start)
end_index = all_letters.index(end)

print(all_letters[start_index:end_index + 1])

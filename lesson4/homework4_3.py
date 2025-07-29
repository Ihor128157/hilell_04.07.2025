import random
length = random.randint(3, 10)
lst = [random.randint(0, 100) for _ in range(length)]
new_lst = []
for i in range(len(lst)):
    if i == 0 or i == 2 or i == len(lst) - 2:
        new_lst.append(lst[i])
print("Початковий список:", lst)
print("Новий список:", new_lst)

lst = [1, 2, 3, 4, 5, 6]

n = len(lst)

half = (n + 1) // 2

first_part = lst[:half]

second_part = lst[half:]

result = [first_part, second_part]

print(result)

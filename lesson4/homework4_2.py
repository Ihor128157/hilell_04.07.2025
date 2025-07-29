lst = [0, 1, 7, 2, 4, 8]
if lst:
    total = 0
    for i in range(0, len(lst), 2):
        total += lst[i]
    result = total * lst[-1]
else:
    result = 0
print(result)

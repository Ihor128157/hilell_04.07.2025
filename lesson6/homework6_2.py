seconds = int(input("Введіть кількість секунд (від 0 до 8640000): "))

days, remainder = divmod(seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, secs = divmod(remainder, 60)

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(secs).zfill(2)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")

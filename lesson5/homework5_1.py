import keyword
import string

s = input()

allowed = "_abcdefghijklmnopqrstuvwxyz0123456789"

if s == "_":
    print(True)
elif (
    s and
    s[0] not in "0123456789" and
    s.islower() and
    s.count("_") <= 1 and
    s not in keyword.kwlist
):
    valid = True
    for c in s:
        if c not in allowed:
            valid = False
            break
    print(valid)
else:
    print(False)



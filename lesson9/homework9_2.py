def difference(*args):
    """
    Returns the difference between the maximum and minimum of the given numbers.

    If no arguments are provided, the function returns 0.

    :param args: A variable number of numerical arguments (int or float).
    :type args: float or int

    :return: The difference between the largest and smallest numbers, rounded to 2 decimal places.
    :rtype: float or int

    """
    if not args:
        return 0
    return round(max(args) - min(args), 2)

print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())

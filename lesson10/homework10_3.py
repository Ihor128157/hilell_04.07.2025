def is_even(digit):
    """
    Returns True if the given integer is even, otherwise False.

    Parameters:
    ----------
    number : int
        The integer to check.

    Returns:
    -------
    bool
        True if the number is even, False otherwise.
    """
    return digit % 2 == 0


print(is_even(2))
print(is_even(5))
print(is_even(0))

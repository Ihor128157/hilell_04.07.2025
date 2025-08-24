def is_even(number):
    """
    Determines whether a given integer is even without using division,
    modulo, or related operations.

    This function converts the number to a string and checks the last digit.
    If the last digit is one of '0', '2', '4', '6', or '8', the number is even.

    Parameters:
    ----------
    number : int
        The integer to check.

    Returns:
    -------
    bool
        True if the number is even, False otherwise.
    """
    last_digit = str(number)[-1]
    return last_digit in '02468'

# --- Tests ---
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'

print('Ok')

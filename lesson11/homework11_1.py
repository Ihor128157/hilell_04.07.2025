def prime_generator(end):
    """
    Generator function that yields prime numbers up to and including the given end value.

    A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    This function checks each number from 2 to 'end' and yields it if it's prime.

    Parameters:
        end (int): The upper bound of the range to generate prime numbers (inclusive).

    Yields:
        int: The next prime number in the sequence up to 'end'.
    """
    def is_prime(n):
        """
        Helper function to determine if a number is prime.

        Parameters:
            n (int): The number to check.

        Returns:
            bool: True if n is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num

# --- Tests ---
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

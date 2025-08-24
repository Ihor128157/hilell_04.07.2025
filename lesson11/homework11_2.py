def generate_cube_numbers(limit):
    """
    Generator that yields cubes of numbers starting from 2
    until the cube is less than the given limit.

    Parameters:
        limit (int): Upper limit for the cube values (exclusive).

    Yields:
        int: The next cube number less than the limit.
    """
    num = 2
    while True:
        cube = num ** 3
        if cube >= limit:
            return  # Exit generator
        yield cube
        num += 1
print(list(generate_cube_numbers(10)))

# --- Tests ---
from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen)
assert list(generate_cube_numbers(10))
assert list(generate_cube_numbers(100))
assert list(generate_cube_numbers(1000))

print("Ok")

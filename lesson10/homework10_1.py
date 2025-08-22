from inspect import isgeneratorfunction
import types

def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    """
    Generator function that produces a numeric sequence based on a user-defined rule.

    Parameters:
    ----------
    begin : int
        The initial value of the sequence (first term).
    end : int
        The total number of elements to generate.
    func : Callable
        A function that defines the rule for generating the next element in the sequence.

    Yields:
    -------
    int
        The next element of the sequence.
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)

gen = some_gen(4, 5, pow)

print(isinstance(gen, types.GeneratorType))
print(list(gen))

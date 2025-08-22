def first_word(text):
    """
    Finds and returns the first word in the given text.

    A word is a sequence of letters and may include apostrophes (e.g., "don't").
    The function ignores punctuation such as commas and periods.
    It correctly handles strings that start with spaces or punctuation.

    Parameters:
    ----------
    text : str
        The input string to search in.

    Returns:
    -------
    str
        The first word found in the input string.
    """

    for ch in ['.', ',']:
        text = text.replace(ch, ' ')

    words = text.split()

    for word in words:
        cleaned = ''
        for char in word:
            if char.isalpha() or char == "'":
                cleaned += char
            else:
                break
        if cleaned:
            return cleaned
    return ''


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))

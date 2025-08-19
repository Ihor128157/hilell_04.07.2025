from typing import List, Dict

def popular_words(text: str, words: List[str]) -> Dict[str, int]:
    """
    Count how many times each word from a list appears in the given text.

    This function performs a case-insensitive search and returns a dictionary
    with the number of occurrences for each word in the provided list.
    If a word is not found, its count will be 0.

    :param text: The input text to analyze.
    :type text: str
    :param words: A list of lowercase words to count in the text.
    :type words: List[str]

    :return: A dictionary where each key is a word from the input list, and its value is the count.
    :rtype: Dict[str, int]

    """
    words_in_text = text.lower().split()
    result = {word: words_in_text.count(word) for word in words}
    return result

text = "When I was One I had just begun When I was Two I was nearly new"
words = ['i', 'was', 'three', 'near']

print(popular_words(text, words))

import string


def is_palindrome(text):
    text = text.lower()

    cleaned_text = ''.join(char for char in text if char.isalnum())

    return cleaned_text == cleaned_text[::-1]


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))
print(is_palindrome('aurora'))

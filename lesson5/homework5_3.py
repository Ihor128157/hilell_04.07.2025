text = input()

words = text.split()
hashtag = ""

for w in words:
    clean_word = ""
    for ch in w:
        if ch.isalnum():
            clean_word += ch
    if clean_word:
        hashtag += clean_word[0].upper() + clean_word[1:].lower()

hashtag = hashtag[:140]

print("#" + hashtag)


from collections import Counter


def find_nonsingleton_words(text):
    word = text.split()
    word_count = Counter(word)
    repeat_word = [word for word, count in word_count.items() if count > 1]
    return repeat_word

text = "con duong nay rat quen thuoc va con duong nay se dan den nha may duong"
single_word = find_nonsingleton_words(text)
print(single_word)

raise Exception("Not implemented yet")
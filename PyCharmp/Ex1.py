def get_first_word(text):
    word = text.split()
    if word:
        return min(word)
    else:
        return "No word"

text = input()
word = get_first_word(text)
print(word)
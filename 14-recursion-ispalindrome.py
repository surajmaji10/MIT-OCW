# print('b'.isalpha())
# print('7'.isdigit())

def pre_process(word):
    processed = ""
    for ch in word.strip():
        if ch.isalpha() or ch.isdigit():
            processed += ch
    return processed.lower()

def is_palind(word):
    if len(word) <= 1:
        return True
    subword = word[1:-1]
    return word[0] == word[-1] and is_palind(subword)

word = input("Enter word to see for palindrome: ")
word = pre_process(word)
yes = "YES" if is_palind(word) else "NO"
print("'{}' is palindrome? {}".format(word, yes))


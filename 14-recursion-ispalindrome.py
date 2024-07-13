# this is a sample code from MIT OCW 18.00

# print('b'.isalpha())
# print('7'.isdigit())

def pre_process(word):
    assert type(word) == str
    processed = ""
    for ch in word.strip():
        if ch.isalpha() or ch.isdigit():
            processed += ch
    return processed.lower()

def is_palind(word):
    """
    return True if `word` is a palindrome else False
    """
    assert type(word) == str
    
    if len(word) <= 1:
        return True
    subword = word[1:-1]
    return word[0] == word[-1] and is_palind(subword)

word = input("Enter word to see for palindrome: ")
word = pre_process(word)
yes = "YES" if is_palind(word) else "NO"
print("'{}' is palindrome? {}".format(word, yes))


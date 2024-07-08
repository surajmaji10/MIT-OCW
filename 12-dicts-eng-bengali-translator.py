## A simple English ---> Bengali translator

subjects = {
    "I": "Ami",
    "He": "Shey",
    "She": "Shey",
    "They": "Tara",
    "It": "Eita",
}

objects = {
    "Food": "Khabar",
    "Cricket": "Cricket",
    "Fastly": "Tadatari",
    "Fish": "Machh",
    "Home": "Ghor",
}

verbs = {
    "Play": "Khela Kore",
    "Dance": "Nach Kore",
    "Eat": "Khabar Kore",
    "Sleep": "Soyon Kore",
    "Look": "Dekha Kore",
}

def format_sentence(sentence):
    formatted_sentence = ""
    for word in sentence.strip().split():
        formatted_sentence += word.lower().capitalize()
        formatted_sentence += " "
    return formatted_sentence

def translate_word(word):
    if word in subjects.keys():
        return subjects[word]
    if word in objects.keys():
        return objects[word]
    if word in verbs.keys():
        return verbs[word]
    return word

def translate_sentence(sentence):
    translated_sentence = ""
    for word in sentence.split(" "):
        translated_sentence += translate_word(word)
        translated_sentence += " "
    return translated_sentence

sentence = input("Input a sentence: ")

sentence = format_sentence(sentence)
print(sentence)
print(translate_sentence(sentence))


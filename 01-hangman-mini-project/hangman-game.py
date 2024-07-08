import pwinput

# program variables
random_word = ""
list_random_word_chars = []
len_random_word = 0
list_masked_word_chars = []
max_num_guesses = 10
guesses_left = max_num_guesses
case_sensitive = True



def input_a_random_word_and_attempt_limit():
    """
    input (in hidden mode) and store the `random word`
    and set up the `game variables` accordingly
    """
    global random_word
    global len_random_word
    global list_masked_word_chars
    global list_random_word_chars
    global max_num_guesses
    global guesses_left
    global case_sensitive

    print("-----------------------")
    print("WELCOME TO HANGMAN-GAME")
    print("-----------------------")

    prompt = "Guess a random word to guess: "
    plain_text = pwinput.pwinput(prompt=prompt, mask='*')
    # print(case_sensitive)
    if not case_sensitive:
        random_word = plain_text.upper()
    else:
        random_word = plain_text
    # print(random_word)
    len_random_word = len(random_word)
    list_masked_word_chars = ["."] * len_random_word
    for char in random_word:
        list_random_word_chars.append(char)

    prompt = "Random word is case sensitive (y|n)? "
    sensitivity = pwinput.pwinput(prompt=prompt, mask='*')
    if sensitivity.lower()[0] == 'y':
        case_sensitive = True
    else:
        case_sensitive = False

    prompt = "Enter maximum guesses limit: "
    plain_text = pwinput.pwinput(prompt=prompt, mask='*')
    max_num_guesses = int(plain_text)
    guesses_left = max_num_guesses



def display_masked_word(display=True):
    """
    display the `guessed word` so far as a string
    """
    global list_masked_word_chars

    masked_word = ""
    for char in list_masked_word_chars:
        masked_word += char
    # print("mask: ", list_masked_word_chars)
    # print("word: ", list_random_word_chars)
    if display:
        print("Guessed: `{}`".format(masked_word))
    return masked_word



def guess_a_character(left):
    """
    read a `guess character`
    """
    print("{} Guess(es) Left.".format(left))
    prompt = "Enter a character: "
    char = pwinput.pwinput(prompt=prompt, mask='*')
    if case_sensitive:
        return char[0]
    return char.upper()[0]



def valid_character(char, list_chars):
    """
    validate if the `guessed character` is in the `random word` or not
    update the `guessed word` and `game variables` accordingly
    """
    # print("mask: ", list_masked_word_chars)
    # print("word: ", list_random_word_chars)
    if char in list_chars:
        idx = list_chars.index(char)
        list_chars[idx] = '#'
        list_masked_word_chars[idx] = char
        print("`{}` is present. Correct!".format(char))
        return True
    else:
        print("`{}` is NOT present. Incorrect!".format(char))
        return False



def check_for_exit_success(guess):
    """
    look if we have guessed the random word
    """
    return guess == random_word



def display_hangman_killed():
    """
    display the contents ASCII  art in case of falure
    """
    file = open("hangman-killed.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line.rstrip("\n"))
    file.close()



def display_hangman_saved():
    """
    display the contents ASCII  art in case of success
    """
    file = open("hangman-saved.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line.rstrip("\n"))
    file.close()



def game_init():
    # global case_sensitive
    # case_sensitive = False ## True by default
    input_a_random_word_and_attempt_limit()
    print()
    print("-------GAME BEGINS-------")



def game_loop():

    global guesses_left

    display_masked_word()
    while guesses_left > 0:
        char = guess_a_character(guesses_left)
        guesses_left -= 1
        print()
        if valid_character(char, list_random_word_chars):
            guessed_so_far = display_masked_word()
            exit_game = check_for_exit_success(guessed_so_far)
            if exit_game:
                return
        else:
            display_masked_word()



def game_end():

    print("{} Guess(es) Left.".format(guesses_left))
    print("-------GAME ENDS---------")
    print()
    guessed_word = display_masked_word(False)
    print("-------------------------")
    print("Guessed  Word: '{}'".format(guessed_word))
    print("Random   Word: '{}'".format(random_word))
    print("-------------------------")

    if check_for_exit_success(guessed_word) == False:
        print("You have failed to SAVE it!")
        display_hangman_killed()
    else:
        print("You have succeeded to SAVE it!")
        display_hangman_saved()



## GAME STARTS HERE ##
if __name__ == "__main__":
    try:
        game_init()
        game_loop()
        game_end()
    except Exception as e:
        print(e)
        print("Exitting the HANGMAN-GAME due to some error!")
        exit(0)


########## END #############

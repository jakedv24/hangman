# Displaying the hangman character
def disp_hangman(x):
    if x == 6:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n           |"
              "\n           |"
              "\n           |"
              "\n   ________|\n")

    if x == 5:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n  (_)      |"
              "\n           |"
              "\n           |"
              "\n   ________|\n")

    if x == 4:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n  (_)      |"
              "\n   |       |"
              "\n           |"
              "\n   ________|\n")

    if x == 3:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n  (_)      |"
              "\n   |       |"
              "\n  /        |"
              "\n   ________|\n")

    if x == 2:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n  (_)      |"
              "\n   |       |"
              "\n  / \      |"
              "\n   ________|\n")

    if x == 1:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n  (_)      |"
              "\n   |\      |"
              "\n  / \      |"
              "\n   ________|\n")

    if x == 0:
        print("\n   --------|"
              "\n   |       |"
              "\n   |       |"
              "\n (x_x)     |"
              "\n  /|\      |"
              "\n  / \      |"
              "\n   ________|\n")

# Checking the guess to make sure it is within the rules.
def check_guess():
    guess = input("Guess a letter (Type 'end' to quit || Type 'solve' to solve the puzzle): ")
    if guess == "end":
        return guess
    if guess == 'solve':
        return guess
    if len(guess) != 1:
        print("One at a time please. Try again.\n")
        check_guess()
    elif len(guess) == 1 and (65 > ord(guess) or ord(guess) > 122):
        print("That is not a letter, please try again.\n")
        check_guess()

    return guess

# Printing the array of words to the user
def arrayp(array):
    empty_read = ' '.join(array)
    print(empty_read, "\n")

# The general function for the 'main' method
def hangman():
    # Print the intro
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWe are going to play hangman.\n"
          "The guesser will get six wrong guesses before they lose.\n"
          "Guesser please look away.\n")
    secret = input("Please input the secret word/phrase and press enter: ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Guesser, you may end the game at any guess by typing 'end' and hitting enter.\n"
          "If you wish to solve the puzzle, type 'solve' and hit enter. You only get one try at this!\n")

    updating = [0] * len(secret)
    guessed_letters = []

    num_wrong = 0
    num_blanks = 0
    guesses_left = 6

    for i in range(0, len(secret)):
        if secret[i] == ' ':
            updating[i] = secret[i]
        else:
            updating[i] = '_'
            num_blanks += 1

    disp_hangman(6)
    arrayp(updating)

    while num_blanks != 0:
        guess = check_guess()

        if guess == "end":
            break

        if guess == "solve":
            guess = input("\nWhat is the secret word/phrase? : ")
            if guess == secret:
                num_blanks = 0
                break
            if guess != secret:
                disp_hangman(0)
                print("\nI'm sorry! That's the wrong answer...Game Over...\n"
                      "The secret word/phrase was: ", secret)
                break

        in_word = False

        # Updating each of the characters that are correct.
        for x in range(0, len(secret)):

            if secret[x] == guess and updating[x] != guess:
                updating[x] = guess
                num_blanks -= 1
                guessed_letters.append(guess)
                in_word = True

        if not in_word:
            guesses_left -= 1

        disp_hangman(guesses_left)

        if guesses_left == 0:
            print("\nYou lose!!\n"
                  "The word/phrase was: ", secret)
            break

        arrayp(updating)

        print("\nYou have", guesses_left, "wrong guesses left.\n")

    if num_blanks == 0:
        print("\nCongrats you win!")

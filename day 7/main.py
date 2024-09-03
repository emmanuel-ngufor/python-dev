import random
# Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages


# Set the number of lives to start at 6
lives = 6

# print logo
print(logo)

# get a random word from the word_list and store it to choosen_word
chosen_word = random.choice(word_list)
# print(chosen_word)

# Create a "placeholder" with the same number of words as the choosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Update the code below to tell the user how many lives they have left.
    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You\'ve already guessed {guess}")
     
    # Create "display" that puts the guess letter in the right position and _ in the rest of the string
    # Loop uses correct_letter list to keep the previous correct letters in display
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that\'s not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"IT WAS < {chosen_word} >! YOU LOSE")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])

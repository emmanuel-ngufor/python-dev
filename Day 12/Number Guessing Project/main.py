
import random, art
TARGET = random.randint(1, 100)

print(art.logo)
print("Welcome to the number guessing game.\nI am thinking of a number between 1 and 100.")
choice = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

attempts = 0
if choice == "easy":
    attempts = 10
elif choice == "hard":
    attempts = 5

print(f"You have {attempts} attempts to guess the number.")

while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess == TARGET:
        print(f"Congrats...{TARGET} is the right number.")
        attempts = 0
    elif guess < TARGET and attempts > 0:
        attempts -= 1
        print(f"Too LOW.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
    elif guess > TARGET and attempts > 1:
        attempts -= 1
        print(f"Too HIGH.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
    else:
        attempts -= 1
        print("Input must be a number.")
        print(f"Too HIGH.\nGuess again\nYou have {attempts} attempts remaining to guess the number.")


    if attempts == 0:
        print("You have run out of attempts. Restart the program to play again...")




# Relevant Topics: Randomisation, Python Lists, Data Validation

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("ROCK, PAPER, SCISSORS.")

game_images = [rock, paper, scissors]

while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or 3 to Quit: \n"))
        if user_choice == 3:
            print("Thanks for playing!")
            break
        if user_choice < 0 or user_choice > 2:
            print("Invalid number, please choose 0, 1, 2, or 3 to quit.")
            continue

        print(f"\nYou chose:\n{game_images[user_choice]}")

        computer_choice = random.randint(0, 2)
        print(f"Computer chose:\n{game_images[computer_choice]}")

        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")
    except ValueError:
        print("Invalid input. Please enter a number.")

    print("\nLet's play again!\n")

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

TARGET = 21

def display_stats(user_data, comp_data):
    print(f"    Your cards: {user_data}, current score: {sum(user_data)}")
    print(f"    Computers  first card is: {comp_data[0]}")

def process(player_cards, dealer_cards):
    if sum(player_cards) == TARGET and sum(dealer_cards) == TARGET:
        print("It's a draw....")
    elif sum(player_cards) > TARGET and sum(dealer_cards) <= TARGET:
        print(f"    Your final hand: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Computer's final hand: {dealer_cards}, current score: {sum(dealer_cards)}")
        print("You went Over...You lose!😭")
    elif sum(player_cards) <= TARGET and sum(dealer_cards) > TARGET:
        print(f"    Your final hand: {player_cards}, current score: {sum(player_cards)}")
        print(f"    Computer's final hand: {dealer_cards}, current score: {sum(dealer_cards)}")
        print("You Win...!😎")


# get user choice to play the game
choice = str(input("Do you want to play a game of BlackJack? Type 'y' and 'n' for no:    ")).lower()

user_cards = [random.choice(cards), random.choice(cards)]
computer_cards = [random.choice(cards), random.choice(cards) ]

play_again = True
while play_again:

    if choice == "y":
        display_stats(user_cards, computer_cards)
        user_score = sum(user_cards)
        comp_score = sum(computer_cards)

        if user_score == TARGET and comp_score == TARGET:
            print("It's a draw")
            play_again = False
        elif user_score <= TARGET and comp_score > TARGET:
            print(f"    Your final hand: {user_cards}, current score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, current score: {comp_score}")
            print("You Win...!😎")
        elif user_score > TARGET and comp_score <= TARGET:
            print(f"    Your final hand: {user_cards}, current score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, current score: {comp_score}")
            print("You went Over...You lose!😭")

        get_another_card = str(input("Type 'y' to get another card or 'n' to pass:    ")).lower()
        if get_another_card == "y":
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
        else:
            play_again = False
    else:
        play_again = False

import random, game_data, art

print(art.logo)

def get_data():
    return random.choice(game_data.data)

def display(detail):
    return f"{detail['name']}, a {detail['description']}, from {detail['country']}."

def compare(answer, acc_a, acc_b):
    if acc_a["follower_count"] > acc_b["follower_count"] and answer == "A":
        return True
    elif acc_b["follower_count"] > acc_a["follower_count"] and answer =="B":
        return True
    else:
        return False


detailA = get_data()
detailB = get_data()
score = 0

should_continue = True
while should_continue:

    if detailA == detailB:
        detailB = get_data()

    print(f"Compare A: {display(detailA)}")
    print(art.vs)
    print(f"Against: {display(detailB)}")

    choice = str(input("Who has more followers? Type 'A' or 'B': ")).upper()

    restart = compare(choice, detailA, detailB)

    if restart and choice == "A":
        score += 1
        detailA = detailA
        detailB = get_data()
        print(f"You are right!... Current score: {score}")
    elif restart and choice == "B":
        score += 1
        detailA = detailB
        detailB = get_data()
        print(f"You are right!... Current score: {score}")
    else:
        print(f"You are wrong!...Final score:  {score}")
        should_continue = False


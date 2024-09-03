# Relevant Topics: Python Loops and Built in functions
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


                # PRO - LEVEL

# Select the required number of letters, symbols, and numbers
chosen_letters = random.choices(letters, k=nr_letters)
chosen_symbols = random.choices(symbols, k=nr_symbols)
chosen_numbers = random.choices(numbers, k=nr_numbers)

# Combine all chosen characters into one list
combined_pool = chosen_letters + chosen_symbols + chosen_numbers
print(f"Combined Pool before shuffling: \n{combined_pool}\n")

# Shuffle the combined list to ensure a random order
random.shuffle(combined_pool)
print(f"Combined Pool After shuffling: \n{combined_pool}")

# Create the password by joining the shuffled list into a string
password = ''.join(combined_pool)

print(f"\nYour password is: {password}\n")



                # EASY LEVEL

# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_letters):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(password)


                
                # MEDIUM LEVEL
                
# password_list = []
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))

# for char in range(0, nr_letters):
#     password_list.append(random.choice(symbols))

# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")


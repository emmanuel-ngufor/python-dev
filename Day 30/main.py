# HANDLING ERRORS AND DEBUGGING - TRY AND EXCEPTIONS

# # File not found error
# with open("daaata.txt") as file:
#     file.read()

# try: 
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The{error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise TypeError("This is an error I made up")



# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3m")

# bmi = weight / height ** 2
# print(bmi)




# Key Error
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["owner"])



#Index Error
# fruit_list = ["Apple", "Banana", "Guava"]
# print(fruit_list[4])


#Type error
# text = "abc"
# print(text + 7)



# Updates to previous NATO Alphabet project
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = { row.letter: row.code for (index, row) in data.iterrows() }
# print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_text = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_text)

generate_phonetic()
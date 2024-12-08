from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generate Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [ choice(letters) for _ in range(randint(8,10)) ]
    password_symbols = [ choice(symbols) for _ in range(randint(2,4))  ]
    password_numbers = [ choice(numbers) for _ in range(randint(2,4))  ]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# def save():
    
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()

#     if len(website) == 0 and len(password) == 0:
#         messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
#     else:
#         is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs is ok to save?")
#         if is_ok:
#             with open("data.txt", mode="a") as data_file:
#                 data_file.write(f"{website} | {email} | {password}\n")
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = { 
        website: {"email": email, "password": password}
    }

    if len(website) == 0 and len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)   # Adds to the dictionary json to maintain the data structure
        else:
            # Updating the old data with the new data
            data.update(new_data)

            with open(file="data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4) # serialize and deserialize json to readbale format
        finally:   
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# def find_password():
#     site = website_entry.get()
#     try:
#         with open(file="data.json", mode="r") as json_file:
#             #Convert json file to string and loads it like a dict_type via json.loads() method
#             json_str = json_file.read()
#     except FileNotFoundError:
#         messagebox.showinfo(title="Opps", message="No Data File Found")
#     else:  
#         json_data = json.loads(json_str)
        
#         if site in json_data:
#             password = json_data[site]["password"]
#             messagebox.showinfo(title=site, message=f"Website: {site}\nPassword: {password}")
#         else:
#             messagebox.showinfo(title="Opps", message="No details for the website exists")


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)




window.mainloop()

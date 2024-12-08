from tkinter import *

#========== LEARNING =======

def button_click():
    content = input.get()
    my_label.config(text=content)

# Layout Managers = park, place and grid
# NB Cannot mix up geometric managers: choose one or the other

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=2)
new_button = Button(text="New")
new_button.grid(column=2, row=0)

    
# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=3)


window.mainloop()
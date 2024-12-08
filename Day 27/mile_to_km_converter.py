# ========== MILES TO KM CONVERTER PROJECT =================
from tkinter import *

# Function to convert miles to km
def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609, 2) 
    km_result_label.config(text=f"{km}")

# Setup configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=290, height=100)


# Labels
is_equal_label = Label(text="is equal to", font=("Arial", 8, "bold"))
is_equal_label.grid(column=0, row=1)
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)
miles_label = Label(text="Miles", font=("Arial", 8, "bold"))
miles_label.grid(column=2,row=0)
km_label = Label(text="Km", font=("Arial", 8, "bold"))
km_label.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)



window.mainloop()
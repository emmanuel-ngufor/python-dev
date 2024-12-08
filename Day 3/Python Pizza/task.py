print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


final_bill = 0

if size == "S":
    final_bill += 15
    if pepperoni == "Y":
        final_bill +=2
    if extra_cheese == "Y":
        final_bill +=1
elif size == "M":
    final_bill += 20
    if pepperoni == "Y":
        final_bill +=3
    if extra_cheese == "Y":
        final_bill +=1
elif size == "L":
    final_bill += 25
    if pepperoni == "Y":
        final_bill +=3
    if extra_cheese == "Y":
        final_bill +=1
else:
    print("Wrong Input")

print(f"Your final bill is: ${final_bill}.")


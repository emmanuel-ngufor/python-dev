
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

producers_balance = 0
consumers_balance = 0



def print_report():
    """Prints a detailed report of the status of the available resources"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${producers_balance}")

def check_sufficient_resources(item):
    """Compares the resources of drink requested against the available resources for sufficiency"""
    water = item["ingredients"]['water']
    milk = 0
    if milk in item:
        milk = item["ingredients"]['milk']
    coffee = item["ingredients"]['coffee']

    shortage = ""
    if water >= resources['water']:
        shortage = "water"
    elif milk >= resources['milk']:
        shortage = "milk"
    elif coffee >= resources['coffee']:
        shortage = "coffee"

    return shortage

def process_coins():
    """Gets the user's coins and Processes the coins to calculate the total cost of the drink"""
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01

    total_cost = quarters + dimes + nickles + pennies
    return total_cost


def check_transaction_successful(cost_price, customer_price):
    if customer_price >= cost_price:
        return round(customer_price - cost_price, 2)  # Return change if applicable
    else:
        return False  # Explicitly return False if insufficient funds



def make_coffee(option, item):
    machine_resources = item["ingredients"]
    resources["water"] -= machine_resources["water"]

    # Deduct milk only if it exists in the item
    if "milk" in machine_resources:
        resources["milk"] -= machine_resources["milk"]

    resources["coffee"] -= machine_resources["coffee"]

    global producers_balance  # Declare the global variable
    producers_balance += item["cost"]  # Update the global balance

    print(f"Here is your {option} ☕. Enjoy!.")


should_continue = True

while should_continue:
    choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

    if choice in MENU:
        # Get the user's drink choice in the options menu
        drink = MENU[choice]
        # check if there is sufficient resources to make the drink
        available = check_sufficient_resources(drink)
        if available == "":
            # Get the cost price and users price and process coins
            consumers_price = process_coins()
            producers_price = drink["cost"]

            # Check if transaction was successful to proceed to coffee prod
            proceed = check_transaction_successful(producers_price, consumers_price)

            if proceed:
                # Make the coffee is funds were sufficient.
                make_coffee(choice, drink)
                print(f"Here is ${proceed} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print(f"Sorry there is not enough {available}.")
            should_continue = False

    elif choice == "report":
        print_report()
    elif choice == "off":
        should_continue = False
        print("Out of Service. System undergoing maintenance")
    else:
        print("Sorry...we don't have that on the menu. Select another option")

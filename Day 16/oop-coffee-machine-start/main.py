from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Create objects to model the real world classes.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


should_continue = True
while should_continue:

    # Get user input for drink choice
    choice = str(input(f"What would you like? ({menu.get_items()}): ")).lower()

    # Check if system needs to be shut down for maintenance
    if choice == "off":
        should_continue = False
        print("Out of Service. System undergoing maintenance")
    # Print report if the user wants report status of resources
    elif choice == "report":
        # print report
        coffee_maker.report()
        money_machine.report()
    # Process order
    else:
        # Search menu if drink is available and return drink object<MenuItem>
        drink = menu.find_drink(choice)

        # drink is available -- do this
        if drink:
            # Check if there are sufficient resources to make the drink
            if coffee_maker.is_resource_sufficient(drink):
                # Check if the payment was successful
                if money_machine.make_payment(drink.cost):  # Pass the drink cost here
                    coffee_maker.make_coffee(drink)

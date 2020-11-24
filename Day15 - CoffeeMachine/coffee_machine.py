# This module is coding mimic of coffee vending machine.
# project requirement is at "☕"

# Import required modules
from data import MENU, COINS, resources

# Initialization
is_machine_on = True
amount = 0
payment = 0
profit = 0

# Functions
# Function # 1 : Check availability. This function gets input of ingredients of each given coffee item and compare with existing resources. Returns True of False based on availability of stock


def check_availability(ingredients):
    """This function gets input of ingredients of each given coffee item and compare with existing resources. Returns True of False based on availability of stock"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function # 2: Process coins: Calculates the coins total inserted and returns its total.


def process_coins():
    print("Please insert coin.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many cents?: ")) * 0.01
    return total

# Function # 3: is_transaction_successful:


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Req 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a). Check the user’s input to decide what to do next.
# b). The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

while is_machine_on:
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    # Req 2: Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == "off":
        is_machine_on = False
    # Req 3: Print report.
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        # Req 4: Check resources sufficient?
        if check_availability(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])

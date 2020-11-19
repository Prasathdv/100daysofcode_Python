# This module is basic numeric calculator (+,-,*,/) with given 2 numbers. This uses concepts of functions with output and recursion.

# import calculator logo
from art import logo

# define all basic arithmetic functions

# addition


def add(num1, num2):
    return num1 + num2

# Subtraction


def subtract(num1, num2):
    return num1 - num2

# multiply


def multiply(num1, num2):
    return num1 * num2

# divide


def divide(num1, num2):
    return num1 / num2


# Define a dictionary of operand and its corresponding function
calc_operand = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """
        This calculates basic arithmetic operations.
    """
    print(logo)
    num1 = float(input("Enter your first number: "))
    for operand in calc_operand:
        print(operand)

    user_continue = False
    while not user_continue:
        calc_operation = input("Enter the operation: ")
        num2 = float(input("Enter your next number: "))
        call_func = calc_operand[calc_operation]
        answer = call_func(num1, num2)
        print(f"{num1} {calc_operation} {num2} = {answer}")
        user_selection = input(
            f"Type 'y' to continue calculation with {answer} or 'n' to start new one: ")

        if user_selection == "y":
            num1 = answer
        elif user_selection == "n":
            user_continue = True
            calculator()
        else:
            print("Invalid option. Please select valid input")
            calculator()


# function call
calculator()

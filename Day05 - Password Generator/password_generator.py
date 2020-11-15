# This module generates random password for user based on users choice.
# This module uses random module for randomizing list sequence, for loop with range concepts

# Generic letters, symbols and numbers declaration
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Welcoming user and getting required input for generating password
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create a empty list
password_list = []
# Generate the random characters , symbols and numbers using random module choice keyword
for char in range(nr_letters):
    password_list += random.choice(letters)
for symbol in range(nr_symbols):
    password_list += random.choice(symbols)
for num in range(nr_numbers):
    password_list += random.choice(numbers)

# Add logic for randomization using random module`s shuffle
random.shuffle(password_list)
# convert list to string using for loop
password = ''
for char in password_list:
    password += char

# Print final random passoword to user
print(f"Your password is {password}")

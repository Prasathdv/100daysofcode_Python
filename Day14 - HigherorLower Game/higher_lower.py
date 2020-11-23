# Import required modules
from art import logo, vs
from game_data import data
import random
from replit import clear


def print_data(account):
  """ Based on account data return the printable format """
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def choice(guess, option_a, option_b):
  """ Based on guess and follower count return correct user option"""
  if account_a > account_b:
    return user_choice == 'a'
  else:
    return user_choice == 'b'

# Display logo
print(logo)
score = 0
is_game_alive = False
random_account_b = random.choice(data)
# Make the game repeatable
while not is_game_alive:
  # Generate random data from data list
  # Making account at position B become the next account at position A.
  random_account_a = random_account_b
  random_account_b = random.choice(data)
  if random_account_a == random_account_b:
    random_account_b = random.choice(data)

  # Format the random data into printable format
  print(f"Compare A: {print_data(random_account_a)}")
  # Display vs logo
  print(vs)
  print(f"Against B: {print_data(random_account_b)}")

  # ask use the option
  user_choice = input("Choose the option 'A' or 'B' => ").lower()

  # Check if user guess is right
  # Get follower count for both options
  account_a = random_account_a["follower_count"]
  account_b = random_account_b["follower_count"]
  # Use if condition to check if user is correct
  # Score calculation
  # Give user feedback
  condition = choice(user_choice, account_a, account_b)
  if condition:
    score += 1
    clear()
    print(logo)
    print(f"You`ve guessed correct. Your score is {score}")
  else:
    clear()
    print(logo) 
    print(f"Sorry your guess is incorrect. Final score is {score}")
    is_game_alive = True 
    

# Clear the screen between rounds
# This module is number guessing game. This uses scopes concept

# import required modules
from random import randint
from art import logo

# Declaring global constants
EASY_LEVEL = 10
HARD_LEVEL = 5
INVALID_INPUT = 0


def choose_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' => ")
    if difficulty_level == 'easy':
        return EASY_LEVEL
    elif difficulty_level == 'hard':
        return HARD_LEVEL
    else:
        return INVALID_INPUT


def game_engine(number, guess, level):
    if guess > number:
        print("Too High. Guess lesser value")
        return level - 1
    elif guess < number:
        print("Too Low. Guess higher value")
        return level - 1
    else:
        print(
            f"You`ve guessed correct. The computer guessed number is {number}")


def game():
    print(logo)
    print("Welcome to  Magical Number Guessing Game!")
    print("I am thinking of a number between 1 to 100")
    number = randint(1, 100)
    print(f"Computer`s number is {number}")
    # Choose difficulty
    level = choose_difficulty()
    # We need number, guess and level
    guess = 0
    while guess != number:
        print(f"You have {level} attempts remaining to guess the number")
        guess = int(input("Make a guess => "))
        level = game_engine(number, guess, level)
        if level == 0:
            print(
                f"Your attempts comes to an end. Better luck next time. Computer guessed number is {number}")
            return    
        elif guess !=number:
            print("Guess again!")        


game()

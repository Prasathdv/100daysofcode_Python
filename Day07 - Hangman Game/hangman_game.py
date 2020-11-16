# This module is all about creating a 'Hangman Game' from the concepts of loops (for, while), conditions (if, elif, else), functions.
# Game rules : User has to guess letters to find out words. For each incorrect letters , game lives will be reduced and finally you lose after 6 lives. Correct guesses led you to win the game.

# import section
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Intilaization section
words_list = word_list
chosen_word = random.choice(words_list)
word_length = len(chosen_word)
end_of_game = False
game_lives = 6
display = []

# Display hangman Game logo
print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# create a empty("_") list equivalent to chosen word length
for _ in range(word_length):
    display += "_"


# Game Logic - Core game engine section
while not end_of_game:
    # Get input guess from user
    guess = input("Guess a letter: ").lower()
    # Check if the guessed letter already entered by user. If so alert.
    if guess in display:
        print(f"'{guess}' is already guessed letter. Please try other words!")
    # Check guessed letter.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    # Check if guessed letter is not in chosen word. if so reduce game live by 1 and alert.
    if guess not in chosen_word:
        game_lives -= 1
        print(
            f"'{guess}' is not in chosen word. You have lost a game life. Current life left is :{game_lives}")
        print(stages[game_lives])
        if game_lives == 0:
            end_of_game = True
            print("Game Over!! Better luck next time")
            print(f"Correct word is: '{str(chosen_word)}'")
    # Display the guess string
    print(f"{' '.join(display)}")
    # Check if user guessed all leters and end game
    if "_" not in display:
        end_of_game = True
        print("You Win!")

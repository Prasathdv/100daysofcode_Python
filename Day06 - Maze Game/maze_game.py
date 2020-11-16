# This is an amazing maze game constructed using while loop and if/elif/else loop.
#  Actual source code will work in this url => https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

'''
Write a program using an if/elif/else statement so Reeborg can find the exit. 
The secret is to have Reeborg 
a. follow along the right edge of the maze, 
b. turning right if it can, 
c. going straight ahead if it can’t turn right, 
d. or turning left as a last resort.
What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).
'''
#


def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

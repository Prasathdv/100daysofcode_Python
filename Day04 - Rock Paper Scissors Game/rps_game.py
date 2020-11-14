# This is Classical Rock paers Scissors game.
# Official Rules of RPS => https://www.wrpsa.com/the-official-rules-of-rock-paper-scissors/
# This game uses randomization logic and list data type

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

rps_option = int(input("What do you chose? 0.Rock 1.Paper 2.Scissors\n"))

print(rps[rps_option])
print("Computer chose")
computer_option = random.randint(0, 2)
print(rps[computer_option])

# rps game logic
# Rock(0) wins against scissors(2).
# Scissors(2) win against paper(1).
# Paper(1) wins against rock(0).

if rps_option == 0 and computer_option == 1:
  print("Computer Wins!")
elif rps_option == 0 and computer_option == 2:
  print("you Win!")
elif rps_option == 1 and computer_option == 0:
  print("You Win!")     
elif rps_option == 1 and computer_option == 2:
  print("Computer Wins!")   
elif rps_option == 2 and computer_option == 0:
  print("Computer Wins!")
elif rps_option == 2 and computer_option == 1:
  print("You Win!")  
elif rps_option == computer_option:
  print("Game Draw!!")    

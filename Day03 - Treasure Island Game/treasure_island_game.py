print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

left_right = input(
    "You`re at a cross road. Where do you want to go? type left or right ")

if left_right == "left":
    swim_wait = input(
        "You come to a lake.There is an island in middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across")
    if swim_wait == "wait":
        which_door = input(
            "Welcome to Treasure island fort.Infront of you are three doors painted in Blue, Red and Yellow. Choose wisely and see your destiny!")
        if which_door == "Red":
            print('''
                (  .      )
                )           (              )
                        .  '   .   '  .  '  .
                (    , )       (.   )  (   ',    )
                .' ) ( . )    ,  ( ,     )   ( .
            ). , ( .   (  ) ( , ')  .' (  ,    )
            (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
        jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
            print("Oh No!!... You are burned by Fire!!... Game Over!!")
        elif which_door == "Blue":
            print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
            ''')
            print("Eaten by Beasts!!.. Aaghhhh.... Burp!!... Game Over!!")
        elif which_door == "Yellow":
            print("You Win!!..You`ve found your  destiny wisely.. Take the treasure with you... Let`s see how would you manage to escape this island .. he he...")

        else:
            print("Game Over you idiot!!!")
    else:
        print("He He He.... You are attacked by Trout!!.. Game Over!!")
else:
    print("Ha ha ha ..... You Fell into deep well . Game Over!!")

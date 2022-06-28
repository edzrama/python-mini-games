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
play = True
while play:
    crossroad = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"")
    if crossroad == "right":
      print("you fall into a hole. Game Over")
    else:
      action = input("You've come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
      if action == "swim":
        print("Attacked by a trout. Game Over")
      else:
        door = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?")
        if door == "red":
          print("Burned by Fire. Game Over")
        elif door == "blue":
          print("Eaten by Beasts. Game Over")
        elif door == "yellow":
          print("You Win!")
        else:
          print("Invalid Pick. Game Over")
    continue_playing = input("Play again? Y/N \n").lower()
    if continue_playing != "y":
        play = False
        print("Game Ended!")
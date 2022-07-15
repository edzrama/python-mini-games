from random import randint

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
play = True
action = [rock, paper, scissors]
while play:
    robot = randint(0, 2)
    user_in = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    if int(user_in) > 2:
        print("Invalid input")
    else:
        print(action[int(user_in)])
        print(f"computer chose: \n{action[robot]}")

        if robot == int(user_in):
            print("draw")
        elif (int(user_in) == 0 and robot == 2) or (int(user_in) == 2 and robot == 1) or (int(user_in) == 1 and robot == 0):
            print("You win!")
        else:
            print("You lose!")
    continue_playing = input("Play again? Y/N \n").lower()
    if continue_playing != "y":
        play = False
        print("Game Ended!")

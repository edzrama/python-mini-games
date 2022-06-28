from art import logo
import os
import random

play = "y"
while play == "y":
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20!")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    random_num = random.randint(1, 20)
    match = False
    if difficulty.lower() == 'easy':
        lives = 10
    elif difficulty.lower() == 'hard':
        lives = 5
    else:
        lives = 0
        match = True
        print('Wrong Input')
        play = input("Play again? type 'y' or 'n': ")

    while not match:
        if lives != 0:
            print(f"You have {lives} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if random_num == guess:
                print(f"You got it! The Answer is {random_num}")
                match = True
                play = input("Play again? type 'y' or 'n': ")
            elif random_num > guess:
                print("Too low.")
                lives -= 1
                if lives != 0:
                    print("Guess again")
            elif random_num < guess:
                print("Too high.")
                lives -= 1
                if lives != 0:
                    print("Guess again")
        else:
            print("You run out of guesses, you lose")
            play = input("Play again? type 'y' or 'n': ")
            match = True

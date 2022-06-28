import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_list = None
bot_list = None
play = True
hit = True
invalid_input = True


def deal_cards():
    global user_list
    global bot_list
    print(logo)
    user_list = []
    bot_list = []
    user_list.append(random.choice(cards))
    user_list.append(random.choice(cards))
    while sum(bot_list) < 17:
        bot_list.append(random.choice(cards))
    calculate_score()


def calculate_score():
    global hit
    global invalid_input
    if sum(user_list) == 21 and sum(bot_list) == 21:
        print_final("draw")
    elif sum(user_list) == 21:
        print_final("BlackJack! You Win")
    elif sum(bot_list) == 21:
        print_final("BlackJack! You Lose")
    elif sum(user_list) > 21:
        print_final("You went over. You lose")
    elif sum(bot_list) > 21:
        print_final("Computer went over. You Win")
    else:
        if hit:
            print(f"your cards: {user_list}, current score: {sum(user_list)}")
            print(f"computer's first: {len(bot_list)}")

            while hit and sum(user_list) < 21 or invalid_input:
                question = input("Type 'y' to get another card, type 'n' to pass:")
                if question.lower() == "y":
                    invalid_input = False
                    user_list.append(random.choice(cards))
                    calculate_score()
                elif question.lower() == "n":
                    invalid_input = False
                    hit = False
                    calculate_score()
                else:
                    invalid_input = True
        else:
            user_count = sum(user_list)
            bot_count = sum(bot_list)
            if user_count > bot_count:
                print_final("You Win")
            elif user_count < bot_count:
                print_final("You Lose")
            else:
                print_final("draw")


def print_final(message):
    print(f"your final hand: {user_list}, final score: {sum(user_list)}")
    print(f"computer's final hand: {bot_list}, final score: {sum(bot_list)}")
    print(message)


while invalid_input:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play.lower() == "y":
        invalid_input = False
        while play == "y":
            deal_cards()
            play = input("play again? Type 'y' or 'n': ")
    elif play.lower() == "n":
        invalid_input = False
        print("Game Ended")
    else:
      print("Invalid input")

from game_data import data
import art
import random

score = 0
compare_a = random.choice(data)
play = True
while play:
    compare_b = random.choice(data)
    print(f"{compare_a['name']}, a {compare_a['description']} from {compare_a['country']}")
    print(art.vs)
    print(f"{compare_b['name']}, a {compare_b['description']} from {compare_b['country']}")
    repeat = True
    while repeat:
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == 'A':
            repeat = False
            if compare_a['follower_count'] > compare_b['follower_count']:
                score += 1
                print(f"You're right, current score: {score}")
                compare_a = compare_b
            else:
                print(f"Sorry, that's wrong answer, final score: {score}")
                play = False
        elif answer == 'B':
            repeat = False
            if compare_b['follower_count'] > compare_a['follower_count']:
                score += 1
                print(f"You're right, current score: {score}")
                compare_a = compare_b
            else:
                print(f"Sorry, that's wrong answer, final score: {score}")
                play = False
        else:
            print("Invalid Input")


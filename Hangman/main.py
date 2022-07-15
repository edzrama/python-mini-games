import random
import hangman_art
import hangman_words

# from hangman_words import word_list - if you wish to access the variable directly
word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo
print(logo)
play = True

while play:
    # Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    chosen_word = list(random.choice(word_list).lower())
    # Current lives / initial value = 6
    lives = 6
    # For each letter in the chosen_word, add a "_" to 'display'. So if the
    # chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
    display = ["_" for _ in chosen_word]
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    while '_' in display and lives >= 1:
        guess = input("Guess a letter: ").lower()
        # Loop through each position in the chosen_word;
        # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        found = False
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = letter
                found = True
        if not found:
            lives -= 1
            print(stages[lives])

        # Print 'display' and you should see the guessed letter in the correct position and every other letter replace
        # with "_".
        print(display)
    if lives == 0:
        print("You lose!")
    else:
        print("You win!")
    continue_playing = input("Play again? Y/N \n").lower()
    if continue_playing != "y":
        play = False
        print("Game Ended!")

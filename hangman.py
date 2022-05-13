# Hangman Game

import random

NUMBER_OF_TRIES = 10
# Maximum number of tries allowed

def pick_random_word():
# Opens words.txt and returns a random word - to add/change words to pick from, simply edit words.txt
    text_file = open("words.txt", "r")
    word_list = text_file.readlines()
    random_word = random.choice(word_list)

    return random_word.strip()

def display_letters_from_word(random_word, letter_list):
    # Receives as arguments the the random word and the list of letters to check the word against
    # Checks the received letters against the word, adding the letter or an underscore to an empty string.
    random_word = random_word.upper()
    empty_str = ""

    for letter in random_word:
        if letter in letter_list:
            empty_str += letter + " "
        else:
            empty_str += "_ "
    
    return empty_str, random_word

def play_game():
    # Receives letter input from player, adding to a list which is then passed into display_letters_from_word().
    # Returns the number of tries left to win the game - if the player runs out of tries, it returns 0.
    letter_list = []
    random_word = pick_random_word()
    tries = NUMBER_OF_TRIES
    print("**HANGMAN**")
    for letter in random_word:
        print("_ ", end="")

    while tries != 0:
        print()
        letter = input("GUESS A LETTER: ").upper()
        letter_list.append(letter)
        game_word, random_word = display_letters_from_word(random_word, letter_list)
        print(game_word)

        if letter not in random_word:
            tries -= 1

        if '_' not in game_word:
            return tries, game_word
        
        print("\nGUESSED LETTERS: " + str(letter_list))
        print("YOU HAVE " + str(tries) + " TRIES LEFT.")

    return 0, random_word

def main():
    result, random_word = play_game()
    if result == 0:
        print("GAME OVER!")
        print("THE WORD WAS: " + random_word)
    else:
        print("YOU WIN!")

if __name__ == "__main__":
    main()
    
# Charlie Conneely
# Anagram game

import dictionary_parser
from rachel import Rachel
from dictionary import Dictionary

def main(name):
    original_letters = []
    other_words = []
    dictionary = Dictionary()
    rachel = Rachel()

    # retrieve array of letters
    nine_letters = rachel.give_the_letters(9)
    for l in nine_letters:
        original_letters.append(l)
    print(''.join(nine_letters).upper())


    input_word = input("Enter your word: ")
    input_word = input_word.lower()

    # check if each letter sees itself on the board
    found = dictionary.compare_words(nine_letters, input_word)

    if found:
        # check if the word is in the dictionary
        message = dictionary.check_word(name, input_word)
        print(message)

    other_words = dictionary.find_other_words(original_letters)

    print("\nHere are some words we found: ")
    for word in other_words:
        print(word)

def intro():
    name = str(input("Enter your name here: "))
    print("Welcome "+name+"!\nLet's Play Countdown!!\n")
    return name

if __name__ == "__main__":
    name = intro()
    ready_to_play = True
    while True:
        if ready_to_play:
            main(name)

        choice = input("\nWould you like to play again? (y/n):")
        choice = choice.lower()
        if choice not in ["y", "n"]:
            ready_to_play = False
            print("Invalid input. Please try again.")
        elif (choice == 'y'):
            ready_to_play = True
        else:
            break


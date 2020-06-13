# Charlie Conneely
# Countdown.py

import dictionary_parser
from rachel import Rachel
from dictionary import Dictionary

class Countdown():

    def countdown(self, name):
        original_letters = []
        other_words = []
        dictionary = Dictionary()
        rachel = Rachel()
        points = 0

        # retrieve array of letters
        nine_letters = rachel.give_the_letters(9)
        for l in nine_letters:
            original_letters.append(l)
        print(''.join(nine_letters).upper())

        input_word = input("Enter your word: ").lower()

        # check if each letter sees itself on the board
        found = dictionary.compare_words(nine_letters, input_word)

        if found:
            # check if the word is in the dictionary
            present = dictionary.check_word(name, input_word)
            if present:
                message = dictionary.check_length(name, input_word)
                print(message)
                points = len(input_word)
        else:
            print("This word isn't present!")

        other_words = dictionary.find_other_words(original_letters)

        if len(other_words) == 0:
            print("\nWe didn't find anything worth noting!\n")
        else:
            # sort list of words - biggest at top
            other_words.sort(key=len, reverse=True)
            print("\nHere are some words we found: ")
            for word in other_words:
                print("- "+word)
        return points

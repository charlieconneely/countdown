# Charlie Conneely
# Countdown.py

import dictionary_parser
from rachel import Rachel
from dictionary import Dictionary

dictionary = Dictionary()
rachel = Rachel()

class Countdown():

    """
    Retrieve random nine letters from Rachel class
    Output letters to console
    Receive input word
    Calculate points by calling check_word
    Call display_other_words
    return points
    """
    def play_countdown(self, name):
        original_letters = []
        nine_letters = []
        original_letters = []
        # retrieve array of letters
        nine_letters = rachel.give_the_letters(9)
        for l in nine_letters:
            original_letters.append(l)
        print(''.join(nine_letters).upper())
        input_word = input("Enter your word: ").lower()
        points = self.check_word(nine_letters, input_word, name)
        self.display_other_words(original_letters)

        return points

    """
    Collect potential words from dictionary class
    Output results to console
    """
    def display_other_words(self, letters):
        other_words = []
        other_words = dictionary.find_other_words(letters)
        if len(other_words) == 0:
            print("\nWe didn't find anything worth noting!\n")
        else:
            # sort list of words - biggest at top
            other_words.sort(key=len, reverse=True)
            print("\nHere are some words we found: ")
            for word in other_words:
                print("- "+word)

    """
    Check if word exists in the nine letters
    Check if word exists in dictionary
    """
    def check_word(self, letters, word, name):
        points = 0
        # check if each letter sees itself on the board
        found = dictionary.compare_words(letters, word)
        if found:
            # check if the word is in the dictionary
            present = dictionary.check_dictionary(word) 
            if present:
                print(dictionary.check_length(name, word))
                points = len(word)
            else:
                print("Word not found in dictionary.")
        else:
            print("This word isn't present!")
        return points


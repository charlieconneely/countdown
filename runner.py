# Charlie Conneely
# Anagram game

import dictionary_parser
import random

def main(name):
    words = dictionary_parser.parse("words.txt")
    found = True

    # retrieve array of letters
    nine_letters = rachel()
    # convert array to string
    nine_letters_string = ''.join(nine_letters)
    # convert to uppercase
    #nine_letters_string = nine_letters_string.upper()
    print(nine_letters_string)

    input_word = input("Enter your word: ")
    # convert to upper case
    input_word = input_word.upper()
    # convert word to array of chars for inspection
    input_word_split = split(input_word)

    # check if each letter sees itself on the board
    for char in input_word_split:
        # check if the letter is present on the board
        if char in nine_letters:
            # remove the letter from the board
            nine_letters.remove(char)
        else:
            found = False

    if found:
        # convert word back to lower
        input_word = input_word.lower()
        # check if the word is in the dictionary
        if input_word in words:
            if (len(input_word) < 6):
                print("Good job "+name+"! Length: " +\
                        str(len(input_word)))
            else:
                print("Great word "+name+"! Length: "\
                        + str(len(input_word)))
        else:
            print("Word not found in dictionary")
    else:
        print("Word not present")

# convert string to list of chars
def split(word):
    return [char for char in word]

def rachel():
    x = 0
    letters = []
    vowels = ['A','E','I','O','U']
    consonants = ['B','C','D','F','G','H','J','K','L','M',
            'N','P','Q','R','S','T','V','X','Z','W','Y']

    print("\nRachel, the letters please!\n")

    while x < 9:
        choice = input("Vowel or Consonant? (v/c): ")
        choice = choice.lower()
        if choice == 'v':
            # generate random number
            letternum = random.randint(0, len(vowels)-1)
            # select vowel at that index
            letter = vowels[letternum]
            # append letter to list of letters
            letters.append(letter)
            x = x + 1
            print(letter)
        elif choice == 'c':
            # generate random number
            letternum = random.randint(0, len(consonants)-1)
            # select consonant at that index
            letter = consonants[letternum]
            # append letter to list of letters
            letters.append(letter)
            print(letter)
            x = x + 1
        else:
            print("Invalid entry. Try again.")
    return letters

def intro():
    name = str(input("Enter your name here: "))
    print("Welcome "+name+"!!\nLet's Play Countdown!\n")
    return name

if __name__ == "__main__":
    name = intro()
    while True:
        main(name)
        while True:
            choice = input("\nWould you like to play again? (y/n):")
            choice = choice.lower()
            if choice == 'n' or choice == 'y':
                break
            else:
                print("Invalid input. Please try again.")
        if (choice == 'n'):
            break



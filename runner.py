# Charlie Conneely
# Anagram game

import dictionary_parser
from rachel import Rachel

dictionary = dictionary_parser.parse("words.txt")

def main(name):
    words = dictionary
    found = True

    rachel = Rachel()
    # retrieve array of letters
    nine_letters = rachel.give_the_letters(9)
    # convert array to string
    nine_letters_string = ''.join(nine_letters)
    print(nine_letters_string)

    input_word = input("Enter your word: ")
    # convert to upper case
    input_word = input_word.upper()
    # convert word to array of chars for inspection
    input_word_split = list(input_word)

    # check if each letter sees itself on the board
    for char in input_word_split:
        # check if the letter is present on the board
        if char in nine_letters:
            # remove the letter from the board
            nine_letters.remove(char)
        else:
            found = False
            print("The letters used don't match with the given ones")
            break

    if found:
        # convert word back to lower
        input_word = input_word.lower()
        # check if the word is in the dictionary
        if input_word in words:
            if (len(input_word) < 6):
                print("Good job {}! Length: {}".format(name, len(input_word)))
            else:
                print("Great word {}! Length: {}".format(name, len(input_word)))
        else:
            print("Word not found in dictionary")

    find_other_words(nine_letters)

def get_random_vowel():
    vowels = ['A','E','I','O','U']
    # generate random number
    letternum = random.randint(0, len(vowels)-1)
    # select vowel at that index
    letter = vowels[letternum]
    return letter

def get_random_consonant():
    consonants = ['B','C','D','F','G','H','J','K','L','M',
                  'N','P','Q','R','S','T','V','X','Z','W','Y']
    # generate random number
    letternum = random.randint(0, len(consonants)-1)
    # select consonant at that index
    letter = consonants[letternum]
    return letter

def find_other_words(letters):
    word_found = True
    others = set()
    letters_original = letters
    for word in dictionary:
        if len(word) > 4:
            letters = letters_original
            split_word = list(word)
            for c in split_word:
                if c in letters:
                    letters.remove(c)
                else:
                    word_found = False
                    break
        if word_found:
            others.add(word)


    return others

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


# Charlie Conneely
# Anagram game

import dictionary_parser
import random

# TO DO
# check if users word is within the nine letters provided

def main():
    words = dictionary_parser.parse("words.txt")
    found = True

    nine_letters = rachel()
    # convert array to string
    nine_letters_string = ''.join(nine_letters)
    # convert to uppercase
    nine_letters_string = nine_letters_string.upper()
    print(nine_letters_string)

    input_word = input("Enter your word: ")
    input_word_split = split(input_word)

    # Check if each character sees itself in the nine_letters
    for char in input_word_split:
        if char in nine_letters:
            nine_letters.remove(char)
        else:
            found = False

    if input_word in words and found == True:
        if (len(input_word) < 6):
            print("Good job! Length: " + str(len(input_word)))
        else:
            print("Great word! Length: " + str(len(input_word)))
    else:
        print("word not found")

# convert string to list of chars
def split(word):
    return [char for char in word]

def rachel():
    x = 0
    letters = []
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m',
                'n','p','q','r','s','t','v','x','z','w','y']

    while x < 9:
        choice = input("Vowel or Consonant? (v/c): ")
        if choice == 'v':
            letternum = random.randint(0, len(vowels)-1)
            letter = vowels[letternum]
            letters.append(letter)
            print(letter)
            x = x + 1
        elif choice == 'c':
            letternum = random.randint(0, len(consonants)-1)
            letter = consonants[letternum]
            letters.append(letter)
            print(letter)
            x = x + 1
        else:
            print("Invalid entry. Try again.")
    return letters

if __name__ == "__main__":
    main()



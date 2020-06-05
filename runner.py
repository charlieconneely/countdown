# Charlie Conneely
# Anagram game

import dictionary_parser
import random

# TO DO
# check if users word is within the nine letters provided

def main():
    words = dictionary_parser.parse("words.txt")
    found = False

    nine_letters = rachel()
    # convert array to string
    nine_letters = ''.join(nine_letters)
    # convert to uppercase
    nine_letters = nine_letters.upper()
    print(nine_letters)

    input_word = input("Enter your word: ")

    if input_word in words:
        found = True

    if found:
        if (len(input_word) < 6):
            print("Good job! Length: " + str(len(input_word)))
        else:
            print("Great word! Length: " + str(len(input_word)))
    else:
        print("word not found")

def rachel():
    x = 0
    letters = []
    vowels = ['a','e','i','o','u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w','y']

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



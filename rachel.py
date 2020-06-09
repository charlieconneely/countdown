from random import randint

class Rachel:
    def __init__(self):
        self.letters = []

    def __get_random_vowel(self):
        vowels = ['A','E','I','O','U']
        # generate random number
        random_number = randint(0, len(vowels)-1)
        # select vowel at that index
        letter = vowels[random_number]
        return letter

    def __get_random_consonant(self):
        consonants = ['B','C','D','F','G','H','J','K','L','M',
                      'N','P','Q','R','S','T','V','X','Z','W','Y']
        # generate random number
        random_number = randint(0, len(consonants)-1)
        # select consonant at that index
        letter = consonants[random_number]
        return letter

    def give_the_letters(self, number_of_letters):

        print("\nRachel, the letters please!\n")
        quantity_of_letters_given = 0
        while quantity_of_letters_given < number_of_letters:
            choice = input("Vowel or Consonant? (v/c): ")
            choice = choice.lower()
            valid_choices = { 'v': self.__get_random_vowel(), 'c': self.__get_random_consonant() }
            if choice in valid_choices:
                letter = valid_choices[choice]
                self.letters.append(letter)
                quantity_of_letters_given += 1
                print(letter)
            else:
                print("Invalid entry. Try again.")

        return self.letters

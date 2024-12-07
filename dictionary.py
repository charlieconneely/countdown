# Charlie Conneely

import requests, dictionary_parser

dictionary = dictionary_parser.parse("words.txt")

class Dictionary:
    def __init__(self):
        self.words = []
        self.message = ''
        self.dictionary = dictionary

    """
    Check if word exists

    returns Boolean
    """
    def check_dictionary(self, word):
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
        response = requests.get(url)
        if response.status_code == 404:
            return False
        elif response.status_code >= 400:
            print(f'API request failed with status {response.status_code}')
            exit(0)
        return True
    """
    Check length of word
    
    returns String 
    """
    def check_length(self, name, word):
        if (len(word) > 5):
            message = f'Great work {name}! Length: {str(len(word))}'
        else:
            message = f'Good job {name}! Length: {str(len(word))}'
        return message

    """
    Loop through all words (>4 chars) in dictionary

    returns Array - Words that exist in the 9 letters
    """
    def find_other_words(self, letters):
        original_letters = []
        self.words = []
        # back-up original 9 letters
        for l in letters:
            original_letters.append(l)

        for word in dictionary:
            if (len(word) >= 4):
                # clear array
                letters = []
                # restore array
                for l in original_letters:
                    letters.append(l)
                word_found = self.compare_words(letters, word)
                #letters = [] # clear array
                if word_found:
                    self.words.append(word)
        return self.words

    """
    Compare word and letters character by character to check for a match

    returns Boolean
    """
    def compare_words(self, letters, word):
        found = True
        split_word = list(word)
        for c in split_word:
            if c in letters:
                letters.remove(c)
            else:
                found = False
                break
        return found



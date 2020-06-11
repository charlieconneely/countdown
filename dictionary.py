# Charlie Conneely

import dictionary_parser

dictionary = dictionary_parser.parse("words.txt")

class Dictionary:
    def __init__(self):
        self.words = []
        self.message = ""

    def check_word(self, name, word):
        word = word.lower()
        if word in dictionary:
            self.message = self.check_length(name, word)
        else:
            self.message = "Word not found in dictionary."
        return self.message

    def check_length(self, name, word):
        if (len(word) > 5):
            message = "Great work "+str(name)+"! Length: " + str(len(word))
        else:
            message = "Good job "+str(name)+"! Length: " + str(len(word))
        return message

    def find_other_words(self, letters):
        original_letters = []
        # back-up original 9 letters
        for l in letters:
            original_letters.append(l)

        for word in dictionary:
            if (len(word) > 5):
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




from dictionary import Dictionary

class PangramFinder():

    def __init__(self, letters, centre_letter):
        letters = letters.strip().lower()
        l = list(letters)
        self.letters = l
        self.centre_letter = centre_letter
        self.d = Dictionary()

    def find_pangram(self):
        found_one = False
        for w in self.d.dictionary:
            if len(w) < len(self.letters): continue
            
            # if dictionary word has a letter that self.letters does not - skip 
            skip = False
            for letter in list(w):
                if letter not in self.letters:
                    skip = True
                    break

            if skip: continue

            match = True
            for l in self.letters:
                if l not in list(w):
                    match = False
                    break
            if match == True:
                found_one = True
                print(f'- {w}')

        if found_one == False: print('None found.')

        self.display_other_notable_words()

    def display_other_notable_words(self):
        others = []

        for word in self.d.dictionary:
            if len(list(word)) < 4: continue
            if self.centre_letter not in word:
                continue
            match = True
            for letter in list(word):
                if letter.lower() not in self.letters:
                    match = False
                    break
            if match:
                others.append(word)

        if len(others) == 0:
            print('No other notable words found.')
        else:
            others = sorted(others, key=len)
            print('Other notable words found:')
            for o in others:
                print(f'- {o}')

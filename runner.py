# Charlie Conneely
# Anagram game

import dictionary_parser

def main():
    words = dictionary_parser.parse("words.txt")
    x = 0
    for word in words:
        x = x + 1
    print(x)

if __name__ == "__main__":
    main()



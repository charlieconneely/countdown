# Charlie Conneely
# Dictionary parser file

"""
Parse contents of file
Return array of all words  
"""
def parse(f):
    file = open(f, "r")
    words = file.read().split()
    file.close()
    return words

if __name__ == "__main__":
    print("please run runner.py instead")

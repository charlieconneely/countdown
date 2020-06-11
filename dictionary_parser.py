# Charlie Conneely
# Dictionary parser file

def parse(f):
    file = open(f, "r")
    words = file.read().split()
    file.close()

    x = 4
    return words

if __name__ == "__main__":
    print("please run runner.py instead")

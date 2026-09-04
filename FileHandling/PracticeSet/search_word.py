import sys

def Searc_word(word,string):
    return string.count(word)

if __name__ == "__main__":
    filename = sys.argv[1]
    word = sys.argv[2]
    with open(filename) as f:
        string = f.read()
        n = Searc_word(word,string)
        print(f"There are {n} occurence in {word} and filename is {filename}")
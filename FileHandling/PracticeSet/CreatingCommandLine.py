import sys

def Count_line(filename):
    with open(filename) as f:
        return len(f.readline())

if __name__ == "__main__":
    filename = sys.argv[1]
    num_line = Count_line(filename)
    print(f"Code line was {num_line} and file is {filename}")
    
    
# print(len("Learning python is fun now!!")) //28 words
# try:
#     File = open("FileHandling/PracticeSet/notes.txt","w")

#     content = File.write("Learning python is fun now!!")

#     print(content)
# except FileNotFoundError:
#     print("File not found")

try:
    FileRead = open("FileHandling/PracticeSet/notes.txt", "r")
    Read = FileRead.read()
    print(Read)

except FileNotFoundError:
    print("Not found")
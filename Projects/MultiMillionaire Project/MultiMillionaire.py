try:
    questions = [
        ["Which of these is a Microsoft Office application?", "Google Chrome", "MS Word", "VLC Player", "Photoshop", 2],
        ["Which software is mainly used for spreadsheets?", "MS Paint", "MS Excel", "Notepad", "Calculator", 2],
        ["Which one is used to send and receive emails?", "MS Paint", "Calculator", "Email", "File Explorer", 3],
        ["Which key is used to create a new line in MS Word?", "Shift", "Enter", "Ctrl", "Alt", 2],
        ["Which of the following is an input device?", "Keyboard", "Monitor", "Printer", "Speaker", 1]
        ]
    
    prizes = ["100","200","300","400","500"]
    
    i = 0
    for question in questions:
        print(f"{question[0]}")
        print(f"a) {question[1]}")
        print(f"b) {question[2]}")
        print(f"c) {question[3]}")
        print(f"d) {question[4]}")

        a = int(input("Choose you Answer : 1 for a, 2 for b, 3 for c, 4 for d : "))
        if (question[5] == a):
            print(f"Hurry,correct answer")
        else:
            print(f"your answer is wrong the correct answer is {question[5]}")
            
            break
        print(f"You won the price is {prizes[i]} ")
        i += 1
except Exception as e:
    print(f"Error is : {e}")
    
    
    
# print(questions)
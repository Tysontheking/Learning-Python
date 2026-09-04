try:
    AppendText = open("FileHandling/DemoWritefile.txt","a")
    AppendText1 = "I just append this text for check"
    content = AppendText.write(AppendText1)
    print(content)
    AppendText.close()
except FileExistsError:
    print("File Does not here!")
WriteDemo = open("FileHandling/DemoWritefile.txt","w")

DemoText = '''Hey Today is a rakshabandhan Festival and i'm just learning new topin in python and today wheather is also so good today is 28/08/2026'''

File = WriteDemo.write(DemoText)


print(File)
WriteDemo.close()
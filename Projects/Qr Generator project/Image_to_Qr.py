import qrcode

url = input("Enter your Url to get Qr code : ")
filename = input("Enter file name : ")

if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)
     
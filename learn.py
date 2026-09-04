# print("satyam")

# name = input("enter your name")

# print("Hello owner "+name)

# all dataTypes in python

# int
# float
# str
# bool
# list
# tuple
# set
# dict
# None

# lets learn int or float

# print(type(10 + 10))
# print(type(10.5 + 10.5))

# operator precedence in python

# print((5 + 4) * 10 / 2) #45

# print(((5 + 4) * 10) / 2) #45

# print((5 + 4) * (10 / 2)) #45

# print(5 + (4 * 10) / 2) #25

# print(5 + 4 * 10 // 2) 


# print(bin(5), 2)

# augmented assigment operator

aug = 10
aug /= 2
# print(aug)

hello = "\rHey just i'm saying \n\"hello to everyone\""

# print(hello)

#formatted string

name = 'satyam'
age = 21

# print(f"hey my name is {name}, i'm {age} year old!")

# print("Hey my name is {0} and i'm {1} years old".format({name},{age}))


from datetime import datetime

date = datetime.today()

# print(f"Today is {date : %b , %d, %y}")


pen =  "Hey just i'm saying hello to everyone"
# print(pen[::-1])

# methodas in python

# print(pen.center(0, "*"))

# print(pen.capitalize())


# print(pen.endswith("everyone"))


# birthdate = input("enter your birthdate in dd/mm/yyyy format: ")
# age = 2026 - int(birthdate.split("/")[1])
# # print(birthdate)
# print(f"your age is {age}")

# name = input("What is your Name : ")
# password = input("What is your Password : ") 
# password_length = len(password)
# pasword_hidden = '*' * password_length

# print(password)

# print(f"Hey {name} you created your password {pasword_hidden} and the length is {len(password)}")

list1 = 'satyam'
# print(list1[0:1])

matrix = [
    [['satyam', 'kumar'],1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[0][2]) #satyam

basket = ['apple', 'banana', 'orange', 'grapes']
basket.sort()
basket.reverse()
basket[::-1]
# print(basket)

# a = int(input("enter your Number : "))
# b = input("enter your Number : ")
# c = input("enter your Number : ")
# print(b + c)
# print(type(a))
# print(a + 10)

# print("Hello, World! Welcome to Python.")

# print("Twinkle, twinkle, little star,\nHow I wonder what you are!")

name = "Satyam"
age = 21
height = 5.9
student = True

# print(name, age, height, student)

num = "45"
newnum = int(num) + 10
# print(newnum)

# food = input("What is your favorite food? ")
# print("Your favorite food is " + food )

# print('Harry said, "Python is awesome!"\nThis is on a new line.\nThis is a tab \t\there')

# intuser = int(input("Enter a number: "))
# print("square of the number is: ", intuser*intuser)


# print("cube of the number is: ", intuser*intuser*intuser)

check = input("Enter a number: ")
# if(int(check) > 18):
#     print("You are eligible to vote.")
# elif(int(check) == 18):
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# if(check.isdigit()):
#     if(int(check) >= 18):
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote.")


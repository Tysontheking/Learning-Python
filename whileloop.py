
# i = 0
# while i in range(11):
#     print(i)
#     i += 1


# value = 0
# while value <10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Loop completed without break")

'''Print numbers from 1 to 10 using a while loop.'''

# num = 1
# while num in range(11):
#     print(num)
#     num += 1
    
    
'''Write a program that keeps asking the user to enter a password until they
enter the correct one.'''

# password = "satyam"
# user_int = ""

# while user_int != password:
#     user_int = input("Enter the password: ")
#     if user_int == password:
#         print("Access granted!")
#     else:
#         print("Incorrect password. Try again.")


reverse = int(input("Enter a string to reverse: "))

while reverse > 0:
    digit = reverse % 10
    print(digit, end="")
    reverse //= 10
    
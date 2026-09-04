# Rule = int(input("Enter a rule number (1-3): "))

# match Rule:
#     case 1:
#         print("Rule 1 matched")
#     case 21:
#         print("Rule 2 matched")
#     case 3:
#         print("Rule 3 matched")
#     case _:
#         print("No matching rule found")

# day = 6
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!")


# from unittest import case


# month = int(input("Enter the month number (1-12): "))
# day = int(input("Enter the day number (1-31): "))

# match day:
#     case 1 | 2 | 3 | 4 | 5 if month >= 6:
#         print("Today is a weekday in June")
#     case 1 | 2 | 3 | 4 | 5 if month != 6 and day == 4:
#         print("Today is a weekday but not in June")
#     case _:
#         print("Today is a weekend") 


'''Ask the user to enter a day number (1–7) and print the corresponding day of
the week using match case .'''

# Day = int(input("Enter a day number (1-7): "))

# match Day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number. Please enter a number between 1 and 7.")


'''Write a program using match case that simulates a simple calculator.
1. Ask the user for two numbers and an operation (+, -, *, /).
2. Perform the operation using match case .'''

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# match operation := input("Enter an operation (+, -, *, /): "):
#     case "+":
#         print(f"The result of {num1} + {num2} is: {num1 + num2}")
#     case "-":
#         print(f"The result of {num1} - {num2} is: {num1 - num2}")
#     case "*":
#         print(f"The result of {num1} * {num2} is: {num1 * num2}")
#     case "/":
#         print(f"The result of {num1} / {num2} is: {num1 / num2}")


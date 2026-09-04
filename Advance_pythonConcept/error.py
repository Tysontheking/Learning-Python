# while True:
#     try:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter another number: "))
#         # c = a + b
#         d = a / b
#         print(f"The Division of {a} and {b} is {d}.")
#     except ZeroDivisionError:
#         print("Change your second number, it cannot be zero.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
    # except ValueError:
    #     print("Please enter valid integers.")


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    d = a / b
    print(f"The Division of {a} and {b} is {d}.")
    # raise ValueError("An error occurred: ")
    
except Exception as e:
        print(f"An error occurred: {e}")

print("This block will always execute, regardless of whether an exception occurred or not.")
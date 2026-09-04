class NegativeNumberError(Exception):
    pass

def AskUser():
    while True:
        try:
            num = int(input("Enter a number: "))
            num1 = int(input("Enter a number: "))
            if num < 0 or num1 < 0:
                raise NegativeNumberError()
            
            print(f"You entered: {num/num1}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            break
        except ZeroDivisionError:
            print("You cannot divide by zero.")
            break
        except NegativeNumberError:
            print("You cannot enter negative numbers.")
            break

AskUser()
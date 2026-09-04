try:
    firstNum = int(input("Enter First Num : "))
    SecondNum = int(input("Enter Second Num : "))

    print(f"Choose your operator to perform Operation\n If you choose '+' For Addition\n If you choose '-' for subtraction\n If you choose '*' for multipication\n if you choose '/' devide")

    operation = input("Choose operation : ")
    match operation :
        case '+':
            print(f"Your Addition Value is : {firstNum + SecondNum}")
        case '-':
            print(f"Your Subtraction Value is : {firstNum - SecondNum}")
        case '*':
            print(f"Your Multipication Value is : {firstNum * SecondNum}")
        case '/':
            print(f"Your Division Value is : {firstNum / SecondNum}")
        case default:
            print("Choose correct operator")
except Exception as e:
    print(f"An error occurred: {e}")
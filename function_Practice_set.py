'''
1. Write a function greet() that prints "Hello, Python Learner!" when called.
'''
# def greet():
#     print("Hello, Python Learner!")
    
# greet()

# def square():
#     intput_num = int(input("Enter a number: "))
#     return intput_num ** 2

# print("The square of the number is: ", square())


'''
 
Write a function full_name(first, last) that takes first name and last nameas parameters and returns a single string in the format "First Last" .

'''

# def full_name(first, last):
#     return first + " " + last


# print(full_name("John", "Doe"))  # Output: John Doe

# def calculate_area(length, width = 10):
#     return length * width

# print(f"The area of rectangle is : {calculate_area(length=20, width=25)}" )


# def sqr_list():
#     av = [1,2,3,4,5]
#     def double(x):
#         return x * 2
#     return list(map(double,av))



# map_fun = list(map(lambda x : x*2, av))

# print(map_fun)


# def sqr_list():
#     av = [1, 2, 3, 4, 5]

#     def double(x):
#         return x * 2

#     return list(map(double, av))


# print(sqr_list())


# def factorial(n):

#     # Factorial is defined for non-negative integers
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")

#     # Base case: 0! = 1, so start result with 1
#     result = 1

#     # Multiply numbers from 1 to n
#     for i in range(1, n + 1):
#         result *= i

#     return result


# print("factorial(n) = ", factorial(2))


# def factorial():
#     n = int(input(" Enter a Num : "))
#     if n < 0:
#         raise ValueError("Number not be negative")
    
#     result = 1
    
#     for i in range(1,n+1):
#         result *= n

#     return result

# print(factorial())


# def summ_of_AllDigit(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + summ_of_AllDigit(n // 10)

# num = int(input("Enter All DigitToSum : "))
# print("Hurry : ", summ_of_AllDigit(num))

import math 

# num = 144
# sqr = math.sqrt(num)
# print(sqr)

# angle = 90

# sin = math.sin(math.radians(angle))
# print(sin)


# def increament():
#     n = 0
#     n += 1
#     print(n)

# increament()
# increament()
# increament()

# def docstring(a,b):
#     '''
#     here we just declare docstring to explore thing in docstrings
#     '''
#     return a*b

# print(docstring(2,3))
# print(docstring.__doc__)
# print(help(docstring))
    

# def fibonacci(n):
#     if n == 0 or n ==1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

# def safe_divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     else:
#         return int(a/b)

# print(safe_divide(2,0))







    




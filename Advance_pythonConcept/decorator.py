# A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.

# def deco(funt):
#     def wrapper():
#         print("Before calling function")
#         funt()
#         print("After calling function")

#     return wrapper

# @deco #@decorator syntax is a shorthand for greet = decorator(greet).

# def greet():
#     print("Hello world!!")

# greet()


# d = deco(greet)
# d()

# Decorator with Parameters

def arg(fun):
    def wrapper(*args, **kwargs):
        print('Argument before callling function')
        result = fun(*args, **kwargs)
        print('Argument after calling function')
        return result
    return wrapper

@arg
def add(a,b):
    return a+b

print(add(5,5))

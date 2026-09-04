'''
def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello!")
    
say_hello()
'''

from time import time
def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2 = time()
        print(f'Time taken to execute the function: {t2-t1} seconds')
    return wrapper
        
    
@timer
def sum_1m(n):
    sum_Num = 0
    for i in range(1, n+1):
        sum_Num += i
    return sum_Num

print(sum_1m(1000000))
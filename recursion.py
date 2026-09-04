'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 7

fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0) = 1 + 0 = 1
fib(3) = fib(2) + fib(1) = 1 + 1 = 2
fib(n) = fib(n-1) + fib(n-2) 
'''

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
    
    
# print(fib(5))

'''
fib(4) + fib(3)
fib(2) + fib(3) + fib(3)    
fib(0) + fib(1) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1
'''

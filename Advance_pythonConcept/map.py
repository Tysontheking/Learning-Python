# num = [1,2,3,4,5]

# def squ(x):
#     return x * x


# Double = list(map(squ, num))

# print(Double)


# s = ['1', '2', '3', '4', '5']

# res  = map(int,s)
# print(list(res))

# val = [1,2,3,4,5]

# lam = list(map(lambda x : x*x, val))

# print(lam)

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]


# addlam = list(map(lambda x,y : x+y, a,b))
# print(addlam)

#In this example, we use map() to convert a list of temperatures from Celsius to Fahrenheit.

celcius = [0, 10, 20, 30, 40]


ferhenheit = list(map(lambda x: (x * 9/5) + 32, celcius))

print(ferhenheit)
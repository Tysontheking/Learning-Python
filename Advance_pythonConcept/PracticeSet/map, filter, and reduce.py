map1 = [1, 2, 3, 4, 5] 

def cubes(x):
    return x ** 3

mapped = map(cubes, map1)
# print(list(mapped))


fil1 = [10, 11, 12, 13, 14]

def even(x):
    return x % 2 == 0

filtered = filter(even, fil1)
# print(list(filtered))


from functools import reduce

red1 = [1, 2, 3, 4, 5]

def add(x,y):
    return x + y

reduced = reduce(add, red1)
print(reduced)
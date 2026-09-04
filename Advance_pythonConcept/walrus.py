# num = [1,2,3,4,5,6,7,8,9,10]

# while (n:= len(num))> 0:
#     print(num.pop())
    
    
    
dic1 = [
    {'name':'sachin', 'age': 30},
    {'name':'rahul', 'age': 25},
    {'name':'virat', 'age': 35}
]

# without walras operator

# for entry in dic1:
#     name = entry.get('name')
#     if(name):
#         print(f"Name is {name}")

# for entry in dic1:
#     if(age := entry.get('age')):
#         print(f"Age is {age}")

foods = []


# while True:
#     f = input("Enter food name: ")
#     if(f == 'quit'):
#         break
#     foods.append(f)
    
while (food := input("Enter Food : ")) != 'quit':
    foods.append(food)
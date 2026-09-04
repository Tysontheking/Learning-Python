# List Practice_Quiestion

Fruits = ["apple", "banana", "cherry"] 

# print(Fruits[0])
# Fruits[1] = 'orange'
# print(Fruits)


# print(len(Fruits))

num_list = [1,2,3,4,5,6,7,8,9,10]
# print(num_list[0:3])
# print(num_list[:-4:-1])

#List_Methods

numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# numbers.remove(2)
# print(numbers)

# names = ["Alice", "Bob", "Charlie"]

# names.insert(0,"David")
# print(names)

#  Tuples and Operations on Tuples

coordinates = (10, 20)
# print(coordinates,type(coordinates))

# coordinates[0] = 50 #TypeError: 'tuple' object does not support item assignment
# print(coordinates)

# convert_list = list(coordinates)
# print(convert_list,type(convert_list))

# # print(convert_list)
# convert_list[0] = 50 
# coordinates = tuple(convert_list)
# print(coordinates)


#Sets and Set Methods

my_set = {1, 2, 3, 3, 4}
# print(my_set)
my_set.add(5)
my_set.remove(2)

# print(4 in my_set)

a = {1, 2, 3}
b = {3, 4, 5}

# c = a.union(b)
# c = a.intersection(b)
c = a.difference(b)
# print(c)


#Dictionaries and Dictionary Methods

student = {"name": "John", "age": 20, "grade": "A"}

# print(student["name"])
# student["grade"] = "+A"
student["city"] = "Delhi"
# print(student)


Friend_dic = {"Satyam":7982791645,"shivam":9205246267,"Mahender" : 8800672605}
# print(Friend_dic.keys())
# print(Friend_dic.values())

# for key,val in Friend_dic.items():
    # print(key,val)
    
    
# Bonus Challenges

# list1 = [1,2,3,2,4,5]
# # print(list1,type(list1))
# dup_sets = set(list1)
# list(dup_sets)
# print(dup_sets,type(dup_sets))

Price_Dic = {"TV" : 20000, "Mobile" : 15000, "Laptop" : 100000}

# highest_price = 0
# highest_product = ""

# for products in Price_Dic:
#     if Price_Dic[products] > highest_price:
#         highest_price = Price_Dic[products] 
#         highest_product = products

# print("Products = ",Price_Dic)
# print("Highest product = ", highest_product)
# print("Highest Price = ",highest_price)

# print(Price_Dic | Friend_dic)
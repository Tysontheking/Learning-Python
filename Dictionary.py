dic1 = {"name" : "satyam", "age" : 20} 
# /dictionary stores data in key:value format

# print(dic1, type(dic1))
# print(dic1["name"])

# print(dic1.get("age")) #ccessing a missing key with [ ] raises a KeyError, while get() is safer because it returns None (or a default value) instead of an error.

# print(dic1.get("state"))
# print(dic1["State"])


# New_dic = {"name" : "john"}
# New_dic["age"] = 23 
# New_dic["state"] = "Delhi" 

# print(New_dic)


# del dic1["age"]
# pop_age = dic1.pop("age")
# print(pop_age)
# print(dic1)

# print(dic1.popitem())


#Dictionary Comprehensions:
# Table_of_5 = {i : i * 5 for i in range(1,11)}
# print(Table_of_5)

# Square_of_num = {i : i**2 for i in range(1,11)}
# print(Square_of_num)

# print(dic1.keys())

# for keys in dic1:
#     print(keys)

# print(dic1.values())

# for val in dic1.values():
#     print(val)

# print(dic1.values(), dic1.keys())

# for key,val in dic1.items():
#     print(key,val,type(val))





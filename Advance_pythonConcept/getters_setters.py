'''
Getter: The getter method is used to retrieve the value of a private attribute. It allows controlled access to the attribute.
Setter: The setter method is used to set or modify the value of a private attribute. It allows you to control how the value is updated, enabling validation or modification of the data before it’s actually assigned.
'''


# class Get_info:
#     def __init__(self,Name,salary):
#         self.Name = Name
#         self.salary = salary
        
#     def full_info(self):
#         return f'job profile is {self.Name} and salary is {self.salary}'
    
#     def get_first_name(self):
#         First_Name = self.Name.split(' ') 
#         print(First_Name)
        
#         return First_Name[0]

# info = Get_info("satyam singh",18000)

# print(info.get_first_name())


class Get_Name:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def get_First_name(self):
        First = self.name.split(" ")
        print(First)
        return First[0]
    
FullName = Get_Name("satyam singh",18000)
# FullName.extra = "Woww Good Name"


print(FullName.get_First_name())

# print(FullName.extra)
class School:
    School_name = "ABC School"  # Class variable
    
    def __init__(self, teacher_name, salary):
        self.teacher_name = teacher_name  # Instance variable
        self.salary = salary  # Instance variable
    
    
    #instance method(default method also)
    def dis_details(self):
        print("School Name: ", School.School_name)  # Accessing class variable
        print("Teacher Name: ", self.teacher_name)  # Accessing instance variable
        print("Salary: ", self.salary)  # Accessing instance variable
     
    @staticmethod   
    def sumtonum(a,b):
        return a+b


Deatils = School("John Doe", 50000)
print("School Name: ", Deatils.School_name)  # Accessing class variable
# print("Teacher Name: ", Deatils.teacher_name)  # Accessing instance variable
# print(School.teacher_name)
# print("Salary: ", Deatils.salary)  # Accessing instance variable

# print(Deatils.dis_details())

print("Sum Num : ", Deatils.sumtonum(10,20))  # Accessing class method



#class methods

# class ClassMethods:
#     MyVarb = 0;
    
#     def __init__(self, myvar):
#         self.Variable = myvar
    
#     @classmethod
#     def class_method(cls,x):
#         cls.MyVarb += x
#         return cls.MyVarb
    
    
# obj1 = ClassMethods(10)

# print("Class Method : ", ClassMethods.class_method(5))
# print("Class Method : ", ClassMethods.class_method(15))






'''
A class defines what an object should look like, and an object is created based on that class. For example:

Class	Objects
Fruit	Apple, Banana, Mango
Car	    Volvo, Audi, Toyota

When you create an object from a class, it inherits all the variables and functions defined inside that class.

'''

# class school:
#     def students(self):
#         return 23
    
    
# s1 = school()
# print(s1.students())

class MyClass:
    x = 5

p1 = MyClass() #p1 is a object and MyClass is a class
print(p1.x)

del p1 # delete your object using del keyword
# print(p1.x)


# class Animal:
#     def speak(self):
#         return print("Animal Sound")

# class Dog(Animal):
#     def speak(self):
#         return print("Dog Bark")
    
# class Cat(Animal):
#     def speak(self):
#         return print("Cat Meow")

# animals = [Dog(),Cat()]

# for animal in animals:
#     animal.speak()
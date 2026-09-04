'''
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class).
'''



# class Animal():
#     def __init__(self,pet):
#         self.pet = pet
        
#     def speak(self):
#         print("pet is speak now!!")
        
# class childAnimal(Animal):
#     def speak(self):
#         print("woof")
#         return super().speak()
    
# pet1 = Animal("dog")
# # pet1.speak()

# child = childAnimal("cat")
# child.speak()


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def into(self):
#         print("Animal name : ",self.name)

# class Sound(Animal):
#     def Animal_Sound(self):
#         print(self.name, "bark")

# # parent = Animal("Dog")
# # parent.into()

# s1 = Sound("Cat")
# s1.into()
# s1.Animal_Sound()


#Super //the child class can leverage the functionality of the parent class.


class Animal_Super:
    def __init__(self,name):
        self.name = name
    
    def into(self):
        print("Animal Name : ", self.name)
    
class Sound(Animal_Super):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def All_details(self):
        print(f'Animal Name is {self.name} and breed is {self.breed}')

s1 = Sound("bruno","Chow Chow")
s1.All_details()

        
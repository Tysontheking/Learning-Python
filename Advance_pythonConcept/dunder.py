class Dunder:
    def __init__(self):
        self.name = "Satyam"
        self.age = 25
        
    def __str__(self):
        return f"Name: {self.name}\n Age: {self.age}"
    
    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        
        return self.age - other.age
    
    
    def __repr__(self):
        return 'object : {}'.format(self.name)
    


obj = Dunder()
print(repr(obj))  # Output: object : Satyam
# print(str(obj))  # Output: Name: Satyam, Age: 25
# print(obj + obj)
# print(obj - obj)
# print(dir(int))




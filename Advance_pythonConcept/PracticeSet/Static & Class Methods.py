class MathUtils():
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def description(cls):
        return "This is a utility class for math operations."
    
    
MathutilsObj = MathUtils()
print("Addition: ", MathutilsObj.add(5, 10))  # Accessing static method
print("Description: ", MathutilsObj.description())  # Accessing class method
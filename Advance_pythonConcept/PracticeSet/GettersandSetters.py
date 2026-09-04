class Employee():
    def __init__(self,salary):
        self._salary = salary  # Private attribute

        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            # raise ValueError("Salary cannot be negative.")
            print("Salary cannot be negative.")
        else:
            self._salary = value
    
e = Employee(50000)
e.salary = -7999
print(e.salary)  # Accessing the salary using the getter method



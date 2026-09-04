'''
The __new__() method creates and returns a new instance of the class.
The __init__() method initializes the newly created object.
The object becomes ready for use.
'''

class Employee:
    def __init__(self,salary,period,relation):
        self.salary = salary
        self.period = period
        self.relation = relation
    def get_info(self):
        print(f"Hey my name is satyam and my salary is {self.salary} and my working period is {self.period}, and my relationShip of company is {self.relation}....")
    
el = Employee(20000,'2 year','Good')
el.get_info()






# class school:
#     def __init__(self,teacher,behaviour,bond):
#         self.teacher = teacher
#         self.behaviour = behaviour
#         self.bond = bond
#     def get_schoolInfo(self):
#         print(f"So my school teacher is so {self.teacher} and my behaviour is also so {self.behaviour} and the bond is {self.bond}")
    
# sch = school("Good","Excellent",'2 years')
# sch.get_schoolInfo()
        
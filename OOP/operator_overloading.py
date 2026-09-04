# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def sum(self,p):
#         return point((self.x + p.x), self.y + p.y)
#     def print_point(self):
#         print( f'X value is {self.x} and Y value is {self.y}')
    
#     def __add__(self, p):
#         return point((self.x + p.x), self.y + p.y)
        

# p1 = point(3,4)
# p2 = point(5,5)

# # p = p1.sum(p2)
# p = p1 + p2
# p.print_point() 


# class add:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# a1 = add(2)
# a2 = add(4)
# print(a1 + a2)
# a = a1.__add__(a2)
# print(a)

#Overloading Comparison Operators

# class Greater:
#     def __init__(self,a):
#         self.a = a

#     def __gt__(self, other):
#         return self.a > other.a

# A1 = Greater(6)
# A2 = Greater(5)

# if A1 > A2:
#     print("a is greater than b")
# else:
#     print("b is greater than a")


#Example 2: This code shows how to overload both < and == operators for custom comparisons.
    
# class equ_less_opr:
#     def __init__(self,a):
#         self.a = a
#     def __lt__(self, other):
#         return "a is lest than b" if self.a < other.a else "b is smaller than a"
#     def __eq__(self, value):
#         return "a is equal to b" if self.a == value.a else "Not equal"

# obj1 = equ_less_opr(15)
# obj2 = equ_less_opr(15)

# print(obj1 < obj2)
# print(obj1 == obj2)


'''
Binary Operators -------------

Operator	Magic Method
+	        __add__(self, other)
-	        __sub__(self, other)
*	        __mul__(self, other)
/	        __truediv__(self, other)
//	        __floordiv__(self, other)
%	        __mod__(self, other)
**	        __pow__(self, other)

Comparison Operators -----------

Operator	Magic Method
<	        __lt__(self, other)
>	        __gt__(self, other)
<=	        __le__(self, other)
>=	        __ge__(self, other)
==	        __eq__(self, other)
!=	        __ne__(self, other


Assignment Operators --------------


Operator	Magic Method
-=	        __isub__(self, other)
+=	        __iadd__(self, other)
*=	        __imul__(self, other)
/=	        __itruediv__(self, other)
//=	        __ifloordiv__(self, other)
%=	        __imod__(self, other)
**=	        __ipow__(self, other)


Unary Operators ------------

Operator	Magic Method
-	        __neg__(self)
+	        __pos__(self)
~	        __invert__(self)
'''

    
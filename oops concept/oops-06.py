'''
Operator Overloading : Python allows us to change the meaning of operators for user-defined classes.
a = 5 
b = 6 
print(a+b)
print(int.__add__(a,b))
__add__ megic method
some example __abs__', '__add__', '__and__', '__bool__,__eq__', '__float__', '__floor__
'''

class point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
        return point(a,b)
    

p1 = point(1, 2)
p2 = point(3, 4)
s3 = p1 + p2
print(s3.a + s3.b)


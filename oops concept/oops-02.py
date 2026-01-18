'''
Types of Methods 
 instance methods
 class methods 
 static methods
'''



class MyClass:
    def __init__(self,value):
        self.value = value 

    def show(self):
        print("my Class is " , self.value)

value = MyClass(10)

value.show()

'''
Instance Method
The most common type.
Can access and modify object (instance) attributes.
First parameter is always self.
'''

class MyNewClass:
    value = 0

    @classmethod
    def increment_count(cls):
        cls.value += 1
        print(cls.value)

MyNewClass.increment_count()

'''
Class Method
Affects the class itself, not specific instances.
Declared using the @classmethod decorator.
First parameter is always cls (refers to the class).
'''


class Add:

    @staticmethod
    def add(a,b):
        print(a+b) 

Add.add(12,23)

'''
Static Method
Does not access instance (self) or class (cls) directly.
Declared using @staticmethod.
Like a regular function inside a class.
'''
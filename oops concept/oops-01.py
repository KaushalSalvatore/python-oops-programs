class Person:
    def __init__(self , name, age): # Constructor
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f'name :- {self.name} , age :- {self.age}')

person = Person('kaushal','28') # Constructor is called here

person.display_info()
# OR
Person.display_info(person)

'''
class Person: → defines a class named Person.
__init__ → the constructor that initializes name and age. and it call automatically when object call person.display_info().
self → refers to the current object.
person = Person("Alice", 30) → calling the constructor and creates an object person and automatically calls __init__.
'''
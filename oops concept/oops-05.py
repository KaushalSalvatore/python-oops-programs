'''
Polymorphism in Python allows objects of different classes to be treated as objects of a common superclass.
4 type of polymorphism
1. Duck Type
2. Operator Overloading 
3. Metthod Overloading 
4. Method Overriding 

duck type :- if there is an object which has a method execute that it we not concered about which class object it is 
 “If it looks like a duck and quacks like a duck, it’s a duck”
'''

class Dog:
    def speak(self):
        return 'woaf'
    
class Cat:
    def speak(self):
        return 'meow'
    
def animal(sound):
    print(sound.speak())

dog = Dog()
cat = Cat()

animal(dog)
animal(cat)
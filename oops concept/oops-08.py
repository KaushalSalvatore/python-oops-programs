'''Method Overriding'''

class Override:
    def Animal(self):
        print('Speak')

    
class Dog(Override):
    def Animal(self):
        print('Dog barks')

A = Override()
B = Dog()

A.Animal()
B.Animal()
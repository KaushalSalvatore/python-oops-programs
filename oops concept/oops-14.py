'''
Monkey Patching means modifying or extending code at runtime — especially for classes or modules you didn’t write yourself.
In Python, because everything is dynamic, you can replace methods and functions on the fly — that’s monkey patching!

Common Use Cases :
Fix bugs in third-party libraries without modifying source code
Add temporary behavior (e.g., for testing/mocking)
Modify methods in objects dynamically

When to Use :
Testing and mocking
Temporary fixes
Dynamically changing behavior
'''

class Dog():
    def speak(self):
        return 'woafff !!!'

dog = Dog()
print(dog.speak())

def cat(self):
    return 'Meow !!!'

Dog.speak = cat

print(dog.speak())
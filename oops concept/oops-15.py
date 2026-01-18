'''
@property is used to control access to an attribute of a class — often called getter/setter behavior.
It allows encapsulation: exposing data like a public attribute but giving control like a method.

To hide internal implementation
To add validation or logic on getting/setting a variable
To make code clean and readable
'''

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    # Property (getter)
    @property
    def salary(self):
        print("Getting salary...")
        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):
        print("Setting salary...")
        if value < 0:
            raise ValueError("Salary can't be negative!")
        self._salary = value

    # Deleter
    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        del self._salary


# 🔍 Usage
emp = Employee("Kaushal", 50000)

print(emp.salary)       # 👉 Calls getter
emp.salary = 60000      # 👉 Calls setter
print(emp.salary)

del emp.salary          # 👉 Calls deleter

# Accessing after delete will raise an AttributeError
# print(emp.salary)     # ❌ Uncomment to see error

'''
1. Public Members  : Accessible from anywhere 
No underscore prefix

2. Protected Members (_single_underscore) : Conventionally intended for internal use
Still accessible but should be treated as "protected"
Meant to be used inside the class and its subclasses

3. Private Members (__double_underscore) : Name-mangled to prevent accidental access,
Not directly accessible using object.__var
Internally renamed to _ClassName__var

'''

class employee:
    def __init__(self,name):
        self.name = name 

emp = employee('damon')
print(emp.name) # ✅ Allowed


class employee:
    def __init__(self,name):
        self._name = name 

emp = employee('damon')
print(emp._name) # ✅  # ⚠️ Allowed, but discouraged




class employee:
    def __init__(self,name):
        self.__name = name 

emp = employee('damon')
# print(emp.__name) # ❌ AttributeError
print(emp._employee__name)  # ✅ Access via name mangling
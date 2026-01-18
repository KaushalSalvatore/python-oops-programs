'''
In Python, everything is an object, and variables are references to those objects. So technically, Python uses 
"call by object reference" or "call by sharing".

Immutable types (int, str, tuple)	Acts like call by value — changes inside functions do not affect the original variable.
Mutable types (list, dict, set)	Acts like call by reference — changes inside functions do affect the original variable.

'''

# Immutable (Call by Value-like)

def modify_number(n):
    n += 10
    print(f"inside funcation value {n}")

x = 5
modify_number(x)
print(f"outside funcation value {x}")

# Mutable (Call by Reference-like)

def mofify_list(lst):
    lst.append(6)
    print(f"inside funcation value {lst}")

my_list = [1,2,3,4]
mofify_list(my_list)
print(f"outside funcation value {my_list}")

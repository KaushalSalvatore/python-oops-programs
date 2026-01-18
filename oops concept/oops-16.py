'''
The map() function is used to apply a function to every item in an iterable (like a list, tuple, etc.).
map(function, iterable)
function: A function to apply (can be a lambda, built-in, or user-defined)
iterable: List, tuple, set, etc.
Returns a map object (an iterator) — often converted to list() or tuple()
'''

def square(n):
    return n*n

lst = [2,3,4,5,6,7]
print(list(map(square,lst)))
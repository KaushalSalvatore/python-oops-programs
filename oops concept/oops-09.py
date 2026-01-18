'''
An iterator in Python is an object that is used to iterate over iterable objects like lists, 
tuples, dicts, and sets. The Python iterators object is initialized using the iter() method. 
It uses the next() method for iteration.
An iterator is an object with two methods:
__iter__() — returns the iterator object itself.
__next__() — returns the next value from the sequence. Raises StopIteration when done.
'''

num = [1,2,3,4,5,6,7,8,9]
it = iter(num)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(it.__next__())
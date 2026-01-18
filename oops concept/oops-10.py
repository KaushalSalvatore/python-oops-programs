'''
A generator function in Python is defined like a normal function, but whenever it needs to 
generate a value, it does so with the yield keyword rather than return. If the body of 
a def contains yield, the function automatically becomes a Python generator function.

A generator is a simpler way to create an iterator using yield instead of return.
It automatically creates __iter__() and __next__() for you.

'''

def tenNumber():
    n = 0
    while n <= 10:
        yield n*n
        n+=1
value = tenNumber()
for i in value:
    print(i)


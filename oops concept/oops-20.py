'''
Lambda Function (Anonymous Function)
A lambda is a short, one-line function without a name.
✅ Lambda → short, quick logic (often with map, filter, sorted)

List Comprehension

List comprehensions are a clean, Pythonic way to create lists.
✅ List comprehension → building lists (cleaner & more readable)

'''

add = lambda a,b : a+b
print(add(1,2))

arr = [1,2,3,4,5,6,7,8]
square = list(map(lambda x : x*x,arr))
print(square)

arr1 = [1,2,3,4,5,6,7,8]
even = list(filter(lambda x : x%2==0,arr1))
print(even)

# comprehension 

x = [1,2,3,4,5,6,7,8,9]
squ = [i*i for i in x]
print(squ)

ev = [x for x in squ if x%2==0]
print(ev)
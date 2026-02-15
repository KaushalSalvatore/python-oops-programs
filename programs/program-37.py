'''
Check list mutability
'''

a = [1,2,3,4,5]

print(id(a))

a.append(6)

print(id(a))
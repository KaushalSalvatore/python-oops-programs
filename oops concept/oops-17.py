'''
Shallow Copy	Creates a new object, but references the same nested/mutable items inside
Deep Copy	Creates a new object and recursively copies all nested objects

Shallow Copy = Photocopy of a folder: same documents inside.

Deep Copy = Manual duplication of both folder and every page inside.
'''

import copy
original = [[1,2],[3,4]]
shallow = copy.copy(original)
shallow[0][0] = 6
print(original)
print(shallow)


deep_original =  [[1,2],[3,4]]
deep_copy = copy.deepcopy(deep_original)

deep_original[0][0] = 6
print(deep_original)
print(deep_copy)
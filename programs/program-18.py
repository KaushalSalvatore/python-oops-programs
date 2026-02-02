'''
array negative element one side
'''

arr = [1,2,-6,3,-13,4,5,-4,-12,-9]

for i in arr:
    if i < 0:
        arr.remove(i)
        arr.append(i)

print(arr)
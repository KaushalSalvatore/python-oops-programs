'''
swap the array value according to given index
'''

arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

a = int(input())
b = int(input())

arr.remove(a)
arr.remove(b)

print(arr)
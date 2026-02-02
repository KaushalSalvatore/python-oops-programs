'''
array right rotation according to given index
'''
index1 = int(input())

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
arr = arr[-index1:] + arr[:-index1]

print(arr)
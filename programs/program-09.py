'''
find the maximum number from Array
'''
arr = [1,4,5,6,16,7,8,16,9,12,12]
arr1 = []
for i in range(0,len(arr)):
    for n in range(i+1,len(arr)):
        if  arr[i] > arr[n]:
            temp = arr[i]
            arr[i] = arr[n]
            arr[n] = temp

print(set(arr))

for  i in arr:
    if i not in arr1:
        arr1.append(i)

print(arr1)



# arr = [20, 10, 20,4, 21, 4, 100]

# max = arr[0]

# for i in arr:
#     if i > max :
#         max = i 

# print(max)



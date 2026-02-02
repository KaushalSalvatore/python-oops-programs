'''
Two Array union Intersection
'''

arr1 = [1,2,3,4]
arr2 = [3,4,5,6]

union_arr = list(set(arr1) | set(arr2))

print(union_arr)

union_arr_2 = []

for i in arr1 +arr2:
    if i not in union_arr_2:
        union_arr_2.append(i)
print(union_arr_2)
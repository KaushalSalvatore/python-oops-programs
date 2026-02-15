'''
Find uncommon elements

Input : arr1[] = {10, 20, 30}
        arr2[] = {20, 25, 30, 40, 50}
Output : 10 25 40 50'''

arr1 = {10, 20, 30}
arr2 = {20, 25, 30, 40, 50}
# ^ → symmetric difference
result = list(set(arr1) ^ set(arr2))
print(result)

# 2nd way

result1 = []
for a in arr1:
    if a not in arr2:
        result1.append(a)

for b in arr2:
    if b not in arr1:
        result1.append(b)
print(result1)
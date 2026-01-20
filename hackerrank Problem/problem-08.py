'''
List Comprehensions 

Given four integers x, y, z, and n, print a list of all coordinates
[i, j, k] such that:

0 ≤ i ≤ x

0 ≤ j ≤ y

0 ≤ k ≤ z

i + j + k ≠ n
'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
result = [[i, j, k] 
        for i in range(x + 1) 
        for j in range(y + 1) 
        for k in range(z + 1) 
        if i + j + k != n]

print(result)
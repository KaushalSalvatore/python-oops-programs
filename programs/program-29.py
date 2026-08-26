'''
sort the array in non-decreasing order and remove duplicates 

i/p : [1,1,1,3,3,3,2,2,2,4,4,4]
o/p : [1,2,3,4]
'''

input = [1,1,1,3,3,3,2,2,2,4,4,4]
output = []

input.sort()

for i in input:
    if i not in output:
        output.append(i)

print(output)

######################################

input = [1, 1, 1, 3, 3, 3, 2, 2, 2, 4, 4, 4]
output = sorted(set(input))
print(output)
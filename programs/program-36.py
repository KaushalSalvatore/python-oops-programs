'''Find longest consecutive sequence
num = [100,1,2,3,4,200,300]
o/p = 4
'''
num = [100,1,2,3,4,200,300]

num.sort()

longest = 1
count = 1
for i in range(1, len(num)):
    if num[i] == num[i-1] + 1:
        count += 1
    elif num[i] != num[i-1]:
        count = 1

    longest = max(longest, count)

print(longest)
print(count)

'''
Find all permutations of string
'''

s = "ABC"


for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                print(s[i] + s[j] + s[k])

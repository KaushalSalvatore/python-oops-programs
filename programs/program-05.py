'''
Count vowel in string
'''
str_1 = "Hello How Are You"

dict = {}

count = 0
vowel = ['a','e','i','o','u']

for chr in str_1.lower():
    if chr in vowel:
        dict[chr] = dict.get(chr, 0) + 1

print(dict)

'''
two strings are anagrams

Input:
str1 = "cat"
str2 = "tca"

Output:
true
'''
# Python Solution 1

from collections import Counter

def is_anagram(str1, str2):
    return Counter(str1) == Counter(str2)

print(is_anagram("cat", "tca"))      # True
print(is_anagram("hello", "olleh"))  # True
print(is_anagram("cat", "car"))      # False

# Python Solution 2 

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram("cat", "tca"))   # True
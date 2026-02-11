'''
Check if two Strings are Anagrams of each other
Anagrams: "rat" and "tar", "listen" and "silent", "anagram" and "nagaram".
'''

s1 = 'listen'
s2 = 'silent'

if sorted(s1) == sorted(s2):
    print('Anagrams')
else:
    print('Not Anagrams')


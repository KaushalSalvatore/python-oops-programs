'''
character occurrence in string
'''

str1 = "character occurrence in string"
dict = {}
for chr in str1:
     
    dict[chr] = dict.get(chr,0)+1

print(dict)
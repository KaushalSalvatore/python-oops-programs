'''
Remove the text from specific index position
'''
str1 = 'Damon salvatore'

index1 = int(input())
index2 = int(input())

str1 = str1.replace(str1[index1],'')
str1 = str1.replace(str1[index2],'')
print(str1)
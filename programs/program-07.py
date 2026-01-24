'''
Remove character form string given input 
'''
str1 = input()
str2 = 'Remove character from String'.lower()
for chr in str1.lower():
    if chr in str2.lower():
        str2 = str2.replace(chr,'')
    else:
        print("No String")

print(str2)
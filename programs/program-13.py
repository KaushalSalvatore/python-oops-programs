'''
Remove duplicate character from string
'''


str1 = "Damon Salvatore"
removeStr = str1
for re in str1:
    removeStr=removeStr.replace(re,"")  
    
print(removeStr)
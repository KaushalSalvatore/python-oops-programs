'''
Remove character form string given input array
'''

str1 = "Damon Salvatore"

removeStr = str1

ip = input()


for re in ip:
    removeStr=removeStr.replace(re,"")

print(removeStr)
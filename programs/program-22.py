'''
Remove characters at odd indices
'''

odd_remove = "kaushal Salvatore"

even_str = ''

# result = odd_remove[::2]

for i in range(len(odd_remove)):
    if i%2 == 0:
        even_str += odd_remove[i]
print(even_str)
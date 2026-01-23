'''
find common letter in two String
'''

str_1 = "hello Good afternoon"
str_2 = "hello Good night"
common = ''
for chr in str_1.replace(' ',''):
    print(f"first------------{chr} ")
    for c in str_2.replace(' ',''):
        print(f"secound------------{c} ")
        if c == chr:
            common += c
            
    
print(common)
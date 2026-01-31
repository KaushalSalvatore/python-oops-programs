'''
common letter in given two string
'''

str1 = input().strip()
str2 = input().strip()
c_chr = ""
for chr in str1:
    for chr1 in str2:
        if chr1 == chr:
            c_chr += chr1 +  " "

print(c_chr) 


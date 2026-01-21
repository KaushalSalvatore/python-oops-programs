'''
Print Armstrong Number
'''

num = 153

temp = num
temp2 = num
l = 0 
a = 0 

while temp > 0:
    temp//=10
    l +=1

while temp2 > 0:
    digit = temp2%10
    a += digit ** l
    temp2//=10
print(a)


'''
Factorial Number to given number
'''

n = int(input())
value = 1
for i in range(1,n+1):
    value = value*i
print(value)
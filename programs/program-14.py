'''
find the perfect number from list

The Smallest Perfect Number: The first perfect number is 6. 
Its divisors are 1, 2, and 3, and (1+2+3=6).The First Four: Known since antiquity, 
these are 6, 28, 496, and 8,128.
'''
arr = [6,28,234,123,12,496,8128]

dict = {}
for i in arr:
    sum = 0 
    for n in range(1,i):
        if i%n == 0:
            sum += n      
    if(i == sum):
        dict[i] = 'PN'
    else:
        dict[i] = 'NPN'
print(dict)
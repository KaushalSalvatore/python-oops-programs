'''
a = [1,2,3,4,5,6,7,8]
b = abcdefgh
output = 36a1b2c3d4e5f6g8h8
'''

a = [1,2,3,4,5,6,7,8]
b = 'abcdefgh' 

result = str(sum(a))

for ch, num in zip(b, a):
    result += ch + str(num)

print(result)
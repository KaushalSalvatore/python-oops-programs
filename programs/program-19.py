'''
Fibonacci Series using reursion and function
(0,1,1,2,3,5,8,13,21,34,55,.....)
'''
# a = 0
# b = 1 
# n = 0
# arr = [0,1]
# while n < 10:
#     c = a+b
#     arr.append(c)
#     a = b
#     b = c
#     n += 1
# print(arr)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i), end=" ")



    


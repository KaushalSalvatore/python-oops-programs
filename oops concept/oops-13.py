'''
 Types of Arguments
 Possition
 keyword
 Default
 variable lenght (*kwargs) (array value)
 **kwargs (dic)
'''

def possition(a,b):
    return a+b

print(possition(2,3)) 

def keyword(a,b):
    return a+b

print(keyword(b= 2,a = 3)) 

def default(a,b=3):
    return a+b

print(default(a=2)) 

def variable_len(*b):
    for i in b:
        return i

print(variable_len([1,3,4,6,7,8,2]))


def kwargs(**kwargs):
    for i ,j in kwargs.items():
        print(f'{i}:{j}')

kwargs(age=26,city='pune',mob=564838482)
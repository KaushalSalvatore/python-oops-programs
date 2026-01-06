'''
Python decorators : 
1. Functions that modify the behavior of other functions
2. Used with the @decorator_name syntax
3. Commonly used for logging, timing, access control
'''

def lowerStr(str):
    return str.lower()

def capitalStr(func):
    def capi(str):
        return str.upper()
    return capi


lower = capitalStr(lowerStr)

print(lower('lower stringConvert or upper'))

@capitalStr
def decoratorLowerStr(str):
    return str.lower()

print(decoratorLowerStr('Using decorator convert String'))
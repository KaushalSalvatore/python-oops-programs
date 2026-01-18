'''
Method Overloading (Simulated in Python)
Python does not support traditional method overloading. Instead, we can use default arguments or *args.
'''

class add:
    def overload(self,a=None,b=None,c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else: 
            s = a 

        return s
    
s1 = add()


print(s1.overload(2,4))
print(s1.overload(2,4,6))
print(s1.overload(2))
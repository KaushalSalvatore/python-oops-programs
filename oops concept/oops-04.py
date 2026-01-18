'''
MRO  -> Method resolution Order 

1. Python looks for methods in the current class, then parents, left to right (for multiple inheritance).
2. If a method is found, it’s called immediately — no duplicate calls.
3. Python follows C3 Linearization, which ensures consistent and predictable lookup order.
4. situation often called the diamond problem
'''

class A:
    def show(self):
        print('A')


class B:
    def show(self):
        print('B')


class C(A,B):
    def show(self):
        super().show() # this will solve diamond Problem 
        print('C')
c = C()
c.show()
print(C.__mro__)
#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


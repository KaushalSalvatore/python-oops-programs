'''
Single Inheritance – One child inherits from one parent. 

Multiple Inheritance – Child inherits from more than one parent.

Multilevel Inheritance – Child → Parent → Grandparent.

Hierarchical Inheritance – Multiple children inherit from one parent.

Hybrid Inheritance – Combination of more than one type.
'''

class Language:

    def India(self):
        print('Hindi')

class Area:
    def India(self):
        print('3.287 million km²')

class Language_1(Language): # Single Inheritance – One child inherits from one parent. 

    def America(self):
        print('english')

class Language_2(Language_1): # Multilevel Inheritance – Child → Parent → Grandparent.

    def Russian(self):
        print('Russian') 

class County(Language,Area): # Multiple Inheritance – Child inherits from more than one parent.

    def Country_details(self):
        print('India People')


class Union(Language_1,Language_2): #Hybrid Inheritance – Combination of more than one type.
    def Multi_Language(self):
        print('Hybrid Inheritance')


lang = Language_1()
lang.India()


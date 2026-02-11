'''
input : [apple , apple , banana , apple , orange , banana] 
output : [[apple , apple , apple],[banana, banana],[orange]]
'''
input  = ['apple' , 'apple' , 'banana' , 'apple' , 'orange' , 'banana'] 

result = {}

for item in input:
    result.setdefault(item , []).append(item)
    
print(list(result.values()))
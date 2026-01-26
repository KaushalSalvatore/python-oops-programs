'''
pair the target sun in given array
'''
sum = 6
arr = [0,1,2,3,4,5,6,7,8,9]
arr1=[]
for i in range(0,len(arr)):
    for n in range(i+1,len(arr)):
        if  arr[i] + arr[n] == 6:
            arr1.append(f'{arr[i]} + {arr[n]}')
print(arr1)
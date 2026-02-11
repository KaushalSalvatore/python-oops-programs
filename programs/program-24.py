'''
Check if given String is Pangram or not

Pangram :- a pangram check often involves converting the string to lowercase, removing non-alphabetic characters, 
and checking if the unique character count equals 26. 
'''

pangram = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"

flag = True

for i in alphabet:
    if i not in pangram.lower():
        flag = False
        break


if flag:
    print("Pangram")
else:
    print("Not Pangram")




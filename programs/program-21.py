'''
Count uppercase and lowercase letters
'''

ch_str = 'AbCdEfGHijklmn'

count_dict = {"uppercase": 0, "lowercase": 0}


for chr in ch_str:
    if chr.isupper():
        count_dict["uppercase"] += 1
    else:
        count_dict["lowercase"] += 1

print(count_dict)
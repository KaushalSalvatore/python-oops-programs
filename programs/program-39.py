'''
longest prefix string in this list [apple , app , appldws , appderr] using python ?
'''

strings = ['apple', 'app', 'appderr', 'appldws']

def longest_prefix(strings):
    strings.sort()

    first = strings[0]
    last = strings[-1]

    result = ""

    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            result += first[i]
        else:
            break

    return result


print(longest_prefix(strings))
 

'''
input: aabbccdeffff
output: d
'''

def non_repeating_value(value):
    freq = {}

    # Count frequency
    for ch in value:
        freq[ch] = freq.get(ch, 0) + 1

    # Find first non-repeating character
    for ch in value:
        if freq[ch] == 1:
            return ch

    return None


# Example
input_str = "aabbccdeffff"
print(non_repeating_value(input_str))


###############################################

def first_non_repeating_char(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

#############################################################
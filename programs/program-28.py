'''
input : my_dict = {
    'v1': 10,
    'v2': {
        'v3': 20,
        'v6': [30],
        'v7': {'v8': 40}
    },
    'v5': [25, 25]
}

output : 10 + 20 + 30 + 40 + 25 + 25 = 150
'''

input = my_dict = {
    'v1': 10,
    'v2': {
        'v3': 20,
        'v6': [30],
        'v7': {'v8': 40}
    },
    'v5': [25, 25]
}

def sum_values(data):
    if isinstance(data, dict):
        return sum(sum_values(v) for v in data.values())
    elif isinstance(data, list):
        return sum(sum_values(v) for v in data)
    elif isinstance(data, (int, float)):
        return data
    return 0

print(sum_values(my_dict))  # 150

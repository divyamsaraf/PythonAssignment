def string_to_list(s):
    return list(s)

input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']

result = list(map(string_to_list, input_list))

print(result)
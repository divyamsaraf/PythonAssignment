def count_frequency(input_list):
    frequency_dict = {}
    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

input_list = list(map(int, input("Enter the elements separated by space: ").split()))
frequency_count = count_frequency(input_list)
print("Frequency count:", frequency_count)

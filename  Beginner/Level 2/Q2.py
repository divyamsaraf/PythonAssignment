def get_unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

list1 = list(map(int, input("Enter the elements of the list: ").split()))

list2 = get_unique_elements(list1)

print("Unique elements:", list2)
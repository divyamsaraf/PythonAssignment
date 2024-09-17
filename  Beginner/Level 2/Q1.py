def find_common_elements_normal(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

l1 = list(map(int, input("Enter the elements of the first list: ").split()))
l2 = list(map(int, input("Enter the elements of the second list: ").split()))

common_elements_normal = find_common_elements_normal(l1, l2)
print("Common elements (Normal):", common_elements_normal)
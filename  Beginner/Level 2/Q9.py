def get_element_at_index(my_list, index):
    try:
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")
        print("IndexError handled")

my_list = [10, 20, 30, 40, 50, 60]

index = int(input("Enter an index: "))

get_element_at_index(my_list, index)

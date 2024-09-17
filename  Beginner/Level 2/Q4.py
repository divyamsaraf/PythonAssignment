def rotate_array(arr, D):
    n = len(arr)  
    D = D % n    
    rotated_array = arr[-D:] + arr[:-D]
    return rotated_array

arr = list(map(int, input("Enter the elements of the array: ").split()))
D = int(input("Enter the number of elements to rotate (D): "))

rotated_arr = rotate_array(arr, D)
print("Array after rotation:", rotated_arr)

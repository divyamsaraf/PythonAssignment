def count_pairs_with_sum(arr, k):
    freq_map = {}
    count = 0  

    for n in arr:
        diff = k - n
        
        if diff in freq_map:
            count += freq_map[diff]

        if n in freq_map:
            freq_map[n] += 1
        else:
            freq_map[n] = 1

    return count

arr = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the target sum (K): "))

pair_count = count_pairs_with_sum(arr, k)
print("Pair count:", pair_count)

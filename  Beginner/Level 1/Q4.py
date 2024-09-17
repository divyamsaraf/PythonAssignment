def sum_of_odd_numbers(start, stop):
    total_sum = 0
    for num in range(start, stop + 1):
        if num % 2 != 0: 
            total_sum += num
    return total_sum

start = int(input("Enter a number: "))
stop = int(input("Enter a number: "))
result = sum_of_odd_numbers(start, stop)
print(f"Sum of odd numbers between {start} and {stop}: {result}")
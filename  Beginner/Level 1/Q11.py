def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def reduce_to_single_digit(num):
    sum_digits = sum_of_digits(num)
    print(f"Sum_of_digits = {sum_digits}", end=", ")
    
    while sum_digits >= 10:
        sum_digits = sum_of_digits(sum_digits)
    
    return sum_digits

input_num = int(input("Enter a number: "))

final_output = reduce_to_single_digit(input_num)
print(f"Final Output: {final_output}")

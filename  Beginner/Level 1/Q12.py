def reverse_number(num):
    revnum = 0
    while num > 0:
        last_digit = num % 10
        revnum = revnum * 10 + last_digit
        num //= 10
    return revnum

input_num = int(input("Enter a number: "))

reversed_num = reverse_number(input_num)
print(f"revnum = {reversed_num}")

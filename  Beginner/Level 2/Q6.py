def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return is_power_of_two(n // 2)
    return False

num = int(input("Enter a number to check if it's a power of two: "))

result = is_power_of_two(num)

if result:
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")

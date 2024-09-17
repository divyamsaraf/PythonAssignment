import math

def calculate_lcm(number1, number2):
    return abs(number1 * number2) // math.gcd(number1, number2)

number1 = int(input("Enter Number 2: "))
number2 = int(input("Enter Number 2: "))
print(f"LCM of {number1} and {number2} is: {calculate_lcm(number1, number2)}")

def perfect_number(num):
    sum_of_divisors = 0
    
    for i in range(1, num):
        if num % i == 0:  
            sum_of_divisors += i

    if sum_of_divisors == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
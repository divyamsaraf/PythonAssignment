def check_number(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Consultadd - Python Training")
    elif num % 3 == 0:
        print("Consultadd")
    elif num % 5 == 0:
        print("Python Training")
    else:
        print("The number is not divisible by 3 or 5")

number = int(input("Enter a number: "))
check_number(number)
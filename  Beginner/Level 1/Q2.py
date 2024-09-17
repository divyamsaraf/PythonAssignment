def count_letters_and_digits(input_str):
    letters = 0
    digits = 0
    
    for char in input_str:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    
    print(f"Alphabets: {letters} & Number: {digits}")

input_str = input("Enter a string: ")
count_letters_and_digits(input_str)
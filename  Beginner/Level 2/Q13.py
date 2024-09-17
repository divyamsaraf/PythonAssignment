starts_with_char = lambda input_string, given_char: input_string.startswith(given_char)

input_string = input("Enter the string: ")
given_char = input("Enter the character: ")

result = starts_with_char(input_string, given_char)
print(f"Does the string start with the given character '{given_char}'? {result}")
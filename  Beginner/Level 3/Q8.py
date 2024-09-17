def encoded_string(string):
    parts = string.split('0')
    
    split_parts = [part for part in parts if part]
    
    if len(split_parts) != 3:
        raise ValueError("Encoded string does not have exactly three parts.")
    
    result = {
        "first_name": split_parts[0],
        "last_name": split_parts[1],
        "id": split_parts[2]
    }
    
    return result

string = input("Enter the encoded string: ")
parsed_data = encoded_string(string)
print(parsed_data)
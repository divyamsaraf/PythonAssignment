def read_even_length_strings(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        even_length_words = []

        for line in lines:
            words = line.split()
            
            for word in words:
                if len(word) % 2 == 0:
                    even_length_words.append(word)
        
        return ' '.join(even_length_words)

    except FileNotFoundError:
        return "File not found!"

filename = './ Beginner/Level 3/doc.txt'
result = read_even_length_strings(filename)
print(result)
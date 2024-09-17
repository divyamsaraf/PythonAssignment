def JtoI(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        corrected_content = content.replace('J', 'I')
        
        print(corrected_content)
    
    except FileNotFoundError:
        print("File not found!")

filename = './ Beginner/Level 3/words.txt'

JtoI(filename)

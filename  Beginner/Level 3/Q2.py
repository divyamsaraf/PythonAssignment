def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found!"

filename = './ Beginner/Level 3/demo.txt'

line_count = count_lines_in_file(filename)
print(f"Number of lines in demo.txt: {line_count}")

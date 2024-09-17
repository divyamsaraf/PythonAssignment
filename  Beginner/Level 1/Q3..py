def calculate_grade():

    physics = float(input("Enter marks for Physics: "))
    chemistry = float(input("Enter marks for Chemistry: "))
    biology = float(input("Enter marks for Biology: "))
    mathematics = float(input("Enter marks for Mathematics: "))
    computer = float(input("Enter marks for Computer: "))

    total_marks = physics + chemistry + biology + mathematics + computer
    percentage = total_marks / 5

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'

    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

calculate_grade()

def construct_dict_with_loops(students, subjects):
    if len(students) != len(subjects):
        raise ValueError("The length of students and subjects lists must be same.")

    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]

    return student_subject_dict

def get_user_input():
    n = int(input("Enter the number of students: "))

    students = []
    for i in range(n):
        student_name = input(f"Enter the name of the student '{i+1}': ")
        students.append(student_name)
    
    subjects = []
    for i in range(n):
        subject_name = input(f"Enter the subject of the student {i+1}: ")
        subjects.append(subject_name)

    return students, subjects

students, subjects = get_user_input()

result_dict = construct_dict_with_loops(students, subjects)
print(result_dict)
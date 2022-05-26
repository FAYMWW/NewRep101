student_dict ={
    'student_A' : 85,
    'student_B' : 79,
    'student_C' : 69,
    'student_D' : 59,
    'student_E' : 49,
}

def fn_grade(grade):
    if student_dict[i] >= 80:
        grade = 'A'
    elif student_dict[i] >= 70:
        grade = 'B'
    elif student_dict[i] >= 60:
        grade = 'C'
    elif student_dict[i] >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print(i + ": Score = " + str(student_dict[i])+ ", Grade = " + grade)

for i in student_dict:
    fn_grade(student_dict)
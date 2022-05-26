def grade_list(list_of_score):
    grade = []
    for score in list_of_score:
        if score >= 80:
            grade.append('A')
        elif score >= 70:
            grade.append('B')
        elif score >= 60:
            grade.append('C')
        elif score >= 50:
            grade.append('D')
        else:
            grade.append('F')
    return grade
print(grade_list([50,60,70,80,59,69,79,99,-1]))
print("Completed!")

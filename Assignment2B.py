list_of_score = [0,-1,99,79,69,59,80,70,60,50]
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
print("Your grade is "+ grade)
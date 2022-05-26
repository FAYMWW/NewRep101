#Grading 10 Students using function and loop
x=0
print("Enter score 10 times:")
while x < 10:
    def grade_result(score):
        if score >= 80:
            grade = 'A'
        elif score >= 70:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        elif score >= 50:
            grade = 'D'
        else:
            grade = 'F'
        return grade
    print("Your grade is "+ grade_result(int(input("Enter your score: "))))
    x = x + 1

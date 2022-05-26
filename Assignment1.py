#Grading 1 Student at a time using if else.
score = int(input("Enter your score: "))
grade = ""
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
print("Your grade is: " + grade)
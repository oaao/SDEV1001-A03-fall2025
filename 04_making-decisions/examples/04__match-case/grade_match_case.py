"""
if we were doing this in if-elif-else syntax:

if letter_grade = "A":
    ...
elif letter_grade = "B":
    ...
...
else:
    print("could not determine numeric grade")


^ ew no thank u
"""

letter_grade = input("Enter your letter grade (e.g. A, B, C...): ")
letter_grade = letter_grade.upper()

match letter_grade:
    case "A" | "A+":
        gpa = 4.0
    case "B":
        gpa = 3.3
    case "C":
        gpa = 2.5
    case "D":
        gpa = 2.0
    case "F":
        gpa = 1.0
    case _:
        print("couldn't determine grade from letter")
        gpa = 0.0

print(f"Your GPA is {gpa}")

"""
if-elif-else syntax becomes visually noisy and hard to read with many cases or multiple conditions:

    if letter_grade = "A":
        ...
    elif letter_grade = "B":
        ...
    elif letter_grade = "C":
        ...
    ...
    else:
        print("could not determine numeric grade")


^ ew no thank u.
let's learn how to use match-case instead!
"""


letter_grade = input("Enter your letter grade (e.g. A, B, C...): ")


# let's cast the input to uppercase, in case the user submits a lowercase letter.
# string values are case-sensitive, e.g. "abc" != "Abc"
letter_grade = letter_grade.upper()


match letter_grade:
    case "A" | "A+":  # we can match multiple cases in the same line with x | y | z ...
        gpa = 4.0
    # case "A+":     <- otherwise, we'd need a separate block for "A+" -- which would be pointless repetition,
    #   gpa = 4.0       because both cases execute identical code.  DRY - Don't Repeat Yourself!
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

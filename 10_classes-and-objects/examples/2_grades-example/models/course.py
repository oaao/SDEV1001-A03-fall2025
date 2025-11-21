class Course:
    def __init__(self, name):
        self.name = name
        self.students = []     # will be a list of Student instances
        self.assignments = []  # will be a list of Assignment instances

    def __str__(self):
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    # writing to attributes
    def add_student(self, student):
        self.students.append(student)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)


    # reading data from attributes
    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_assignment(self, assignment_id):
        for assignment in self.assignments:
            if assignment.id == assignment_id:
                return assignment
        return None

    # processing data
    def get_course_average(self):
        total = 0
        num_submissions = 0

        for student in self.students:
            for submission in student.submissions:
                total += submission.grade
                num_submissions += 1

        return total / num_submissions

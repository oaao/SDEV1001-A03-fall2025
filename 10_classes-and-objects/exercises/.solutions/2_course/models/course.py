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

    def get_assignment_average(self, assignment_id):
        """
        Instead of for loops as seen in the other method,
        you could instead use a list/tuple comprehension to filter data,
        and use the length of that iterable for the count of elements!

        assignment_grades = []
        for student in self.students:
            for submission in student.submissions:
                if submission.assignment.id == assignment_id:
                    assignment_grades.append(submission.grade)

        ^ translated into a comprehension expression, this would look like:
        """
        assignment_submissions = [  # this list expression could all be one line too!
            submission.grade
            for student in self.students for submission in student.submissions
            if submission.assignment.id == assignment_id
        ]
        return sum(assignment_submissions) / len(assignment_submissions)

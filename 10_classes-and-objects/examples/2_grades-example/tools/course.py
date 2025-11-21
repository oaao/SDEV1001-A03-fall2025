class Course:
    def __init__(self, name):
        self.name = name
        self.students = []     # will be a list of Student instances
        self.assignments = []  # will be a list of Assignment instances

    def __str__(self):
        return f"{self.name} has {len(self.students)} students and {len(self.assignments)} assignments"

    def add_student(self, student):
        self.students.append(student)

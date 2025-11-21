class Submission:
    def __init__(self, student, assignment, grade):
        self.student = student        # Student instance
        self.assignment = assignment  # Assignment instance
        self.grade = grade            # int

    def __str__(self):
        return f"{self.student.name} received {self.grade} on {self.assignment}"

class Student:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        self.submissions = []  # will be a list of Submission instances

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)
        
    def add_submission(self, submission):
            self.submissions.append(submission)

    def get_average(self):
        # assuming all assignments are weighted equally...
        grades = []
        for submission in self.submissions:
            grades.append(submission.grade)

        return sum(grades) / len(grades)
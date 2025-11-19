class Student:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name
        self.submissions = []  # will be a list of Submission instances

    def __str__(self):
        return f"{self.name}"

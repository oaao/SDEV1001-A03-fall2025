from data.course_data import assignment_data, student_data, submission_data

from models.course import Course
from models.student import Student
from models.assignment import Assignment


def add_students_from_data(course, student_data):
	for data in student_data:
		student_instance = Student(
			data["id"],
			data["name"]    # <-- both of these are positional arguments in Student.__init__()
		)
		course.add_student(student_instance)


def add_assignments_from_data(course, assignment_data):
    for assignment in assignment_data:
        assignment_instance = Assignment(
        	assignment["id"],
        	assignment["name"]
        )
        course.add_assignment(assignment_instance)


if __name__ == "__main__":

	 course = Course("Colourful Entomology 304")
	 print("before adding anything:", course)

	 add_students_from_data(course, student_data)
	 print("after adding students:", course)

	 add_assignments_from_data(course, assignment_data)
	 print("after adding assignments:", course)


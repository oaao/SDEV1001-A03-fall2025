from data.course_data import assignment_data, student_data, submission_data

from tools.course import Course
from tools.student import Student


def add_students_from_data(course, student_data):
	for data in student_data:
		student_instance = Student(
			data["id"],
			data["name"]    # <-- both of these are positional arguments in Student.__init__()
		)
		course.add_student(student_instance)


if __name__ == "__main__":

	 course = Course("Colourful Entomology 304")
	 print(course)

	 add_students_from_data(course, student_data)
	 print(course.students)
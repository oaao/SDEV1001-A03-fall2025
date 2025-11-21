from data.course_data import assignment_data, student_data, submission_data

from models.assignment import Assignment
from models.course import Course
from models.student import Student
from models.submission import Submission


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

def add_submissions_from_data(course, assignment_data):
	# a 'through-model' that connects Student and Assignment instances
    for submission in submission_data:
        student = course.get_student(submission["student_id"])
        assignment = course.get_assignment(submission["assignment_id"])
        submission = Submission(student, assignment, submission["grade"])
        student.add_submission(submission)


if __name__ == "__main__":

	 course = Course("Colourful Entomology 304")
	 print("before adding anything:", course)

	 add_students_from_data(course, student_data)
	 print("after adding students:", course)

	 add_assignments_from_data(course, assignment_data)
	 print("after adding assignments:", course)

	 add_submissions_from_data(course, submission_data)
	 print("after adding submissions:", course)

	 # now that I've populated instances w/ all necessary data, I can...
	 course_avg = course.get_course_average()
	 print(f"The average for {course.name} is {course_avg}")

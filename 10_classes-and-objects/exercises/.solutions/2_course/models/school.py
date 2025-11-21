class School:
	
	def __init__(self, name):
		self.name = name
		self.courses = []

	def add_course(self, course):
		self.courses.append(course)

	def list_courses(self):
		print(f"\nListing courses for {self.name}:")
		for course in self.courses:
			print(f"  - {course.name}")

#  What relationship is appropriate for Course and Faculty

class Faculty:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise
        
    def display(self):
        print(f" name is : {self.name} and expertise is {self.expertise}")

class Course:
    def __init__(self, course_name, faculty):
        self.course_name = course_name
        self.faculty = faculty
        
    def display(self):
            print(f" course name is : {self.course_name} and faculty is {self.faculty}")


python_expert = Faculty("Dr. Smith", "Python Programming")
python_course = Course("Introduction to Python Programming", "python_expert")


python_expert.display()
python_course.display()

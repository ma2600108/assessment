class Student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id
        self.grade=grade

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.id)
        print("Grades:", self.grade)

class UngraduateStudent(Student):
    def __init__(self, name, id, grade, major):
        super().__init__(name, id, grade)
        self.major=major
    
    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.id)
        print("Grades:", self.grade)
        print("Major:", self.major)

class GraduateStudent(Student):
    def __init__(self, name, id, grade, program_title):
        super().__init__(name, id, grade)
        self.program_title=program_title
        
    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.id)
        print("Grades:", self.grade)
        print("Program Title:", self.program_title)

m=Student("Mustafa",16060410,95)
m.display_info()

n=UngraduateStudent("Ahmed",28424891,90,"Mechatronics")
n.display_info()

o=GraduateStudent("Mustafa Hazem",2600108,100,"EEE")
o.display_info()
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.__grade = grade
    
    def get_grades(self):
        return f'{self.__grade}'
    
    def add_grades(self, grade):
       if 100>=grade>=0:  
         self.__grade.append(grade)
       else:
         return "Grade invalid"
    
    def calculate_average(self):
       if len(self.__grade)==0:  
         return 0
       else:
         avg=sum(self.__grade)/len(self.__grade)
         return avg

    def calculate_grade(self):
       avg=self.calculate_average()
       if avg==0:  
         return "N/A"
       else:
         if avg>=90:
           return "A"
         elif avg>=80:
           return "B"
         elif avg>=70:
           return "C"
         elif avg>=60:
           return "D"
         else:
           return "F"

    def display_info(self):
         print("Name: ",self.name)
         print("Student ID: ",self.student_id)
         print("Grade: ",self.__grade)
         print("Average grade: ",self.calculate_average())
         print(f"Calculated grade: {self.calculate_grade()}")

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

m=Student("Mustafa",16060410,[95,85])
m.get_grades()
m.add_grades(85)
m.display_info()

#n=UngraduateStudent("Ahmed",28424891,90,"Mechatronics")
#n.display_info()

#o=GraduateStudent("Mustafa Hazem",2600108,100,"EEE")
#o.display_info()
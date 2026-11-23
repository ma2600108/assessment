class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grade = []

    def get_grades(self):
        return self.__grade
    
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
         print("\nName: ",self.name)
         print("Student ID: ",self.student_id)
         print("Grade: ",self.__grade)
         print("Average grade: ",round(self.calculate_average(), 2))
         print(f"Calculated grade: {self.calculate_grade()}")

    def grades_sort(student_list):
      n=len(student_list)
      for i in range(n-1):
          for j in range(n-i-1):
             if student_list[j].calculate_average()>student_list[j+1].calculate_average():
                student_list[j],student_list[j+1]=student_list[j+1],student_list[j]
      return student_list

      #file=open("students.txt","w")
      # for s in student_list:
      #   file.write(f"{s.name} | {s.student_id} | {s.get_grades()} | {s.calculate_average()} | {s.calculate_grade()}\n") 
      # file.close()

class UngraduateStudent(Student):
    def __init__(self, name, student_id, major):
        super().__init__(name, student_id)
        self.major=major
    
    def display_info(self):
        super().display_info()
        print("Major:", self.major)

class GraduateStudent(Student):
    def __init__(self, name, student_id, program_title):
        super().__init__(name, student_id)
        self.program_title=program_title
        
    def display_info(self):
        super().display_info()
        print("Program Title:", self.program_title)

def save_students(students, filename):
    file = open(filename, "w")                       # open for writing
    for s in students:
        if isinstance(s, GraduateStudent):
            kind, extra = "Graduate", s.program_title
        elif isinstance(s, UngraduateStudent):
            kind, extra = "Undergraduate", s.major
        else:
            kind, extra = "Student", ""
        grades = ";".join(str(g) for g in s.get_grades())
        file.write(kind + "," + s.name + "," + str(s.student_id) + "," + extra + "," + grades + "\n")
    file.close()                                      # always close the file
    print("Saved", len(students), "students to", filename)

def read_students(filename):
    students = []
    try:
        file = open(filename, "r")                    # open for reading
        for line in file:
            line = line.strip()
            if line == "":
                continue
            kind, name, student_id, extra, grades = line.split(",")
            if kind == "Graduate":
                s = GraduateStudent(name, student_id, extra)
            elif kind == "Undergraduate":
                s = UngraduateStudent(name, student_id, extra)
            else:
                s = Student(name, student_id)
            if grades != "":
                for g in grades.split(";"):
                    s.add_grades(float(g))
            students.append(s)
        file.close()                                  # always close the file
    except FileNotFoundError:
        print("Error: the file", filename, "does not exist")
    return students

#m=Student("Mustafa",16060410)
#m.add_grades(95)
#m.add_grades(87)
#m.add_grades(85)
#m.display_info()

n=UngraduateStudent("Ahmed",28424891,"Mechatronics")
n.add_grades(90)
n.add_grades(99)
n.add_grades(92)
#n.display_info()

o=GraduateStudent("Mustafa Hazem",2600108,"EEE")
o.add_grades(100)
o.add_grades(100)
o.add_grades(100)
#o.display_info()

save_students([n, o], "students.txt")

loaded = read_students("students.txt")
for s in loaded:
    s.display_info()
    print()

read_students("missing_file.txt") 
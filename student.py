class Student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id
        self.grade=grade

m=Student("Mustafa",16060410,95)
print(m.name,m.id,m.grade)
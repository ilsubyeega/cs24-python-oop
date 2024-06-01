class Student():
    def __init__(self, name):
        self.name = name
        print('Creating Student object', self.name)

    def __del__(self):
        print('In the __del__ method for student:', self.name)

class Teacher():
    def __init__(self):
       print('Creating the Teacher object')
       self.oStudent1 = Student('Joe')
       self.oStudent2 = Student('Sue')
       self.oStudent3 = Student('Chris')

    def __del__(self):
        print('In the __del__ method for Teacher')

oTeacher = Teacher()

del oTeacher
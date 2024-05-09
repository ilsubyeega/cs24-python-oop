from student import Student

oStudent1 = Student('Joe Schmoe')
oStudent2 = Student('Jane Smith')

print(oStudent1.grade)
print(oStudent2.grade)
print()

oStudent1.grade = 85
oStudent2.grade = 92

# oStudent1.grade = 'abc'

print(oStudent1.grade)
print(oStudent2.grade)

# forcing to write double underscore(didnt know before, wow)
print(vars(oStudent1))
oStudent1._Student__grade = 100
print(oStudent1.grade)

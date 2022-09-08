class Student:
    #static field
    major = "CSE"

    #constractor
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name

s1 = Student(1, "John")
s2 = Student(2, "Bill")

print(s1.major)
print(s2.major)
print(s1.rollNo)
print(s2.name)
print(Student.major)
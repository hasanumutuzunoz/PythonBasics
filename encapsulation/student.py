class Student:
    """"
    def __init__(self):
        self.__id = 123 #private variable
        self.__name = "John"

    def display(self):
        print(self.__id)
        print(self.__name)"""

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

s = Student()
"""
#print(s.__id)
#print(s.__name) #this cannot work because it is private variable
s.display()

print(s._Student__id) # (Name Mangling) You can access private variables without a inner function like this
print(s._Student__name)"""

s.setId(123)
s.setName("John")
print(s.getId())
print(s.getName())
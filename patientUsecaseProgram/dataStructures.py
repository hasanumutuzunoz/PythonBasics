#Map of lists
#This is basicly dictinary with lists
students = {"John":["Python", "DJango", "DRF"], "Bob":["Java", "Spring"], "Jim":["JS", "Node", "React"]}
keys = students.keys()

print(students["Bob"]) #Print Bob's courses

#Print each students courses
for eachKey in keys:
     print("Courses taken by", eachKey, "are: ")
     for eachCourse in students[eachKey]:
         print(eachCourse)

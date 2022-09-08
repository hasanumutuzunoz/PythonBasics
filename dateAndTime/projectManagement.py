from datetime import *

class Project:
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def addResource(self, resource):
        self.resources.append(resource)

class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

project = Project("AI", date(2022,1,9), date(2022,5,15))
task = Task("Creating a lifetime financial and health habits for a very long and happy life", 90)
resource = Resource("Hasan", "Python")
task.addResource(resource)
project.addTask(task)

for eachTask in project.tasks:
    print(eachTask.name)
    for eachResource in eachTask.resources:
        print(eachResource.name)
        print(eachResource.skill)
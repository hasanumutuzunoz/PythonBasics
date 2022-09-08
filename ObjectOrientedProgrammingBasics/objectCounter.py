class ObjectCounter:

    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects += 1

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)

o1 = ObjectCounter()
o2 = ObjectCounter()
o3 = ObjectCounter()
o4 = ObjectCounter()
o5 = ObjectCounter()
o6 = ObjectCounter()
o7 = ObjectCounter()

ObjectCounter.displayCount()
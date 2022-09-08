# An interface in Python is simple an abstract class with all the methods are abstract method
# So I am not writing an interface code again here
# ABC must be inherited to create abstract class
# abstractmethod must be inherited to create abstract method

from abc import abstractmethod, ABC

# Abstract class
class BMW(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine stopped")

    # Abstract Method
    #All abstract methods must be implemented in the sub classes
    @abstractmethod
    def drive(self):
        pass

# Inheritance from parent class BMW
class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        #BMW.__init__(self, make, model, year)
        super().__init__(make, model, year) # super() invokes the parent class
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self): # ONLY available in three series, not in parent class, not in five series
        print(self.cruiseControlEnabled)

    # Override function
    def start(self):
        super().start()
        print("Button Start")

    def drive(self):
        print("Three series is being driven")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
        print("Three series is being driven")

threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
fiveSeries = FiveSeries(True, "BMW", "506i", "2020")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
fiveSeries.stop()


#b = BMW("BMW", "328i", "2018") # We cannot instantiate absract classes
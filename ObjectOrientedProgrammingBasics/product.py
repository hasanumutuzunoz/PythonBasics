class Product:

    def __init__(self):
        self.name = "iPhone"
        self.description = "Apple smartphone"
        self.price = 700

    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1 = Product()
"""print(p1.name)
print(p1.description)
print(p1.price)"""
p1.display()
p1 = None #make sure the object memory is deleted
          # it is already deleting automaticly

p2 = Product()
p2.display()


x = 123 #global variable

def display():
    x = 678 #local variable, only accesable within display() function
    print(x)
    print(globals()["x"]) #print global variables

#print(x)
#display()

#Assign function to variable
z = display
z()
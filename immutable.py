"""Python uses same memory if the variables has same value
    If we change one variable value, Python will create a new memory space. """
a=20
b=20
print(id(a)) #print the memory location
print(id(b))
print(a is b) #if a and b memory location is same

a=True
b=False
print(id(a)) #print the memory location
print(id(b))
print(a is b) #if a and b memory location is same

a="Hasan"
b="Hasan"
print(id(a)) #print the memory location
print(id(b))
print(a is b) #if a and b memory location is same
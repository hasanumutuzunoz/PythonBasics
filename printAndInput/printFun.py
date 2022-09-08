print()
print("Hello" * 3)
print("All the power is \n within you")

a,b=10,20
print(a, b, sep="++iiuhiuhiuh++")  #seperator

name = "john"
marks = 94.5827364
print("Name is", name, "marks are", marks)

#%s string data - %i integer - %f float data
print("name is %s,Marks are %.2f" %(name,marks)) # %.2f prints 2 numbers after dot

print("name is {}, Marks are {}".format(name, marks))
print("name is {1}, Marks are {0}".format(name, marks)) #with index
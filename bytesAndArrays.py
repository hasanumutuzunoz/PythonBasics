lst = [20,30,40,234]
print(type(lst))

b=bytes(lst) #convert list to byte
print(type(b)) #bytes cannot be changed or added
print(b)

b1 = bytearray(lst) #convert list to byte array
print(type(b1))
b1[2] = 33
print(b1) #we can add on byteArray


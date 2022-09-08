#Same variables uses same memory
a = 20
b = 20
c = 30
print(id(a), id(b), id(c))

f = 3.14

#complex variables has real any imaginary parts
c = 5+3j
print(c.real)
print(c.imag)

#string
s = "Hasan"
print(type(s))

#list
lst = [1,2,3,4,5]
#tuple
t = (1,2,3,4,5)
print(type(t))
#set (cannot repeat)
s = {1,2, 3,4,5,5,5,6}
print(type(s))
print(s)
#frozen set (immutable - cannot changed)
fs = frozenset(s)
print(type(fs))
#dictionary
d = {1:100, 2:90, 3:60}
print(type(d))
#bytes
b = bytes(lst)
print(type(b))
print(b)

#Bytearray is immutable
ba = bytearray(lst)
print(type(ba))

#range is immutable
r1 = range(20)
r2 = range(20)
range(1,10)
range(1,30,3)




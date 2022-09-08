#Set does not allow duplicates, slicing, indexing, repetition
#Set variables are random order
s={10,20,30,"XYZ",10,20,10}

s.update([88,99])
s.remove(30)
print(s)
print(type(s))

f=frozenset(s) #frozen set cannot be changed
print(f)

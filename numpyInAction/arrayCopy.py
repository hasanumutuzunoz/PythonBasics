from numpy import *

a1 = arange(1,10)
a2 = a1.view() # Shallow Copy - When we change any element from a2, a1 also  changes
a3 = a1.copy() # Normal Copy - a1 won't be changed when we change the copy

print('a1', a1)
print('a2', a2)

a2[3] = 40
print('a1', a1)
print('a2', a2)

a3[3] = 50
print('a1', a1)
print('a3', a3)
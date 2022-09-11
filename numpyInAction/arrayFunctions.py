from numpy import *

a1 = arange(12) # 0 to 11
print('a1', a1)

a2 = reshape(a1,(2,6)) # a2 is re-shape of a1 2 dimensional
print('a2', a2)

a3 = reshape(a1,(2,2,3))
print('a3', a3)

print(a3.flatten()) # convert multidimensional to singe dimensional

print(eye(3)) # create 3 by 3 matrix

print(ones((2,3))) # create 2 to 3 matrix with ones
print(zeros((2,3)))
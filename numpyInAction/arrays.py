#import numpy as np
#arr = np.array([1,2,3,4,5])

from numpy import *

arr = array([1,2,3,4,5],int) # only int value (optional)
carr = array(['a','b','c'])
sarr = array(['Python', 'Django', 'Django Rest'])
print(arr)
print(carr)
print(sarr)

print(linspace(0,100,50)); #print 50 values between 0 to 100
larr = logspace(1,20)
for i in larr:
    print(larr)
print(arange(1,58,3)) # print 1 to 58 incrementing 3
print(arange(58,1,-3)) # reverse
print(zeros(200))
print(ones(100))
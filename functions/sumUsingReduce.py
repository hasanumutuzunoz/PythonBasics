#To use the reduce func, we need to import reduce from functools
from functools import reduce

lst = [5, 10, 15, 20]

#Sum of elements with using reduce function
result = reduce(lambda x,y: x+y, lst)
print(result)
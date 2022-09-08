""" tuples cannot be changed like lists (immutable)
single element tuple must end with comma ,
singleTPL = (1,)
"""

tpl = (20,30,40,20,50,"xyz")
singleTpl = (1,)
print(tpl)
print(singleTpl*8)
print(type(singleTpl))
print(tpl.count(20))
print(tpl.index(50))

lst=[14,67,49,"xyz"]
print(type(lst))
tpl1=tuple(lst) #convert list to tupple
print(tpl1)
print(type(tpl1))
lst1=list(tpl1)  #convert tuple to list
print(lst1)
print(type(lst1))
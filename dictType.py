dict1={1:"john", 2:"bob", 3:"bill"} #id no: value, ....
print(dict1)
print(type(dict1))
print(dict1.items()) #print dict items

k=dict1.keys()       #print dict keys
for i in k:
    print(i)

v=dict1.values()     #print dict values
for i in v:
    print(i)

print(dict1[3])      #print dict specific value

del dict1[1]
print(dict1)


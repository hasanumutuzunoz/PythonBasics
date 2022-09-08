#with eval we can add list items easily
l1 = eval(input("Enter a list of elements"))
print(l1)

#erase the duplicates - hard way
l2=[]
for eachValue in l1:
    if eachValue not in l2:
        l2.append(eachValue)
print(l2)

#easy way with set
s1 = set(l1)
print(s1)
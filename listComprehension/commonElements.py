a = [2,4,6,8,4,4,7,4,4,4]
b = [7,2,3,4,7,8,8,8]

#result = [i for i in range(len(a)) if a[i] == b[i]]
#print(result)

# (My Way) Print common elements from 2 lists.
# Result is set type so no duplicates
result = []
for i in range(len(a)):
    for z in range(len(b)):
        if a[i] == b[z]:
            result.append(a[i])
setResult = set(result)
print(setResult)

# Same logic shorter
result = []
for i in a:
        if i in b:
            result.append(i)
setResult = set(result)
print(setResult)


# BEST VERSION
result = [i for i in a if i in b]
print(result)

s = "All the power is within you"
print(s)

#Split the words
temp = s.split()
print(temp)

#reverse the split words
result = []
i = len(temp)-1
while i>=0:
    result.append(temp[i])
    i = i-1

print(result)

output = " ".join(result)
print(output)
print(type(output))
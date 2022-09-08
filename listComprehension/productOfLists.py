# Create a new list with multiplying 2 lists
a = [1,2,3,4,5]
b = [6,7,8,9,10]

z = []
for i in range(0, len(a)):
    z.append(a[i]*b[i])
print(z)

z2=[]
z2 = [a[i]*b[i] for i in range(len(a))]
print(z2)
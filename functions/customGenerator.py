#Custom Generator
#yield stores all values and returns
def customGen(x,y):
    while x < y:
        yield x
        x+=1

result = customGen(10,70)
for i in result:
    print(i)
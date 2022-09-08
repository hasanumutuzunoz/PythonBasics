def average(a,b):
    #print("Average of the numbers is : ", (a+b)/2)
    return (a+b)/2

result = average(10,20)
print(result)
print(average(b=10,a=20))


#default parameters
def defaultArguments(a = 30, b = 90):
    return (a+b)/2
print(defaultArguments())

def defaultArguments(a = 30, b = 90):
    return (a+b)/2
print(defaultArguments(a=70))

def defaultArguments(a = 30, b = 90):
    return (a+b)/2
print(defaultArguments(70))

def defaultArguments(a = 30, b = 90):
    return (a+b)/2
print(defaultArguments(70,60))
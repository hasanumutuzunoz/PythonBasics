# Decorator function that doubles a result of a function
def decor(func):
    def inner():
        result = func()
        return result*2
    return inner

# Apply decorator to a function automatically
@decor
def num():
    return 5

#resultFun = decor(num)
#print(resultFun())

print(num())
#Decorator function
def howAreYou(func):
    def inner(n):
        result = func(n)
        result += " How are you?"
        return result
    return inner

@howAreYou
def hello(name):
    return "Hello " + name

print(hello("Hasan"))
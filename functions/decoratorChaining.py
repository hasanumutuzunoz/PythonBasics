def square(func):
    def inner():
        n = func()
        return n*n
    return inner

def half(func):
    def inner():
        n = func()
        return n/2
    return inner

@square # this invokes second, (5*5=25) Result
@half   # this invokes first (10/2=5)
def num():
    return 10

print(num())
#Function inside a function
def display():
    def message():
        return "Hello "
    return message

func = display()
print(func())


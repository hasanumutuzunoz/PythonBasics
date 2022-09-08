# *arguments, **keywordArguments are the optional arguments
def myFunc(x, *arguments, **keywordArguments):
    print(x)

    #Add optional argument
    keywordArguments["id"] = 123;

    print(arguments) #print tuple
    for eachArg in arguments:
        print(eachArg)

    print(keywordArguments) #print dictionary
    for key, value in keywordArguments.items():
        print(key, value)

    modified_pos_param = arguments + (50,)
    my_func2(*modified_pos_param, **keywordArguments)


def my_func2(*args, **keyArgs):
    print(args)
    print(keyArgs)


myFunc(10, 10, 10, 20, 30, 40, 50, name = "Hasan", salary = 100000)




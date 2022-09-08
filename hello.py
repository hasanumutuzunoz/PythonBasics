# This is my first python program.

"""Multi line comment
    With double quote"""

'''Multi line comment 
    with singe quote '''

print("print with double quote")
print('print with single quote')

''' indentation is mandatory in python
    typically 4 space indent'''

x=int(input("Enter min number "))
y=int(input("Enter max number "))
i=x
if i % 2 == 0:
    i=x+1
while i<=y:
    print(i)
    i+=2




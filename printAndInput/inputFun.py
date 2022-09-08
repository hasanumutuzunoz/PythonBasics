"""s=input()
print(s)
s=input("ENter your name")
print(s)
i=int(input("Enter a int number")) #if 'int' not defined then it becomes string value
print(i)
print(type(i))"""

lst = [x for x in input("enter 3 numbers separated by space: ").split()]
print(lst)

lst2 = [int(x) for x in input("enter 3 int separated by comma: ").split(',')]
print(lst2)

lst3 = [float(x) for x in input("enter 3 float separated by comma: ").split(',')]
print(lst3)
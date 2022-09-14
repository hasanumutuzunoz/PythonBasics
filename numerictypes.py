# identifiers
# we cannot start identifier name with number
# we cannot use key words such as 'if' for identifier name

userid = 123
userID = 156 #case sensitive
user150ID = 150
user_150ID = 150
_user_150_ID = 150 #private _ at the beginning

a=13 #we dont need to define the variable type
b=100
c=-66
print(a,b,c)
print(type(a))
x=33.5
y=-25.8 #float
z=205 #int
print(x,y,z)
print(type(y))

d=3+5j #complex type
print(d)
print(type(d))

e=0B1010 #binary type defined, print converts into int
print("HERE IS BINARY!!!", e)
print(type(e))

f=0XFF #Hexadecimal type
print(f)
print(type(f))

g=True #bool
print(g)
print(type(g))
print(9>8)
print(9<8)

print(x)
h=int(x) #convert float to int
print(h)

i=float("22.5")
print(i)
print(type(i))

print(bin(990)) #convert int to binary
print(hex(1990)) #convert int to hexadecimal
print(oct(10)) #convert int to octa
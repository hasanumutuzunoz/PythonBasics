def cal(a,b):
    x = a + b
    y = a - b
    z = a * b
    u = a / b
    return x, y, z, u

result = cal(10,20)
print(result)

for i in result: print(i)
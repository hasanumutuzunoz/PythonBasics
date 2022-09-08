"""def cube(n):
    return n**3
print(cube(3))"""

# Lambda is an annonimous function without a name
# Return the cube of a number
f = lambda n:n**3
print(f(3))

# Is the number even lambda function
isEven = lambda n: "YES "if n%2==0 else "NO"
print(isEven(9))

# Calculate the sum of two numbers lambda
sum = lambda n1, n2: n1+n2
print(sum(3, 4))


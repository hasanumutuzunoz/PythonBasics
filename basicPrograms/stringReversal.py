#Print reverse string with using (s[::-1])
"""s = input("enter a string")
print(s[::-1])"""

#Print reverse string with using while loop
"""s = input("enter a string")
i = len(s)-1
result = ""
while i >= 0:
    result = result + s[i]
    i = i-1
print(result)"""

#Print string with join
"""s = "-++++=====".join(["a","b","c"])
print(s)"""

#Print reverse string with using join
s = input("Enter a string")
print("".join(reversed(s)))


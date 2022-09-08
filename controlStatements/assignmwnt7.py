n = int(input("Enter a number"))
i = 1
while i < n:
    i += 1
    if n%i == 0:
        print("This is not a prime number")
        break
    else:
        print("This is a prime number")
        break


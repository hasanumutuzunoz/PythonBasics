# Simple assessment error
try:
    num = int(input("Enter an even number: "))
    assert num % 2 == 0, "You entered an odd number"
except AssertionError as obj:
    print(obj)

# If we use try and except, any code after will be executed
print("After the assertion")

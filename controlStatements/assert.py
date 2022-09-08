"""The assert is used to continue to execute if the given condition evaluates to True.
If the assert condition evaluates to False, then it raises the AssertionError exception with the specified error message."""

x = int(input("enter a number greater than 10 "))
assert x>10, "Wrong number entered"
print("You entered ", x)

"""class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

password = input("Please enter a password")

if len(password) < 8:
    raise InvalidPasswordException("Invalid password. Please enter a password with at least 8 characters")
"""

try:
    password = input("Enter valid password")
    assert len(password) > 8, "Password has to be at least 8 characters"
except AssertionError as obj:
    print(obj)

print("Enter a valid password")


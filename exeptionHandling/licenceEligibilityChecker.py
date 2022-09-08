class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg

age = int(input("Enter the age"))
if age < 18:
    raise TooYoungException("You are too young")
elif age > 90:
    raise TooOldException("You are too old")
else:
    print("You are eligible")

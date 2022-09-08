import logging

logging.basicConfig(filename="myLog.log", level=logging.DEBUG)

try:
    f = open("myFile", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division is in progress")
    c = a / b
    #print(c)
    f.write("Writing %d into file" %c)

# We can modified user error
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
    logging.error("Division by zero")

except ValueError:
    print("Syntax error")

# If except cannot catch error than else will work
else:
    print("YEYY! You have entered a non zero number without syntax error, BRAVO! :D ")

# This finally is always executed even when the program stops by except error
finally:
    f.close()
    print("File closed")

print("Code after the exception")


# Open the file for writing
"""
f = open("myFile.txt", "w")
s = input("Enter text : ")
f.write(s)
f.close()
"""

# Write multiple strings
f = open("myFile.txt", "w")
print("Enter Text (Type # when you are done)")
s = ""
while s != "#":
    s = input()
    f.write(s + "\n") # (+ "\n") is for adding new line with every enter

f.close()
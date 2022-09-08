# To check if the file is exists, we need to import os, sys modules
import os, sys

if os.path.isfile("myFile.txt"):
    f = open("myFile.txt", "r")
else:
    print("File does not exist")
    sys.exit()

s = f.read()
print(s)
f.close()
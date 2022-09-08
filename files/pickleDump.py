# student.py  ||   pickleDump.py    ||       pickleLoad.py

import pickle, student

f = open("student.dat", "wb")
s = student.Student(123, "John", 90)

# Pickle Dump (SAVE) object into an file. pickle.dump(objectToDump, file)
pickle.dump(s, f)
f.close()
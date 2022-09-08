# student.py  ||   pickleDump.py    ||       pickleLoad.py

import pickle
f = open("student.dat", "rb")
obj = pickle.load(f) # Unpickle (LOAD) object from a file
obj.display()
f.close()
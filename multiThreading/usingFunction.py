from threading import *

def displayNumbers():
    i = 0
    print(current_thread().name)
    while(i<=10):
        print(i)
        i+=1

# Run function using a new thread
print(current_thread().name)
t = Thread(target=displayNumbers)

t.start()
#Print even numbers, odd numbers, 1 to 10.

from threading import *
from time import *

c = Condition()

def evenNumbers():
    c.acquire()
    for i in range (1,100):
        if i%2==0:
            print(i)
        sleep(0.1)
    c.notify()
    c.release()

def oddNumbers():
    c.acquire()
    for i in range(1,100):
        if i%2!=0:
            print(i)
        sleep(0.1)
    c.notify()
    c.release()

def mainThread():
    c.acquire()
    for i in range(1,11):
        print(i)
        sleep(0.1)
    c.notify()
    c.release()

t1 = Thread(target=evenNumbers)
t2 = Thread(target=oddNumbers)
t3 = Thread(target=mainThread)
t1.start()
t2.start()
t3.start()
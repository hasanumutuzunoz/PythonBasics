from threading import *
from time import sleep

class myThread:

    def displayNumbers(self):
        i = 0
        print(current_thread().name)
        sleep(1) #wait 1 seconds
        while (i <= 10):
            print(i)
            i += 1

# Run multi threads
obj = myThread()
t = Thread(target=obj.displayNumbers)
t.start()

t2 = Thread(target=obj.displayNumbers)
t2.start()

t3 = Thread(target=obj.displayNumbers)
t3.start()
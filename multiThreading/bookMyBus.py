from threading import *
from time import sleep
class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.lock = Lock()
        #self.lock = Semaphore() # You can either use semaphore or lock, doesn't matter

    def buy(self, seatsRequested):
        self.lock.acquire()  #Lock the seat for synchronization so others cannot buy the same ticket
        print("Total seats available:", self.availableSeats)

        if(self.availableSeats >= seatsRequested):
            print("Comfirming a seat")
            print("Processing the payment")
            sleep(5)
            print("Printing the ticket")
            self.availableSeats -= seatsRequested

        else:
            print("Sorry. No seats available.")
        self.lock.release()

obj = BookMyBus(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(5,))
t3 = Thread(target=obj.buy, args=(4,))
t4 = Thread(target=obj.buy, args=(1,))
t5 = Thread(target=obj.buy, args=(2,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
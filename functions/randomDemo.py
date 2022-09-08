from random import *

for i in range(10):
    print(random()) #print 10 random numbers between 0 and 1

for i in range(10):
    print(randint(1,50)) #print 10 random numbers between 1 to 50

for i in range(10):
    print(uniform(1,50)) #Print 10 random float numbers between 1 to 50
                         #Not including 1 and 50

for i in range(10):
    print(randrange(40,50)) # rand 40 to 50

for i in range(10):
    print(randrange(1,10,5)) # rand 1 to 10 with step 5

list = ["Java", "python", "devops", "aws"]
for i in range(10):
    print(choice(list)) #print random 10 elements from the list
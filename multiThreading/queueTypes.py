import queue

#Print Reverse with LifoQueue
lq = queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(500)
lq.put(50)
while not lq.empty():
    print(lq.get(), end=" ")

print()

#Print Priority Value
pq = queue.PriorityQueue()
pq.put(400)
pq.put(100)
pq.put(500)
pq.put(50)
while not pq.empty():
    print(pq.get(), end=" ")

print()

#Print Other Variable Type Priority Value
pq = queue.PriorityQueue()
pq.put((400, "John"))
pq.put((100, "Bob"))
pq.put((500, "Max"))
pq.put((50, "Jack"))
while not pq.empty():
    print(pq.get()[1], end=" ") #Get only names with [1]

print()

q = queue.Queue()
q.put(400)
q.put(100)
q.put(500)
q.put(50)
while not q.empty():
    print(q.get(), end=" ")
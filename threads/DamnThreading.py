# multiple threads can share the same queue
from queue import Queue
from threading import Thread

def shareQueue(q):
    while True:
        print(q.get())
        q.task_done()


q = Queue() # The queue is created
num_threads = 5     # We'll have 5 threads
for i in range(num_threads):
    workerThread = Thread(target=shareQueue, args=(q,))
    workerThread.setDaemon(True)
    workerThread.start()


for x in range(50):
    q.put(x)

# Using the koin method the program will wait until the queue is empty 
# and the threads are done working(info comes from the task_done method)
q.join()
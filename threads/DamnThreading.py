# multiple threads can share the same queue
from queue import Queue
from threading import Thread

def shareQueue(q):
    while true:
        print(q.get())
        q.task_done()


q = Queue() # The queue is created
num_threads = 5     # We'll have 5 threads
for i in range(num_threads):
    workerThread = Thread(target=shareQueue, args=(q,))
    workerThread.setDaemon(True)
    workerThread.start()
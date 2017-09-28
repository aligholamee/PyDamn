# Because the data is passed between producer and consumer threads safely and locking is handled by the caller
# multiple threads can work on the same queue instance
import queue

fq = queue.Queue()

# add an element
fq.put(2)

# removes element at the other end
fq.get()


# LIFO
lq = queue.LifoQueue()

# add an element
lq.put(2)

# removes element at the same head
lq.get()

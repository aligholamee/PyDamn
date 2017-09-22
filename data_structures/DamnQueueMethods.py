import queue

q = queue.Queue(3)
q.put(1)
q.put(2)
q.put(3)

print(q.qsize())
print(q.empty())
print(q.full())

# call the block for some time until there is a free slot
q.put(4, block=True, timeout=500)


import queue


class Methoz(object):
    def __init__(self, priority):
        self.priority = priority
        return
    
    # Less than is used to override the functionality of the < operator
    def __lt__(self, other):
        return self.priority < other.priority

q = queue.PriorityQueue()
q.put(Methoz(55))
q.put(Methoz(5))
q.put(Methoz(42))

while not q.empty():
    print(q.get().priority)

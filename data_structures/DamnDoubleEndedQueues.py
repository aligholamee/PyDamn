from collections import deque

queue = deque()
queue.append("b")
queue.appendleft("a")
queue.pop()
queue.popleft()

# we can set the maximum length for the following queue
d = deque(maxlen=5)

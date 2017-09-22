# using deque from collections to implement the queue
from collections import deque


queue = deque([
    "a", 
    "b",
    "c"
])

queue.append("e")
queue.append("d")
queue.popleft()
queue.popleft()
print(queue)

# Reverese queue
# A reverse queue can be implemented by opting for appendleft instead of append and pop instead of popleft

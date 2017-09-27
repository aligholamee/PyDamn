# Coroutine can be find inside the python's types module
# The coroutine function is used to transform a generator function into a coroutine function, returning 
# a generator-based function.
# this couroutine is both a generator iterator and an awaitable coroutine object.
import types

def my_gen():
    yield 1
    yield 2


myCoroutineObject = types.coroutine(my_gen)

# the new coroutine object is still iterable
for element in myCoroutineObject:
    print(element)

# Output will be 
# 1
# 2

# the generator based coroutine is awaitable, but does not necessarily implement __await__()

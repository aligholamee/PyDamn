# bytes object is an immutable sequence of single bytes
# it behaves like a sequence of integers but some of it's methods only work with ASCII data.

# create a bytes object from a iterable of integers
cbyte = bytes(range(4))
print(cbyte)

# create a bytes object from a hexadecimal string
hexbyte = bytes('2EF0')
print(hexbyte)

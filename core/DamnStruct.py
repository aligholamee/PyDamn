# Python's struct module has some function to convert between the text and binary data
# in both directions

import struct

# Get a bytes object containing some values
bytesObject = struct.pack('hh', 3, 5)
print(bytesObject)

# Unpack the buffer
# print(struct.unpack('hh', ?)

# Return the size of the struct
struct.calcsize('hh')
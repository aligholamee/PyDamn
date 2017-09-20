a = bytes(b"abc")   # bytes object

d = a.replace(b"b", b"f") # this will work
c = a.replace("b", "f")    # this will work
b = a.replace(b"b", "f")    # this will work
#print(b)
#print(c)
#print(d)


# counting the occurances of a subsequence
testString = bytearray(b"HelloWorld!")
print(testString.count(b"o"))

# create a copy of the bytes 0 filled to a specified width
width2 = bytes(b"54")
width6 = width2.zfill(6)
print(width2)
print(width6)
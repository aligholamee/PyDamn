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

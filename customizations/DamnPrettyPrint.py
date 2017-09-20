# Pyhton provides a way of generating eye pleasing representations of data structures when printing by using the pprint module.
import pprint
from math import sqrt

data = [(x, {y: y*y for y in range(2)}) for x in range(4)]

# print(pprint.pformat(data, width=20))


# y is nested into the x's loop
# z is not nested thus is repeated for the whole process again
customizedData = [(x, {y: sqrt(y) for y in range(10)}) for x in range(2),{z: z for z in range(5)}]
print(pprint.pformat(customizedData, width=50))
# Pyhton provides a way of generating eye pleasing representations of data structures when printing by using the pprint module.
import pprint

data = [(x, {y: y*y for y in range(2)}) for x in range(4)]

print(pprint.pformat(data, width=20))
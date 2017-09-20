# Named tuples are easy to create and lightweight object types.
# Named tuples are immutable.
# meaning that their content cannot be changed after they are created.


# representing two simple points with a normal tuple
from math import sqrt

p1 = (4.3, 6.1)
p2 = (2.1, 3.4)

line_length1 = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
msg = 'the length of the line is: ' + str(line_length1)
print(msg)



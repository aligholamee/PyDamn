# Named tuples are easy to create and lightweight object types.
# Named tuples are immutable.
# meaning that their content cannot be changed after they are created.


# representing two simple points with a normal tuple
from math import sqrt
from collections import namedtuple

p1 = (4.3, 6.1)
p2 = (2.1, 3.4)

line_length1 = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
msg = 'the length of the line is: ' + str(line_length1)
print(msg)

# now representing two dots with a named tuple
Point = namedtuple('Point', 'X Y')
pt1 = Point(4.3, 6.1)
pt2 = Point(2.1, 3.4)

line_length2 = sqrt((pt1.X - pt2.X)**2 + (pt1.Y - pt2.Y)**2)
msg2 = 'the length of the line is: ' + str(line_length2)
print(msg2)
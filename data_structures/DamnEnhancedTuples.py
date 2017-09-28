# The collections module privdes an enhanced version of a tuple
from collections import namedtuple

# create a named tuple object
point = namedtuple('point3D', 'x y z')

A = point(x=3, y=6, z=5)
print(A)

# access a specific member
print(A.x)

# namedtuple are backwards compatible with the normal tuples, member
# access can also be done with the indexes
print(A[0])

# Converting a namedtuple to a dict
print(A._asdict())
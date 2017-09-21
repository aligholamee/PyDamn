# cmath is sepcialised for operations on complex numbers
import cmath
import math

# both are the same to create a complex number
z = complex(4, 5)
z = 4 + 5j

print(z.real)
print(z.imag)

# get the phase of a number - both are the same
print(math.atan2(z.imag, z.real))
print(cmath.phase(z))

# get the polar representation
print(cmath.polar(z))

# same functions for the complex numbers
print(cmath.log(z))
print(cmath.cos(z))

import math

# constants
print(math.pi)
print(math.e)

# check if a var is Nan of INF
var = 6.886868686868
math.isnan(var)
math.isinf(var)

# separate the whole and the fractional sections of a number
print(math.modf(var))

# trigonometric functions
math.sin(var)
math.atan(var)

# angular conversions
math.degrees(var)   # radians to degrees
math.radians(var)     # degrees to radians

# power and log
math.exp(var)   # returns e**var
math.log(var)   # base is e by default
math.pow(var,var)

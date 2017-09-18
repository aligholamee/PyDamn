# The dictionary is Python's main mapping type. It maps hashable values to arbitrary objects as long as they provide the key integrity.


# 1st syntax
d1 = {
    'first': 1,
    'second': 2,
    'third': 3 
}

# 2nd syntax
d2 = dict(
    first = 1,
    second = 2
)


# now displaying the dictionaries
print(d1['first'])
print(d2)


# We can use update t0o concatenate two dictionaries
x1 = {
    'fruit1': 'orange',
    'fruit2': 'apple'
}

x2 = {
    'fruit3': 'bannana',
    'fruit4': 'mavricks'
}

x1.update(x2)
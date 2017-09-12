

# Validating the number's equality
num = 6
print('Assignment 1:')
print(num == 6)

num2 = 10
print('Assignment 2:')
print(num < 10)


# Boolean operators
num3 = 25
str = 'Hello World!'
if str=='Hello World!' and num==25:
    print('Success!')
elif str == 'Hello World!' and num > 2:
    print('Success!')

# Membership operator 'in'
x = 5
nums = [1, 2, 3, 4, 5]
if x in nums:
    print('Found!')
else:
    print('Not Fonud!')

# The 'is' operator
# Used to match the instances of a variable
blob = 'Hello World'
blob2 = blob

print(blob2 is blob)
# This will print true


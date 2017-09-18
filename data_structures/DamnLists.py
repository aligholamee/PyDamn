# stack works like LIFO
stack = [1, 2, 3]
stack.append(4)
stack.append(5)

print(stack)

stack.pop()
print(stack)

# there is no push method here
# we use append instead

# del statement is used to delete the element from the list but it doesnt return anything
del stack[0:2]
print(stack)

# deletes the entire list
del stack[:]
print(stack)
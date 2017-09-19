# zip returns a list of tuples wbere the n th tuple contains the nth item from each of the lists passed into the function

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
squares = [1, 4, 9, 16]

zipped_list = zip(letters, numbers, squares)
print(zipped_list)
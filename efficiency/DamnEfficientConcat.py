# Strings in Python are immutable. The advantage os that strings can be directly used as keys in dictionaries. 
# String copies can be shared among multiple variable bindings.
# But the disadvantage is that if you want to amend something in an existing string, then you have to 
# create a new one. This leads to significant inefficiencies.

# A common mistake when building big lists
s = ""
list = ['hi', 'do', 'like', 'me']
for substring in list: 
    s += substring
print(s)

# Instead
p = ""
p = "".join(list)
print(p)

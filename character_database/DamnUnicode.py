# Python's self explanatory module called unicodedata provudes the user with acces to the ucode character database.

# lookup a character name with lookup
import unicodedata
print(unicodedata.lookup('RIGHT SQUARE BRACKET'))

# Get a character's name with name
print(unicodedata.name(u'~'))

# Get the category of a character
print(unicodedata.category(u'X'))
# L = letter
# u = uppercase


# TO get the version of the Unicode database currently used: 
print(unicodedata.unidata_version)
# using the unicodedata it's easy to normalize any unicode data string
import unicodedata 

# Normalization Form Compatiblity Decomposition
data = u'INVEFAAM'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
import re

txt = 'The rain in Spain'
x = re.search("^The.*Spain", txt)

# print(x)

# span: 1 - 3999 incl
# I
# V
# X
# L
# D
# C
# M


# [] set of characters
# * zero or more occurrences
# \D string does not contain digits
now = 'MXXV'
numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    }


exp = "[IVXLDCM]*"
y = re.match(exp, now)
print(y)
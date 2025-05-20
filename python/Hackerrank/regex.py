import re

# txt = 'The rain in Spain'
# x = re.search("^The.*Spain", txt)

# # print(x)

# # span: 1 - 3999 incl
# # I
# # V
# # X
# # L
# # D
# # C
# # M


# # [] set of characters
# # * zero or more occurrences
# # \D string does not contain digits
# now = 'MXXV'
# numbers = {
#     'IX': 9,
#     'IV': 4,
#     'I': 1,
#     'V': 5,
#     'XL': 40,
#     'XC': 90,
#     'X': 10,
#     'L': 50,
#     'CD': 400,
#     'CM': 900,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
#     }

# exp = "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
# y = re.match(exp, now)
# print(y)


# phone numbers
# 10 digit number
# start with 7, 8, 9

# n = 2
# inp = [9587456281, 1252478965]

# exp = "^(7|8|9\d{9})$"

# for number in inp:
#     if re.match(exp, str(number)):
#         print('YES')
#     else:
#         print('NO')

n = 2

input = ('DEXTER <dexter@hotmail.com>', 'VIRUS <virus!@variable.:p>')

 
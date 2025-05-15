
size = 5
fill = '-'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# center_letter = 'a'
# width = size *3 +2
# print(width)
result = []
# j = size

for i in range(size):
    for j in range(size):
        index = size-i
        print(alphabet[index])


# for i in range(int(width/2), size, -1):
#     j -= 1
#     letter_list = alphabet[j]
#     print(letter_list)
#     result.append(letter_list.center(width, fill))
# print(line for line in result)

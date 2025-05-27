def front_back(str):
    length = len(str)
    if length == 0 or length == 1:
        return ''
    first = str[0]
    last = str[length-1]
    new_list = []
    for i in range(length):
        if i == 0:
            new_list.append(last)
        elif i == length-1:
            new_list.append(first)
        else:
            new_list.append(str[i])
    return ''.join(new_list)


print(front_back('abcdef'))

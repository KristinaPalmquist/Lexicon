def last2(str):
    length = len(str)
    count = 0
    if length < 2:
        return 0
    last2 = str[length-2]+str[length-1]
    for i in range(length-2):
        if str[i] + str[i+1] == last2:
            count += 1
    return count


print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))

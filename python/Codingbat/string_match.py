def string_match(a, b):
    lengthA = len(a)
    print(lengthA)
    for i, charA in enumerate(a):
        if i == lengthA-1:
            print('end')
            continue
        for j, charB in enumerate(b):
            if i == j and charA == charB and a[i+1] == b[j+1]:
                return i


print(string_match('xxcaazz', 'xxbaaz'))


def xyz_there(str):
    for i in range(len(str)-3):
        print(str[i], str[i+1], str[i+2], str[i+3])
        if (i == 0 and str[i] == 'x'
                and str[i+1] == 'y'
                and str[i+2] == 'z'):
            return True
        elif str[i] == '.':
            continue
        elif (
                str[i+1] == 'x'
                and str[i+2] == 'y'
                and str[i+3] == 'z'
        ):
            return True
    return False


print(xyz_there('xyz'))

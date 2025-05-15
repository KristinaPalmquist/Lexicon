def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-2):
        control = string[i:(i+len(sub_string))]
        if control == sub_string:
            count += 1
    return count

string = 'ABCDCDC'
sub_string = 'CDC'

count = count_substring(string, sub_string)
print(count)
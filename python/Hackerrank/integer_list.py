
list = []
N = 12


str = (
    'insert 0 5', 
    'insert 1 10', 
    'insert 0 6', 
    'print', 
    'remove 6', 
    'append 9', 
    'append 1', 
    'sort', 
    'print', 
    'pop', 
    'reverse', 
    'print')

list = []
for n in range(N):
    inp = str[n].split()
    instr = inp[0]
    if instr == 'insert':
        i = int(inp[1])
        e = int(inp[2])
        list.insert(i, e)
    if instr == 'print':
        print(list)
    if instr == 'remove':
        e = int(inp[1])
        list.remove(e)
    if instr == 'append':
        e = int(inp[1])
        list.append(e)
    if instr == 'sort':
        list.sort()
    if instr == 'pop':
        list.pop()
    if instr == 'reverse':
        list.reverse()

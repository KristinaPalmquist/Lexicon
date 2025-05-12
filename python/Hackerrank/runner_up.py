
inp = '2 3 6 6 5'
n = 5

arr =map(int, inp.split())
my_list = (list(arr))
my_list.sort()
my_list.reverse()
first = my_list[0]
second = 0
for x in my_list:
    if x < first:
        second = x
        break
        
    
print(x)


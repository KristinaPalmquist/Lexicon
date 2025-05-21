
""" Python Lambda Functions """
""" Lambda functions explained: https://www.youtube.com/watch?v=KR22jigJLok """

# def add(x, y):
#     return x + y
# print(add(4, 5))

# ref = lambda x, y: x + y
# print(ref(4, 5))

# print((lambda x,y: x+y)(4,5))


# def my_map(my_func, my_iter):
#     result = []
#     for item in my_iter:
#         result.append(my_func(item))
#     return result
# nums = [3,4,5,6,7]
# print(*my_map((lambda x: x+1), nums))


def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result

nums = [3,4,5,6,7]
cubed = my_map(lambda x: x**3, nums)
print(cubed)
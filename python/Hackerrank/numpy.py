import numpy

test_input1 = '2 2'
test_input2 = '1 2'
test_input3 = '3 4'


n, m = map(int, input().split())
array = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array), 11))
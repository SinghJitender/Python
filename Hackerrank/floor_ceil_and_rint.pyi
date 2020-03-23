import numpy

numpy.set_printoptions(sign=' ')
numbers = list(map(float,str(input()).split(" ")))
print(numpy.floor(numbers))
print(numpy.ceil(numbers))
print(numpy.rint(numbers))
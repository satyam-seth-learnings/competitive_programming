import numpy

# logic-1
# print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))

# Logic-2
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(*map(int,input().split())))
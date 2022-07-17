import numpy
numpy.set_printoptions(legacy='1.13')

# Logic-1
n=int(input())
arr=numpy.array([input().split() for _ in range(n)],float)
print(numpy.linalg.det(arr))

# Logic-2
# print(numpy.linalg.det([list(map(float,input().split())) for _ in range(int(input()))]))
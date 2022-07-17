import numpy
n,m=map(int,input().split())
a=numpy.array([list(map(int,input().split())) for _ in range(n)])
b=numpy.array([list(map(int,input().split())) for _ in range(n)])
print(a+b,a-b,a*b,a//b,a%b,a**b,sep='\n')
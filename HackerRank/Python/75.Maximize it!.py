from itertools import product
k,m=map(int,input().split())
lst=[]
def fun(nums):
    return sum([x**2 for x in nums])%m
for _ in range(k):
    lst.append(map(int,input().split()[1:]))
print(max(map(fun,product(*lst))))
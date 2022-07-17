from itertools import combinations
n,a,k=int(input()),input().split(),int(input())
c=tuple(combinations(a,k))
f=[i for i in c if 'a' in i]
print(f'{len(f)/len(c):0.3f}')
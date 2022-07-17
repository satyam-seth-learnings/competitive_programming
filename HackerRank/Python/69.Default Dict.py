from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
for i in range(1,n+1):
    d[input()].append(i)
for j in range(m):
    index=input()
    if d[index]==[]:
        print(-1)
    else:
        print(*d[index])
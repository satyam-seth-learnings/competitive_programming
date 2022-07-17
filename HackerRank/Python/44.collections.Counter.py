# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
x=int(input())
s=list(map(int,input().split()))
col=Counter(s)
e=0
for i in range(int(input())):
    d=list(map(int,input().split()))
    if col[d[0]]>0:
        e+=d[1]
        col[d[0]]-=1
print(e)
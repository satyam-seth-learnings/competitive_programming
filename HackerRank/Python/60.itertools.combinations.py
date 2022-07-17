# Logic-1
from itertools import combinations
s,k=input().split()
for i in range(1,int(k)+1):
    for j in combinations(sorted(s),i):
        print(*j,sep='')

# Logic-2
from itertools import combinations
s,k=input().split()
for i in range(1,int(k)+1):
    for j in combinations(sorted(s),i):
        print(''.join(j))

# Logic-3
from itertools import combinations
s,k=input().split()
print(*[''.join(j) for i in range(1,int(k)+1) for j in combinations(sorted(s),i)],sep='\n')
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Logic-1
from itertools import combinations_with_replacement
s,k=input().split()
for i in combinations_with_replacement(sorted(s),int(k)):
    print(*i,sep='')

# Logic-2
from itertools import combinations_with_replacement
s,k=input().split()
for i in combinations_with_replacement(sorted(s),int(k)):
    print(''.join(i))

# Logic-3
from itertools import combinations_with_replacement
s,k=input().split()
print(*[''.join(i) for i in combinations_with_replacement(sorted(s),int(k))],sep='\n')
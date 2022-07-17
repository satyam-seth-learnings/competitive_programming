# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
de=deque()
for i in range(int(input())):
    op_ar=input().split()
    if op_ar[0]=='append':
        de.append(op_ar[1])
    elif op_ar[0]=='appendleft':
        de.appendleft(op_ar[1])
    elif op_ar[0]=='pop':
        de.pop()
    elif op_ar[0]=='popleft':
        de.popleft()
print(*de)
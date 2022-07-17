# Logic-1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in range(int(input())):
    input()
    d=deque(map(int,input().split()))
    top_of_stack=0
    if d[0]>=d[-1]:
        top_of_stack=d.popleft()
    else:
        top_of_stack=d.pop()
    while d:
        if d[0]>=d[-1] and d[0]<=top_of_stack:
            top_of_stack=d.popleft()
        elif d[-1]>=d[0] and d[-1]<=top_of_stack:
            top_of_stack=d.pop()
        else:
            break
    if d:
        print('No')
    else:
        print('Yes')

# Logic-2
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
for _ in range(int(input())):
    input()
    d=deque(map(int,input().split()))
    stack=[]
    if d[0]>=d[-1]:
        stack.append(d.popleft())
    else:
        stack.append(d.pop())
    while d:
        if d[0]>=d[-1] and d[0]<=stack[-1]:
            stack.append(d.popleft())
        elif d[-1]>=d[0] and d[-1]<=stack[-1]:
            stack.append(d.pop())
        else:
            break
    if d:
        print('No')
    else:
        print('Yes')
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n=int(input())
stu=namedtuple('stu',input().split())
marks=[int(stu._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks)/len(marks))
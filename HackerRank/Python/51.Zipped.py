# Enter your code here. Read input from STDIN. Print output to STDOUT
# Logic-1
n,x=map(int,input().split())
l=[]
for _ in range(x):
    l.append(map(float,input().split()))
for i in zip(*l):
    print(sum(i)/x)

# Logic-2
# [print(sum(i)/len(i)) for i in zip(*[map(float,input().split()) for _ in range(int(input().split()[1]))])]
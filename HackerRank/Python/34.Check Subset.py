# Enter your code here. Read input from STDIN. Print output to STDOUT
l=[]
for i in range(int(input())):
    n1=int(input())
    s1=set(map(int,input().split()))
    n2=int(input())
    s2=set(map(int,input().split()))
    l.append(s1.issubset(s2))
for i in l:
    print(i)
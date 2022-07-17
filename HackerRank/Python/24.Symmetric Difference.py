# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
a=list(s1.symmetric_difference(s2))
for i in sorted(a):
    print(i)
# Enter your code here. Read input from STDIN. Print output to STDOUT
s1=set(map(int,input().split()))
l=[]
for i in range(int(input())):
    s2=set(map(int,input().split()))
    l.append(s2.issubset(s1) and len(s1)>len(s2))
print(all(l))
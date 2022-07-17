# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
A=set(map(int,input().split()))
for i in range(int(input())):
    cmd,args=input().split()
    B=set(map(int,input().split()))
    eval('A.'+cmd+'(B)')
print(sum(A))

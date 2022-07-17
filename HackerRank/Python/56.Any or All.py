# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
l=input().split()
print(all(map(lambda x:int(x)>0,l)) and any(map(lambda x:x==x[::-1],l)))
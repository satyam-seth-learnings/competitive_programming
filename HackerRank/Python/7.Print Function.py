# Read an integer N.
# Without using any string methods, try to print the following:
# 123....N
# Note that "..." represents the values in between.

# Logic-1
# n = int(input())
# for i in range (n):
#     print(i+1,end="")

# Logic-2
print(*[i for i in range(1,int(input())+1)],sep="")
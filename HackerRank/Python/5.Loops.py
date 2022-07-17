# Read an integer N. For all non-negative integers i<N , print i2. See the sample for details.
# Logic-1
# n=int(input())
# for i in range (n):
#     print(i**2)

# Logic-2
# print(*[i**2 for i in range(int(input()))],sep='\n')

# Logic-3
print(*(i**2 for i in range(int(input()))),sep='\n')